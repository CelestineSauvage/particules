#coding: utf-8
from agent import Agent
import random

"""
Environnement sous forme de grille 2D (coordonnées entières et environnement discret) où sont placés les particules.
Celui-ci peut-être torique ou non
"""
class Env:

    def __init__(self, n, l, h, t):
        self.l = l
        self.h = h
        self.grid = []
        self.t = t

    def generate(self, canvas, n):
        """
        Place n agent aléatoirement sur la grille
        """
        i = 0
        grid = [[0] * (self.h) for _ in range(self.l)] # tableau vide
        l_agents = []
        while (i < n) : # on génère les n agents dans le tableau
            # pour chaque agent, on le place aléatoirement sur la map
            posX = random.randint(0, self.l-1)
            posY = random.randint(0, self.h-1)
            if (self.getAgent(posX, posY) == 0): # si pas de bille sur cette case
                while(True):
                    pasX, pasY = (random.randint(-1, 1), random.randint(-1, 1))
                    if ( (pasX,pasY) != (0,0)):
                        break
                agent = Agent(canvas, posX, posY, pasX, pasY)
                grid[posX][posY] = agent
                l_agents.append(agent)
                i += 1
        self.grid = grid
        return l_agents

    def getAgent(self, posX, posY):
        """
        Retourne ce qu'il y a à la position x,y
        """
        for i in range (max(0, posX-5), min(self.l-1, posX+5)):
            for j in range (max(0, posY-5), min(self.h-1, posY+5)):
                try:
                    agent = self.grid[i][j]
                    if (agent != 0):
                        return agent
                except:
                    pass
        return 0

    def unsetAgent(self, posX, posY):
        self.grid[posX][posY] = 0

    def setAgent(self, agent, posX, posY):
        """
        Set un agent à la position x, y sur la grille
        """
        #newpos
        newPosX = posX
        newPosY = posY

        self.unsetAgent(agent.posX, agent.posY) # on enlève la bille
        dec = abs(agent.pasX * agent.pasY) # dans quelle direction se déplace la particule ?
        if (posX < 0): # on replace correctement la boule si besoin
            newPosX += 2 - dec
            agent.pasX *= -1
        if ((self.l - posX) <= 1):
            newPosX -= 2 - dec
            agent.pasX *= -1
        if (posY < 0):
            newPosY += 2 - dec
            agent.pasY *= -1
        if ((self.h - posY) <= 1):
            newPosY -= 2 - dec
            agent.pasY *= -1

        maybeAgent = self.getAgent(newPosX, newPosY) # retourne ce qui se trouve à la nouvelle position
        if (maybeAgent != 0): # si il y a un agent à la nouvelle case, on échange les directions
            agent.swap_pas(maybeAgent)
            newPosX = agent.posX + agent.pasX # nouveau posX
            newPosY = agent.posY + agent.pasY # nouveau posY

        self.grid[newPosX][newPosY] = agent
        agent.posX = newPosX
        agent.posY = newPosY
        # try :
        #     if (env.t): # si le monde est tellurique
        #         newPosX = (posX+l)%l
        #         newPosY = (posY+h)%h
        #     else : # sinon
        #         newPosX = posX
        #         newPosY = posY
        #
                # dec = abs(agent.pasX * agent.paxY) # dans quelle direction se déplace la particule ?
                # if (posX < 0): # on replace correctement la boule si besoin
                #     newPosX += 2 - dec
                # if ((l - posX) < 0):
                #     newPosX -= 2 - dec
                # if (posY < 0):
                #     newPosX += 2 - dec
                # if ((l - posY) < 0):
                #     newPosX -= 2 - dec
        #
        #     self.grid[newPosX][newPosY] = agent
        #     agent.posX = newPosX
        #     agent.posY = newPosY
        # except :
        #     print("Erreur d'indice pour set un agent")

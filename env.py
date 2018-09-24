#coding: utf-8
from agent import Agent
import random

"""
Environnement sous forme de grille 2D (coordonnées entières et environnement discret) où sont placés les particules.
Celui-ci peut-être torique ou non
"""
class Env:

    def __init__(self, n, l, h, t, size, seed):
        self.l = l
        self.h = h
        self.grid = []
        self.t = t
        self.size = size
        self.seed = seed

    def generate(self, canvas, n):
        """
        Place n agent aléatoirement sur la grille
        """
        i = 0
        self.grid = [[0] * (self.h) for _ in range(self.l)] # tableau vide
        l_agents = []
        random.seed(self.seed) # initialise avec une graine le random
        while (i < n) : # on génère les n agents dans le tableau
            # pour chaque agent, on le place aléatoirement sur la map
            posX = random.randint(0, self.l-1)
            posY = random.randint(0, self.h-1)
            if (self.getAgent(posX, posY) == 0): # si pas de bille sur cette case
                while(True):
                    pasX, pasY = (random.randint(-1, 1), random.randint(-1, 1))
                    if ( (pasX,pasY) != (0,0)):
                        break

                agent = Agent(canvas, posX, posY, pasX, pasY, self.size, i)
                self.grid[posX][posY] = agent
                l_agents.append(agent)
                i += 1
                #print("i"+str(i)+"posX "+str(posX)+"posY "+str(posY)+"pasX "+str(pasX)+"pasY "+str(pasY))
        return l_agents

    def getAgent(self, posX, posY):
        """
        Retourne ce qu'il y a à la position x,y
        """
        return self.grid[posX][posY]

    def unsetAgent(self, posX, posY):
        self.grid[posX][posY] = 0

    def setAgent(self, agent, posX, posY):
        """
        Set un agent à la position x, y sur la grille
        """
        #newpos
        newPosX = posX
        newPosY = posY
        #
        # print("i ", agent.id)
        # print("posX ", posX)
        # print("posY ", posY)
        self.unsetAgent(agent.posX, agent.posY) # on enlève la bille
        #dec = abs(agent.pasX * agent.pasY) # dans quelle direction se déplace la particule ?
        if (self.t): # si le monde est torique
            newPosX = (newPosX+self.l)%self.l
            newPosY = (newPosY+self.h)%self.h
            # print("newPosX ", newPosX)
            # print("newPosY ", newPosY)
            # print("--------------")
        else : # sinon
            if (posX < 0): # on replace correctement la boule si besoin
                newPosX += 2
                agent.pasX *= -1
            if ((self.l - posX) <= 1):
                newPosX -= 2
                agent.pasX *= -1
            if (posY < 0):
                newPosY += 2
                agent.pasY *= -1
            if ((self.h - posY) <= 1):
                newPosY -= 2
                agent.pasY *= -1

        maybeAgent = self.getAgent(newPosX, newPosY) # retourne ce qui se trouve à la nouvelle position
        if (maybeAgent != 0): # si il y a un agent à la nouvelle case, on échange les directions
            agent.swap_pas(maybeAgent)
            if (self.t):
                newPosX = (newPosX+self.l)%self.l
                newPosY = (newPosY+self.h)%self.h
            else :
                newPosX = agent.posX + agent.pasX # nouveau posX
                newPosY = agent.posY + agent.pasY # nouveau posY

        try :
            self.grid[newPosX][newPosY] = agent
        except :
            print("l ", self.l)
            print("h ", self.h)
            print("posX ", posX)
            print("posY ", posY)
            print("newPosX ", newPosX)
            print("newPosY ", newPosY)
            exit()
        agent.posX = newPosX
        agent.posY = newPosY

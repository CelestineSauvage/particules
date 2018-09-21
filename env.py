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
            if (grid[posX][posY] == 0): # si pas de bille sur cette case
                agent = Agent(canvas, posX, posY, random.randint(-1, 1), random.randint(-1, 1))
                grid[posX][posY] = agent
                l_agents.append(agent)
                i += 1
        self.grid = grid
        return l_agents

    def getAgent(self, posX, posY):
        """
        Retourne ce qu'il y a à la position x,y
        """
        try :
            return self.grid[posX][posY]
        except :
            print("Erreur d'indice pour retrouver un agent")

    def unsetAgent(self, posX, posY):
        self.grid[posX][posY] = 0

    def setAgent(self, agent, posX, posY):
        """
        Set un agent à la position x, y sur la grille
        """
        try :
            if (env.t): # si le monde est tellurique
                newPosX = (posX+l)%l
                newPosY = (posY+h)%h
            else : # sinon
                newPosX = posX
                newPosY = posY

                dec = abs(agent.pasX * agent.paxY) # dans quelle direction se déplace la particule ?
                if (posX < 0): # on replace correctement la boule si besoin
                    newPosX += 2 - dec
                if ((l - posX) < 0):
                    newPosX -= 2 - dec
                if (posY < 0):
                    newPosX += 2 - dec
                if ((l - posY) < 0):
                    newPosX -= 2 - dec

            self.grid[newPosX][newPosY] = agent
            agent.posX = newPosX
            agent.posY = newPosY
        except :
            print("Erreur d'indice pour set un agent")

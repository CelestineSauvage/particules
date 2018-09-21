#coding: utf-8

"""
Contient les caractéristiques des particules et une méthode decide(), destinée à coder le processus de décision de ces particules
"""
class Agent:

    def __init__(self, canvas, posX, posY, pasX, pasY):
        # position initiale de la particule
        self.posX = posX
        self.posY = posY

        # direction initiale de la particule
        self.pasX = pasX
        self.pasY = pasY

        self.canvas = canvas
        self.circle = canvas.create_oval([pasX, pasY, (pasX)+10, (pasY)+10], outline="red", fill="red")

    def swap_pas(self, agent):
        """
        Swap la direction de 2 agents
        """
        agent.pasX, agent.pasY = self.pasX, self.pasY

    def decide(self, env):
        """
        Méthode qui permet à un agent de décider de son comportement
        """
        newPosX = self.posX + self.pasX # nouveau posX
        newPosY = self.posY + self.pasY # nouveau posY

        env.unsetAgent(self.posX, self.posY)

        env.setAgent(self, newPosX, newPosY)
        self.canvas.coords(self.circle, newPosX, newPosY, newPosX + 10, newPosY + 10)
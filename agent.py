#coding: utf-8

"""
Contient les caractéristiques des particules et une méthode decide(), destinée à coder le processus de décision de ces particules
"""
class Agent:

    def __init__(self, canvas, posX, posY, pasX, pasY, size):
        # position initiale de la particule
        self.posX0 = posX
        self.posY0 = posY
        self.posX1 = posX+size
        self.posY1 = posY+size

        # direction initiale de la particule
        self.pasX = pasX
        self.pasY = pasY

        self.size = size

        self.canvas = canvas
        self.circle = canvas.create_oval([posX, posY, self.posX1, self.posY1], outline="grey", fill="grey")

    def swap_pas(self, agent):
        """
        Swap la direction de 2 agents
        """
        agent.pasX, agent.pasY, self.pasX, self.pasY = self.pasX, self.pasY, agent.pasX, agent.pasY
        self.canvas.itemconfig(self.circle, outline="red", fill="red")
        agent.canvas.itemconfig(agent.circle, outline="red", fill="red")

    def decide(self, env):
        """
        Méthode qui permet à un agent de décider de son comportement
        """
        newPosX = self.posX + (self.pasX*self.size) # nouveau posX
        newPosY = self.posY + (self.pasY*self.size) # nouveau posY

        env.setAgent(self, newPosX, newPosY)
        self.canvas.coords(self.circle, self.posX, self.posY, self.posX + self.size, self.posY + self.size)

#coding: utf-8

"""
Contient les caractéristiques des particules et une méthode decide(), destinée à coder le processus de décision de ces particules
"""
class Agent:

    def __init__(self, canvas, posX, posY, pasX, pasY, size, i):
        # position initiale de la particule
        self.posX = posX
        self.posY = posY

        # direction initiale de la particule
        self.pasX = pasX
        self.pasY = pasY

        self.size = size

        self.id = i

        self.canvas = canvas
        self.circle = canvas.create_oval([(posX * self.size), (posY * self.size), (posX * self.size) + self.size, (posY * self.size) + self.size], outline="grey", fill="grey")

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
        newPosX = self.posX + (self.pasX) # nouveau posX
        newPosY = self.posY + (self.pasY) # nouveau posY

        env.setAgent(self, newPosX, newPosY)
        self.canvas.coords(self.circle, (self.posX * self.size), (self.posY * self.size), (self.posX * self.size) + self.size, (self.posY * self.size) + self.size)

    def describe(self):
        print("Agent;")

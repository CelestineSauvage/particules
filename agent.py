#coding: utf-8

"""
Contient les caractéristiques des particules et une méthode decide(), destinée à coder le processus de décision de ces particules
"""
class Agent:

    def __init__(self, posX, posY, pasX, pasY, size, i):
        # position initiale de la particule
        self.posX = posX
        self.posY = posY

        # direction initiale de la particule
        self.pasX = pasX
        self.pasY = pasY

        self.size = size

        self.color = "grey"

        self.change = 0

        # self.canvas = canvas
        # self.circle = canvas.create_oval([(posX * self.size)+posX, (posY * self.size)+ posY, (posX * self.size) + self.size + posX, (posY * self.size) + self.size + posY], outline="grey", fill="grey")

    def swap_pas(self, agent):
        """
        Swap la direction de 2 agents
        """
        agent.pasX, agent.pasY, self.pasX, self.pasY = self.pasX, self.pasY, agent.pasX, agent.pasY
        self.color = "red"
        agent.color = "red"

        self.change = 1
        # self.canvas.itemconfig(self.circle, outline="red", fill="red")
        # agent.canvas.itemconfig(agent.circle, outline="red", fill="red")

    def decide(self, env):
        """
        Méthode qui permet à un agent de décider de son comportement
        """
        self.change = 0
        newPosX = self.posX + (self.pasX) # nouveau posX
        newPosY = self.posY + (self.pasY) # nouveau posY

        env.setAgent(self, newPosX, newPosY)
        # self.canvas.coords(self.circle, (self.posX * self.size)+self.posX, (self.posY * self.size)+ self.posY, (self.posX * self.size) + self.size+self.posX, (self.posY * self.size) + self.size+ self.posY)


    def describe(self):
        """
        Décrit la position de l'agent
        """
        print("Agent;"+str(self.posX)+","+str(self.posY))

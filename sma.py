#coding: utf-8
from env import Env
from tkinter import *
import random
import time

"""
Contient la méthode run() qui effectue le tour de parole
"""
class SMA:

    def __init__(self, n, l, h, t, size):
        newl = (l-1)*size
        newh = (h-1)*size
        self.window = Tk()
        self.window.geometry(str(newl)+"x"+str(newh))

        self.canvas = Canvas(self.window, height=newl, width=newh)
        self.canvas.grid(row=1, column=1, sticky='w')

        self.env = Env(n, l, h, t, size) #env
        self.n = n
        self.l_agents = (self.env).generate(self.canvas, n) # liste des agents

    def shuffle(self):
        """
        Mélange la liste d'ordre
        """
        random.shuffle(self.l_agents)

    def turn(self):
        """
        Déroulement d'un tour
        """
        self.shuffle()
        for agent in (self.l_agents):
            agent.decide(self.env)
        self.window.after(self.time, self.turn)

    def run(self):
        i = 0
        self.time = 5
        self.turn()
        self.window.mainloop()

if __name__ == "__main__":
    # execute only if run as a script
    game = SMA(1000, 500, 500, False, 2)
    game.run()

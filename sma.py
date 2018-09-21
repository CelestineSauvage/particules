#coding: utf-8
from env import Env
from tkinter import *
import random
import time

"""
Contient la méthode run() qui effectue le tour de parole
"""
class SMA:

    def __init__(self, n, l, h, t):
        self.window = Tk()
        self.window.geometry("1000x1000")

        self.canvas = Canvas(self.window, height=1000, width=1000)
        self.canvas.grid(row=1, column=1, sticky='w')

        self.env = Env(n, 1000, 1000, t) #env
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
            self.window.after(500, self.turn)

    def run(self):
        i = 0
        self.turn()
        self.window.mainloop()

if __name__ == "__main__":
    # execute only if run as a script
    game = SMA(1, 100, 100, False)
    game.run()

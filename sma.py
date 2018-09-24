#coding: utf-8
from env import Env
from tkinter import *
import random
import time
import json
from pprint import pprint

"""
Contient la méthode run() qui effectue le tour de parole
"""
class SMA:

    def __init__(self, n, l, h, t, size, seed, limite, refresh, delay, refresh):
        newl = (l)*size
        newh = (h)*size

        #vue
        self.window = Tk()
        self.window.geometry(str(newl)+"x"+str(newh))

        #canvas
        self.canvas = Canvas(self.window, height=newl, width=newh)
        self.canvas.grid(row=1, column=1, sticky='w')

        #env
        self.env = Env(n, l, h, t, size, seed)

        #n
        self.n = n

        #liste des agents
        self.l_agents = (self.env).generate(self.canvas, n) # liste des agents

        #nb de tours
        self.turn = 0
        self.limite = limite

        #refresh
        self.refresh

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
        self.time = 50
        self.turn()
        self.window.mainloop()

def parse():
    """
    Parse le fichier JSON de config
    """
    with open('Properties.json') as data_file:
        data = json.load(data_file)
        return data

def main():
    data = parse()

    # set des valeurs par défault
    n = 10
    l = 100
    h = 100
    t = False
    size = 10
    seed = -1
    limite = -1
    refresh = 1

    # parcours des options saisis par l'utilisateur
    try :
        if (data["torus"]):
            t = True
        if (data["gridSizeX"]):
            l = int(data["gridSizeX"])
        if (data["gridSizeY"]):
            h = int(data["gridSizeY"])
        if (data["boxSize"]):
            size = data["boxSize"]
        if (data["delay"]):
            delay = True
        if (data["scheduling"]):
            data = int(data["scheduling"])
        if (data["trace"]):
            data = True
        if (data["seed"]):
            seed = int(data["seed"])
        if (data["refresh"]):
            refresh = int(data["refresh"])
        if (data["nbParticles"]):
            n = int(data["nbParticles"])

        game = SMA(n, l, h, t, size, seed, limite, refresh, delay, refresh)
        game.run()

    except :
        print("Tu chies dans la colle quelque part Célestine")


      # "torus":"True",
      # "gridSizeX":"100",
      # "gridSizeY":"100",
      # "canvasSizeX":"100",
      # "canvasSizeY":"100",
      # "boxSize":"10",
      # "delay":"True",
      # "scheduling":"1",
      # "trace":"True",
      # "seed":"0",
      # "refresh":"1",
      # "nbParticles":"30"

if __name__ == "__main__":
    # execute only if run as a script
    main()

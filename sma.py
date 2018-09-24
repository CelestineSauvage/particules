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

    def __init__(self, n, l, h, t, size, seed, limite, refresh, delay, speed, action, trace):
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
        self.nturn = 0
        self.limite = limite

        #refresh
        self.refresh = refresh

        #delay
        self.delay = delay

        # time
        self.time = speed

        # scheduling
        self.action = action

        self.trace = trace

        self.order = range(n)

        # random
        if (seed != -1):
            random.seed(seed)

    def scheduling(self):
        """
        Mélange la liste d'ordre
        """
        if (self.action == 2):
            self.order = random.sample(range(self.n), k=self.n)
        if (self.action == 3):
            self.order = [random.randint(0,self.n-1) for _ in range(self.n)]

    def turn(self):
        """
        Déroulement d'un tour
        """
        if (self.nturn == self.limite): # nb de tours < limite ?
            exit()

        self.nturn+=1 # on incrémente le nombre de tour
        self.scheduling() #quelle méthode pour donner la parole ?
        for i in range(0,self.refresh): # taux de refresh de la page
            for ag in self.order:
                self.l_agents[ag].decide(self.env)
                if (self.trace):
                    self.l_agents[ag].describe()

        if (self.delay):
            self.time+= 1
        if (self.trace):
            print("Turn;"+str(self.nturn))
        self.window.after(self.time, self.turn)

    def run(self):
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
    action = 2
    limite = -1
    refresh = 1
    delay = False
    speed = 20
    trace = False

    # parcours des options saisis par l'utilisateur
    if (data["torus"]):
        t = True
    if (data["gridSizeX"]):
        l = int(data["gridSizeX"])
    if (data["gridSizeY"]):
        print("pour")
        h = int(data["gridSizeY"])
    if (data["boxSize"]):
        print("pour")
        size = int(data["boxSize"])
    if (data["delay"]):
        delay = True
    if (data["scheduling"]):
        action = int(data["scheduling"])
    if (data["trace"]):
        trace = True
    if (data["seed"]):
        seed = int(data["seed"])
    if (data["refresh"]):
        refresh = int(data["refresh"])
    if (data["nbParticles"]):
        n = int(data["nbParticles"])
    if (data["speed"]):
        speed = int(data["speed"])

    game = SMA(n, l, h, t, size, seed, limite, refresh, delay, speed, action, trace)
    game.run()

    # except :
    #     print("Tu chies dans la colle quelque part Célestine ")


if __name__ == "__main__":
    # execute only if run as a script
    main()

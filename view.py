from tkinter import *

class View :

    def __init__(self, l, h, size, l_agents, grid):
        self.w = l*(size+1)
        self.h = h*(size+1)
        self.size = size

        #vue
        self.window = Tk()
        self.window.geometry(str(self.w)+"x"+str(self.h))

        #canvas
        self.canvas = Canvas(self.window, height=self.h, width=self.w)
        self.canvas.grid(row=1, column=1, sticky='w')

        if (grid):
            self.create_grid()
        self.init_agents(l_agents)


    def create_grid(self, event=None):
        """
        Crée les lignes de la grille
        """
        # self.canvas.delete('grid_line') # Will only remove the grid_line

        # Creates all vertical lines at intevals of 100
        for i in range(0, self.w, self.size+1):
            self.canvas.create_line([(i, 0), (i, self.h)], tag='grid_line')

        # Creates all horizontal lines at intevals of 100
        for i in range(0, self.h, self.size+1):
            self.canvas.create_line([(0, i), (self.w, i)], tag='grid_line')

    def init_agents(self, l_agents):
        """
        Initialise les ronds des agents
        """
        for ag in l_agents:
            x = ag.posX
            y = ag.posY
            color = ag.color
            ag.circle = self.canvas.create_oval([(x * self.size)+x,
                                                (y * self.size)+ y,
                                                (x * self.size) + self.size + x,
                                                (y * self.size) + self.size + y],
                                                outline=color, fill=color)

    def set_agent(self, time, l_agents, fct):
        """
        Bouge les ronds des agents
        """
        for ag in l_agents:
            x = ag.posX
            y = ag.posY
            color = ag.color
            self.canvas.itemconfig(ag.circle, outline=color, fill=color)
            self.canvas.coords(ag.circle, (x * self.size)+x,
                                            (y * self.size)+ y,
                                            (x * self.size) + self.size + x,
                                            (y * self.size) + self.size + y)
        self.window.after(time, fct)

    def mainloop(self):
        self.window.mainloop()

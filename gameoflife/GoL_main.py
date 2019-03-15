"""
Minakov Nikita Csse1709r Venik.Team
Almaty 2019
SDP 4
"""

import numpy as np
import random

class Grid(object):

    def __init__(self):
        self.current_grid = np.zeros((150,150))
        self.section_tobe_evaluated = 0
        self.size = 2
        self.pattern = 'clear'
        self.position = 0
        self.position2 = 0
        self.past_ticks = []

    def new_pattern(self, pattern):
        self.position2 = 0
        current_grid = np.zeros((150, 150))
        if pattern == 'Random':
            rand_sect1 = random.randint(0, 5)
            rand_sect2 = random.randint(6, 100)
            sect = current_grid[rand_sect1:rand_sect2, rand_sect1:rand_sect2]
            for y in range(len(sect)):
                for x in range(len(sect)):
                    sect[y][x] = random.choice([1, 0])
            self.current_grid = current_grid[rand_sect1:rand_sect2, rand_sect1:rand_sect2]
        elif pattern == 'Remove':
            self.current_grid = current_grid
        else:
            return
        self.pattern = pattern

    def start_over(self):
        self.position2 = 0
        self.new_pattern(self.pattern)

    def tick(self):
        self.expand()
        next_grid = np.zeros((self.size+ self.position, self.size+self.position))
        current_grid = self.current_grid.tolist() # not using numpy functions because slows process down
        for i in range(self.section_tobe_evaluated[2]-2, self.section_tobe_evaluated[3]+2):
            for i2 in range(self.section_tobe_evaluated[0]-2,self.section_tobe_evaluated[1]+2):
                neighbors = 0
                try:
                    current_state = current_grid[i][i2] # Can be either 1 or 0
                except IndexError:
                    current_state = 0
                try:
                    neighbors += current_grid[i + -1][i2 + -1]
                    neighbors += current_grid[i + -1][i2 + 0]
                    neighbors += current_grid[i + -1][i2 + 1]
                    neighbors += current_grid[i + 0][i2 + -1]
                    neighbors += current_grid[i + 0][i2 + 1]
                    neighbors += current_grid[i + 1][i2 + -1]
                    neighbors += current_grid[i + 1][i2 + 0]
                    neighbors += current_grid[i + 1][i2 + 1]
                except IndexError:
                   continue

                next_grid[i+self.position][i2+self.position] = 1 if current_state and (neighbors == 2 or neighbors == 3) else (1 if neighbors == 3 else 0)
        self.current_grid = next_grid

        self.past_ticks.append(self.live_cells()) # for tick reverse

    def tick_reverse(self):
        next_grid = np.zeros((self.size, self.size))
        try:
            past_tick_grid = self.past_ticks[-1] # 'coordinates' of active cells of past boards
            for tup in past_tick_grid:
                next_grid[tup[0]][tup[1]] = 1
            del self.past_ticks[-1]
            self.current_grid = next_grid
        except IndexError:
            pass
        if len(self.past_ticks) > 100:
            del self.past_ticks[0]

    def expand(self):
        live = self.live_cells()
        live_x = [x[1] for x in live]
        live_y = [y[0] for y in live]
        try:
            min_x = min(live_x)
            min_y = min(live_y)
            max_x = max(live_x)
            max_y = max(live_y)
            self.position = 1 if min_x == 0 or min_y == 0 else 0
            self.position2 += 1 if min_x == 0 or min_y == 0 else 0
            live_max_overall = max(max_x, max_y) + 3
            self.size = live_max_overall
            self.section_tobe_evaluated = (min_x, max_x + 1, min_y, max_y + 1)
        except ValueError:
            pass

    def live_cells(self):
        living = []
        for y, row in enumerate(self.current_grid):
            for x, cell in enumerate(row):
                if cell:
                    living.append((y, x))
        return living


try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

class Screen(tk.Canvas):
    def __init__(self):
        self.window_side_length = 300
        tk.Canvas.__init__(self, root, height=self.window_side_length, width=self.window_side_length)
        self.board = Grid()
        self.board.new_pattern('Random')
        self.ticks = 0
        self.factors_of_300 = [x for x in range(1, 151) if self.window_side_length%x == 0 and x < 151] # to get equal spacing of the squares on the grid
        self.action_state = 0  # can be only play (1) or pause (0)
        self.separation_length = 0
        self.moving_x = 0
        self.moving_y = 0
        self.slider = None
        self.play_pause = None
        self.patternlist = tk.StringVar()
        self.patternlist.set('Random')

        if self.action_state:
            self.tick()

    def todo(self, *action): # Either continue ticking or tick by user input
        if self.action_state:
            self.action_state = 0
            self.play_pause.config(text='Play')
        else:
            self.action_state = 1 # self.tick() is run in place_squares
            self.play_pause.config(text='Pause')

    def place_squares(self):
        self.delete('all')
        self.create_rectangle(0, 0, self.window_side_length, self.window_side_length, fill='black')

        if self.window_side_length % self.slider.get() != 0:  # To filter number so the scale number is a factor of 300 (To get equilateral squares)
            closest = sorted(self.factors_of_300, key=lambda x: abs(x - self.slider.get()))
            self.separation_length = self.window_side_length / closest[0]

        else:
            self.separation_length = self.window_side_length / self.slider.get()
        m = (self.board.position2 * self.separation_length) - 15 # to spread list to the left and up. The 15 is to give some space to zooming
        x = self.moving_x
        y = self.moving_y-m
        x2 = self.separation_length+self.moving_x
        y2 = self.separation_length+self.moving_y-m
        cube_array = self.board.current_grid # Using the Grid class
        for row in cube_array:
            for block in row:
                if block:
                    self.create_rectangle(x-m, y, x2-m, y2, fill='light green')

                if not block:
                    pass
                x += self.separation_length
                x2 += self.separation_length
            x = self.moving_x
            x2 = self.separation_length+self.moving_x
            y += self.separation_length
            y2 += self.separation_length

        if self.action_state:
            self.tick()
        self.after(10, self.place_squares)

    def tick(self):
        self.ticks += 1
        self.board.tick()

    def reverse_tick(self):
        self.board.tick_reverse()

    def start_over(self):
        self.ticks = 0
        self.board.start_over()

    def home(self):
        self.moving_x = 0
        self.moving_y = 0

        self.slider.set(25)

    def move(self, action):
        if action.keycode == 37:
            self.moving_x += 20
        elif action.keycode == 38:
            self.moving_y += 20
        elif action.keycode == 39:
            self.moving_x -= 20
        elif action.keycode == 40:
            self.moving_y -= 20

    def set_pattern(self):
        self.board.new_pattern(self.patternlist.get())


def main():
    canv = Screen()
    canv.grid(column=2)
    tk.Frame(root, width=100).grid(column=0)
    tk.Button(root, text='<', command=canv.reverse_tick).grid(column=2, row=1, sticky=tk.W)
    play_pause = tk.Button(root, text='Play', command=canv.todo)
    play_pause.grid(column=2, row=1)
    tk.Button(root, text='>', command=canv.tick).grid(column=2, row=1, sticky=tk.E)
    slider = tk.Scale(root, from_=1, to=150, orient=tk.HORIZONTAL)
    slider.grid(column=2)
    slider.set(25)
    options = tk.OptionMenu(root, canv.patternlist, 'Random', 'Remove')
    options.grid(row=3, column=2)
    tk.Button(root, text='Go', command=canv.set_pattern).place(x=290, y=375)
    canv.play_pause = play_pause
    canv.slider = slider
    canv.place_squares()
    tk.Button(root, text='Restart', command=canv.start_over).grid(column=2)
  #  tk.Button(root, text='Home', command=canv.home).grid(column=2)
    root.bind('<Down>', canv.move)
    root.bind('<Left>', canv.move)
    root.bind('<Right>', canv.move)
    root.bind('<Up>', canv.move)
    root.bind('<space>', canv.todo)

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Conway\'s Game of Life by Minakov Nikita')
    root.geometry('500x450')
    main()
    root.mainloop()

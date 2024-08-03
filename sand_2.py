import pygame
import numpy as np
import random
from particles import Particle

class Space:
    def __init__(self, window_x=0, window_y=0):
        pygame.init()
        self.window = pygame.display.set_mode((450, 650))
        pygame.display.set_caption("Sand Simulation")
        self.clock = pygame.time.Clock()

        self.sand_size = 2
        self.rows = self.window.get_width() // self.sand_size
        self.columns = self.window.get_height() // self.sand_size

        self.grid = np.zeros((self.rows, self.columns), dtype=bool)
        self.velocity_grid = np.ones((self.rows, self.columns), dtype=float)
        self.hue_grid = np.zeros((self.rows, self.columns), dtype=float)

        self.obstacles = np.zeros((self.rows, self.columns), dtype=bool)
        self.hue_value = 200
        self.sand_particles = []
        self.make_obstacles()

    def make_obstacles(self):
            
        for i in range(1,9):
            for x in range(self.rows):
                if x%i!=0:
                    self.obstacles[x, 50+(i*20)] = True

    def on_mouse_drag(self, pos):
        x, y = pos
        row = x // self.sand_size
        col = y // self.sand_size
        matrix = 2
        if x >= self.sand_size and x <= self.window.get_width() - self.sand_size and y >= self.sand_size and y <= self.window.get_height() - self.sand_size:
            for i in range(-matrix, matrix + 1):
                for j in range(-matrix, matrix + 1):
                    if 0 <= row - i < self.rows and 0 <= col - j < self.columns:
                        if not self.grid[row - i, col - j] and not self.obstacles[row - i, col - j]:
                            self.grid[row - i, col - j] = True
                            self.velocity_grid[row - i, col - j] = 1
                            self.hue_grid[row - i, col - j] = self.hue_value

            self.hue_value += 0.5
            if self.hue_value > 360:
                self.hue_value = 1

    def fall(self):
        falling = list(zip(*np.where(self.grid)))
        random.shuffle(falling)
        new_grid = self.grid.copy()
        new_velocity_grid = self.velocity_grid.copy()
        new_hue_grid = self.hue_grid.copy()

        for x, y in falling:
            velocity = self.velocity_grid[x, y]
            hue = self.hue_grid[x, y]
            max_fall = int(velocity)
            moved = False
            brk = False
            # print(f"x : {x}, y : {y}")
            for fall_distance in range(max_fall, 0, -1):
                new_y = y + fall_distance  # Always fall down
                if not (0 <= new_y < self.columns):
                    break

                for change_y in range(fall_distance, 0, -1):
                    if (0 <= y + change_y < self.rows and self.obstacles[x, y + change_y] ) :
                        new_y = y + change_y
                        brk = True
                        break

                if 0 <= new_y < self.columns :
                    # Check directly below
                    if not new_grid[x, new_y] and not self.obstacles[x, new_y] and not brk:
                        new_grid[x, y] = False
                        new_grid[x, new_y] = True
                        new_velocity_grid[x, new_y] = velocity + 0.5
                        new_hue_grid[x, new_y] = hue
                        moved = True
                        break

                    # Check diagonally left
                    elif x > 0 and not new_grid[x - 1, new_y] and \
                        not self.obstacles[x - 1, new_y] and random.random() < 0.5:
                        new_grid[x, y] = False
                        new_grid[x - 1, new_y] = True
                        new_velocity_grid[x - 1, new_y] = velocity + 0.5
                        new_hue_grid[x - 1, new_y] = hue
                        moved = True
                        break

                    # Check diagonally right
                    elif x < self.columns - 1 and not new_grid[x + 1, new_y] and \
                        not self.obstacles[x + 1, new_y] and random.random() < 0.5:
                        new_grid[x, y] = False
                        new_grid[x + 1, new_y] = True
                        new_velocity_grid[x + 1, new_y] = velocity + 0.5
                        new_hue_grid[x + 1, new_y] = hue
                        moved = True
                        break

            if not moved:
                new_velocity_grid[x, y] = 1

        self.grid = new_grid
        self.velocity_grid = new_velocity_grid
        self.hue_grid = new_hue_grid

    def update_particles(self):
        falling = np.where(self.grid)
        current_particles = len(self.sand_particles)
        needed_particles = len(falling[0])

        for _ in range(needed_particles - current_particles):
            self.sand_particles.append(Particle(0, 0, self.sand_size, self.hue_value))

        for i, (x, y) in enumerate(zip(falling[0], falling[1])):
            if i < len(self.sand_particles):
                self.sand_particles[i].x = x
                self.sand_particles[i].y = y
                self.sand_particles[i].hue_value = self.hue_grid[x, y]
                self.sand_particles[i].show_sand(self.window)

        for i in range(needed_particles, current_particles):
            if i < len(self.sand_particles):
                self.sand_particles.pop()

    def update(self):
        self.fall()
        self.update_particles()

    def draw_obstacles(self):
        for x in range(self.rows):
            for y in range(self.columns):
                if self.obstacles[x, y]:
                    pygame.draw.rect(self.window, (255, 0, 0), (x * self.sand_size, y * self.sand_size, self.sand_size, self.sand_size))

    def run(self):
        running = True
        while running:
            self.window.fill((0, 0, 0))
            self.update()
            self.draw_obstacles()
            pygame.display.flip()
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEMOTION:
                    if event.buttons[0]:
                        self.on_mouse_drag(event.pos)

        pygame.quit()

space = Space()
space.run()

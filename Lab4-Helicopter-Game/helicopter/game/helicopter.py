"""
Helicopter: the player-controlled vehicle. Moves vertically based on
held Up/Down keys.
"""

import pygame

THRUST = 0.4
DAMPING = 0.92
MAX_SPEED = 8.0


class Helicopter:
    def __init__(self, x, y, width=40, height=24):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vy = 0.0
        self.has_shield = True  # Helicopter starts with 1 shield charge

    def handle_input(self, keys_pressed):
        if keys_pressed[pygame.K_UP]:
            self.vy -= THRUST
        if keys_pressed[pygame.K_DOWN]:
            self.vy += THRUST

    def update(self, height_bound):
        self.vy *= DAMPING
        self.vy = max(-MAX_SPEED, min(MAX_SPEED, self.vy))

        self.y += self.vy

        min_y = self.height / 2
        if self.y < min_y:
            self.y = min_y
            self.vy = 0.0

        max_y = height_bound - (self.height / 2)
        if self.y > max_y:
            self.y = max_y
            self.vy = 0.0

    def get_rect(self):
        return pygame.Rect(
            int(self.x - self.width / 2),
            int(self.y - self.height / 2),
            self.width,
            self.height,
        )
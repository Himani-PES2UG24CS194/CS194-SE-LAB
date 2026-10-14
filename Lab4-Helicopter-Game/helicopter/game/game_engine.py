"""
GameEngine: owns the helicopter and all obstacles, manages scoring and state.
"""

import random
import pygame

from game.helicopter import Helicopter
from game.obstacle import Obstacle
from game.renderer import WIDTH, HEIGHT

SPAWN_INTERVAL_FRAMES = 90
GAP_HEIGHT = 150
WALL_WIDTH = 60
SCROLL_SPEED = 3


class GameEngine:
    def __init__(self):
        self.reset()

    def reset(self):
        """Reset all game variables to start a fresh game."""
        self.helicopter = Helicopter(x=100, y=HEIGHT / 2)
        self.obstacles = []
        self.frames_until_spawn = 0
        self.game_over = False
        self.score = 0

    def _spawn_obstacle(self):
        margin = 60
        gap_y = random.randint(margin + GAP_HEIGHT // 2, HEIGHT - margin - GAP_HEIGHT // 2)
        self.obstacles.append(Obstacle(
            x=WIDTH, gap_y=gap_y, gap_height=GAP_HEIGHT,
            wall_width=WALL_WIDTH, screen_height=HEIGHT, speed=SCROLL_SPEED,
        ))

    def handle_input(self, keys_pressed):
        if not self.game_over:
            self.helicopter.handle_input(keys_pressed)

    def handle_keydown(self, key):
        if key == pygame.K_r:
            self.reset()

    def check_collisions(self):
        heli_rect = self.helicopter.get_rect()
        for obstacle in list(self.obstacles):
            top_rect = obstacle.get_top_rect()
            bottom_rect = obstacle.get_bottom_rect()
            
            if heli_rect.colliderect(top_rect) or heli_rect.colliderect(bottom_rect):
                if self.helicopter.has_shield:
                    # Shield absorbs the hit!
                    self.helicopter.has_shield = False
                    self.obstacles.remove(obstacle)
                else:
                    self.game_over = True
                break

    def update(self):
        if self.game_over:
            return

        self.helicopter.update(HEIGHT)

        self.frames_until_spawn -= 1
        if self.frames_until_spawn <= 0:
            self._spawn_obstacle()
            self.frames_until_spawn = SPAWN_INTERVAL_FRAMES

        for obstacle in self.obstacles:
            obstacle.update()
            
            if not obstacle.scored and obstacle.x + obstacle.wall_width < self.helicopter.x:
                obstacle.scored = True
                self.score += 1

        self.obstacles = [o for o in self.obstacles if not o.is_off_screen()]

        self.check_collisions()

    def draw(self, surface, font):
        from game import renderer
        renderer.draw_scene(surface, self.helicopter, self.obstacles)
        
        # Display HUD Info
        shield_status = "READY" if self.helicopter.has_shield else "DEPLETED"
        renderer.draw_text(surface, font, f"Score: {self.score} | Shield: {shield_status}", (10, 10))

        if self.game_over:
            renderer.draw_banner(surface, font, "GAME OVER - Press R to Restart")
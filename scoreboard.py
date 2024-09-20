import os
import pygame
from constants import *

class Scoreboard:
    def __init__(self, font_path, font_size, screen, initial_score=0):
        self.screen = screen
        self.score = initial_score
        self.font = pygame.font.Font(font_path, font_size)
        self.color = (255, 255, 255)  # White color for text

    def update_score(self, points):
        """Updates the score by adding points."""
        self.score += points

    def reset_score(self):
        """Resets the score to zero."""
        self.score = 0

    def render(self):
        """Renders the score text centered at the top of the screen."""
        score_text = f"Score: {self.score}"
        text_surface = self.font.render(score_text, True, self.color)
        text_rect = text_surface.get_rect()
        text_rect.center = (self.screen.get_width() // 2, 50)  # Center horizontally, Y = 50 pixels

        # Blit the text to the screen
        self.screen.blit(text_surface, text_rect)    
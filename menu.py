import pygame
import time
import pygame_menu
from pygame_menu import themes
class Menu(pygame_menu.Menu):
    def __init__(self,root,theme=themes.THEME_SOLARIZED):
        super().__init__(pygame.display.get_caption()[0],root.get_width(),root.get_height(),theme=theme)
        self.root = root
        self.run = False
        self.active = None
    def flip(self,events):
        if self.is_enabled():
            self.run = True
            self.update(events)
            self.active = False
        if self.is_enabled():
            self.run = False
            self.draw(self.root)
            self.active = True

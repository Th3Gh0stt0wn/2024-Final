# Decay of Angels role
#pygame.draw.rect(screen, (163, 73, 46), (900, 10, 200, 150))
import pygame, sys
pygame.init()
screen = pygame.display.set_mode((1110, 800))

state = "menu"

white=(255,255,255)
bold = pygame.font.Font.bold
font = pygame.font.SysFont("inkfree", 24, bold)

class Angels:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        
    def draw(self):
        if state == "menu":
            pygame.draw.rect(screen, (152, 98, 181), (self.xpos, self.ypos, 200, 150))
            title = font.render("Decay of Angels", True, white)
            screen.blit(title,(self.xpos+15, self.ypos+155))
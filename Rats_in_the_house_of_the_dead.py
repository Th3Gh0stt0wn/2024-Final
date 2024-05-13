import pygame, sys
pygame.init()
screen = pygame.display.set_mode((1110, 800))

state = "menu"

white=(255,255,255)
bold = pygame.font.Font.bold
font = pygame.font.SysFont("inkfree", 24, bold)

class Rats:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        
    def draw(self):
        if state == "menu":
            pygame.draw.rect(screen, (173, 173, 173), (self.xpos, self.ypos, 200, 150))
            title = font.render("Rats in the", True, white)
            title2 = font.render("House of the Dead", True, white)
            screen.blit(title,(self.xpos+30, self.ypos+155))
            screen.blit(title2,(self.xpos+5, self.ypos+175))
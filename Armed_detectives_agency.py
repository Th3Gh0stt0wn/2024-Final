import pygame, sys
pygame.init()
screen = pygame.display.set_mode((1110, 800))

state = "menu"

white=(255,255,255)
bold = pygame.font.Font.bold
font = pygame.font.SysFont("inkfree", 24, bold)

class detective:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        
    def draw(self):
        if state == "menu":
            pygame.draw.rect(screen, (138, 255, 226), (self.xpos, self.ypos, 200, 150))
            begin = font.render("Armed Detective Agency", True, white)
            screen.blit(begin,(self.xpos-20,self.ypos+155))
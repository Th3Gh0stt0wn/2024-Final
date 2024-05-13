# Police role
        #pygame.draw.rect(screen, (35, 49, 158), (600, 600, 200, 150))
import pygame, sys
pygame.init()
screen = pygame.display.set_mode((1110, 800))

state = "menu"

white=(255,255,255)
bold = pygame.font.Font.bold
font = pygame.font.SysFont("inkfree", 24, bold)

class police:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        
    def draw(self):
        if state == "menu":
            pygame.draw.rect(screen, (87, 143, 173), (self.xpos, self.ypos, 200, 150))
            begin = font.render("Police", True, white)
            screen.blit(begin,(self.xpos+70,self.ypos+155))
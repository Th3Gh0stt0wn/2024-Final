import pygame, sys
pygame.init()
screen = pygame.display.set_mode((1110, 800))

state = "menu"

white=(255,255,255)
bold = pygame.font.Font.bold
font = pygame.font.SysFont("inkfree", 24, bold)

class Division:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        
    def draw(self):
        if state == "menu":
            pygame.draw.rect(screen, (158, 35, 101), (self.xpos, self.ypos, 200, 150))
            title = font.render("Special division", True, white)
            title2 = font.render("for unusal powers", True, white)
            screen.blit(title,(self.xpos+30, self.ypos+155))
            screen.blit(title2,(self.xpos+20, self.ypos+175))

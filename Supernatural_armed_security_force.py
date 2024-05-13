import pygame, sys
pygame.init()
screen = pygame.display.set_mode((1110, 800))

state = "menu"

white=(255,255,255)
bold = pygame.font.Font.bold
font = pygame.font.SysFont("inkfree", 24, bold)

class Security:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        
    def draw(self):
        if state == "menu":
            pygame.draw.rect(screen, (196, 81, 138), (self.xpos, self.ypos, 200, 150))
            title = font.render("Supernatural Armed", True, white)
            title2 = font.render("Security Force", True, white)
            screen.blit(title,(self.xpos+5, self.ypos+155))
            screen.blit(title2,(self.xpos+30, self.ypos+175))
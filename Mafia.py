import pygame, sys
pygame.init()
screen = pygame.display.set_mode((1110, 800))
clock = pygame.time.Clock()
gameover = False
state = "menu"

xpos = 0
ypos = 0
mousePos = (xpos, ypos)
mouseDown = False

white=(255,255,255)
bold = pygame.font.Font.bold
font = pygame.font.SysFont("inkfree", 24, bold)

class PM_file:
    def __init__(self, xpos: int, ypos: int, name: str, color: tuple[int, int, int]):
        self.xpos = xpos
        self.ypos = ypos
        self.name = name
        self.color = color

    def draw(self):
        if state == "menu":
            pygame.draw.rect(screen, self.color, (self.xpos, self.ypos, 200, 150))
            begin = font.render(self.name, True, white)
            screen.blit(begin,(self.xpos +70, self.ypos +160))

class Mori(PM_file):        
    def __init__(self, xpos: int, ypos: int):
        super().__init__(xpos, ypos, "Ogai Mori", (161,145,188))

class Ace(PM_file):        
    def __init__(self, xpos: int, ypos: int):
        super().__init__(xpos, ypos, "Ace", (161,145,188))

class Chuuya(PM_file):        
    def __init__(self, xpos: int, ypos: int):
        super().__init__(xpos, ypos, "Chuuya Nakahara", (161,145,188))

class Koyo(PM_file):        
    def __init__(self, xpos: int, ypos: int):
        super().__init__(xpos, ypos, "Koyo Ozaki", (161,145,188))

class Ryunosuke(PM_file):        
    def __init__(self, xpos: int, ypos: int):
        super().__init__(xpos, ypos, "Ryunosuke Akutagawa", (161,145,188))

class Gin(PM_file):        
    def __init__(self, xpos: int, ypos: int):
        super().__init__(xpos, ypos, "Gin Akutagawa", (161,145,188))

class Ichiyo(PM_file):        
    def __init__(self, xpos: int, ypos: int):
        super().__init__(xpos, ypos, "Ichiyo", (161,145,188))

class Ryuro(PM_file):        
    def __init__(self, xpos: int, ypos: int):
        super().__init__(xpos, ypos, "Ryuro Hirotsu", (161,145,188))

class Michizo(PM_file):        
    def __init__(self, xpos: int, ypos: int):
        super().__init__(xpos, ypos, "Michizo Tachihara", (161,145,188))

class Elise(PM_file):        
    def __init__(self, xpos: int, ypos: int):
        super().__init__(xpos, ypos, "Elise", (161,145,188))

class Motojiro(PM_file):        
    def __init__(self, xpos: int, ypos: int):
        super().__init__(xpos, ypos, "Motojiro Kajii", (161,145,188))

class Arthur(PM_file):        
    def __init__(self, xpos: int, ypos: int):
        super().__init__(xpos, ypos, "Arther Rimbaud", (161,145,188))
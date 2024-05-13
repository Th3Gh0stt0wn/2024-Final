import pygame, sys

#Main files
from Armed_detectives_agency import detective#1
from begin import Begin#2
from Citizen import citizen#3
from Credits import woowo#4
from Decay_of_angels import Angels#5
from Hunting_dogs import Dogs#6
from Police import police#7
from Port_Mafia import mafia#8
from Rats_in_the_house_of_the_dead import Rats#9
from Special_divison_for_unusal_powers import Division#10
from Supernatural_armed_security_force import Security#11
from The_guild import Guild#12
from quit import leave#Quit button

#Files
from Agency import ADA_file#1
from HDogs import Hunting_dogs_file#2
from Mafia import PM_file#3
from Decay import Decay_file#4

#Characters
from Agency import Fukuzawa#1
from HDogs import Fukuchi#2
from Mafia import Mori#3
from Decay import Fyodor#4

#Nessicary
pygame.display.set_caption("Bungo Stray Dogs")
screen = pygame.display.set_mode((1110, 800))
clock = pygame.time.Clock()
gameover = False

#mouse input
xpos = 0
ypos = 0
mousePos = (xpos, ypos)
mouseDown = False
#Text inputs

white=(255,255,255)
bold = pygame.font.Font.bold
font = pygame.font.SysFont("inkfree", 24, bold)
#game state variable

state = "menu"
start = False
button1 = False #go back to menu
quitGame = False #quit the game
ADA = False
Port_Mafia = False
Leave = False
Hunting_Dogs = False
Decay_of_the_Angel = False 
The_Guild = False
Rats_in_the_House_of_the_Dead = False
Supernatural_armed_security_force = False
Special_division_for_unusal_powers = False
Police = False
Citizen = False
Credits = False

#Main files
beginning = Begin(10,10)
port = mafia(300, 10)
agency = detective(600,10)

dog = Dogs (10,200) 
angel = Angels (300, 200)
guild = Guild(600, 200)

rats = Rats(10, 400)
division = Division(300, 400)
security = Security(600, 400)

cops = police (10,600)
player = citizen(300,600)
credit = woowo (600, 600)

Quit = leave (900, 10)

#Files
file1 = PM_file
file2 = ADA_file
file3 = Hunting_dogs_file
file4 = Decay_file

#Characters
mori = Mori(10,10)#1
fukuzawa = Fukuzawa(10,10)#2
fukuchi = Fukuchi(10,10)#3
fyodor = Fyodor(10,10)#4

#Game loop
while not gameover:
    clock.tick(60)
    
    #input section
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = False
        #keeps track of mouse position
        if event.type == pygame.MOUSEMOTION:
            mousePos = event.pos
        #keeps track of mouse button
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseDown = True
        if event.type == pygame.MOUSEBUTTONUP:
            mouseDown = False
        
    #physics section
    #print(mousePos)#uncomment for testing
    
    #state 1: menu state!------------------------------
    if state == "menu": 
        #begin
        if mousePos[0]>10 and mousePos[0]<210 and mousePos[1]>10 and mousePos[1]<160:
            start = True
        else:
            start = False

        #mafia
        if mousePos[0]>300 and mousePos[0]<500 and mousePos[1]>10 and mousePos[1]<160:
            Port_Mafia = True
        else:
            Port_Mafia = False

        #agency
        if mousePos[0]>600 and mousePos[0]<800 and mousePos[1]>10 and mousePos[1]<160:
            ADA = True
        else:
            ADA = False

        #hunting dogs
        if mousePos[0]>10 and mousePos[0]<210 and mousePos[1]>200 and mousePos[1]<350:
            Hunting_Dogs = True
        else:
            Hunting_Dogs = False

        #Decay
        if mousePos[0]>300 and mousePos[0]<500 and mousePos[1]>200 and mousePos[1]<350:
            Decay_of_the_Angel = True
        else: 
            Decay_of_the_Angel = False

        if mousePos[0]>600 and mousePos[0]<800 and mousePos[1]>200 and mousePos[1]<350:
            The_Guild = True
        else:
            The_Guild = False

        if mousePos[0]>10 and mousePos[0]<210 and mousePos[1]>400 and mousePos[1]<550:
            Rats_in_the_House_of_the_Dead = True
        else:
            Rats_in_the_House_of_the_Dead = False

        if mousePos[0]>300 and mousePos[0]<500 and mousePos[1]>400 and mousePos[1]<550:
            Supernatural_armed_security_force = True
        else:
            Supernatural_armed_security_force = False

        if mousePos[0]>600 and mousePos[0]<800 and mousePos[1]>400 and mousePos[1]<550:
            Special_division_for_unusal_powers = True
        else:
            Special_division_for_unusal_powers = False
            
        if mousePos[0]>10 and mousePos[0]<210 and mousePos[1]>600 and mousePos[1]<750:
            Police = True
        else:
            Police = False
            
        if mousePos[0]>300 and mousePos[0]<500 and mousePos[1]>600 and mousePos[1]<750:
            Citizen = True
        else:
            Citizen = False

        if mousePos[0]>600 and mousePos[0]<800 and mousePos[1]>600 and mousePos[1]<750:
            Credits = True
        else:
            Credits = False

        if mousePos[0]>900 and mousePos[0]<1100 and mousePos[1]>10 and mousePos[1]<160:
            Leave = True
        else:
            Leave = False

        #begin
        if start == True and mouseDown == True:
            print("You have chosen to start the game")
            state = "playing"

        #mafia
        elif Port_Mafia == True and mouseDown == True:
            print("You have selected the Port Mafia role")
            state = "Mafia"

        #agency
        elif ADA == True and mouseDown == True:
            print("You have selected the Armed detective agency role")
            state = "Agency"

        #hunting Dogs
        elif Hunting_Dogs == True and mouseDown == True:
            print("You have selected the Hunting dogs role")
            state = "Hunting Dogs"

        #Decay of the Angel
        elif Decay_of_the_Angel == True and mouseDown == True:
            print("You have selected the Decay of the Angel role")
            state = "Decay of the Angel"

        elif The_Guild == True and mouseDown == True:
            print("You have selected The Guild role")
            state = "The Guild"

        elif Rats_in_the_House_of_the_Dead == True and mouseDown == True:
            print("You have selected the Rats in the House of the Dead role")
            state = "Rats in the House of the Dead"
        
        elif Supernatural_armed_security_force == True and mouseDown == True:
            print("You have selected the Supernatural armed security force role")
            state = "Supernatural armed security force"

        elif Special_division_for_unusal_powers == True and mouseDown == True:
            print("You have selected the Special division for unusal powers role")
            state = "Special division for unusal powers"
        
        elif Police == True and mouseDown == True:
            print("You have selected the police role")
            state = "Police"
        
        elif Citizen == True and mouseDown == True:
            print("You have selected the citizen role")
            state = "citizen"

        elif Credits == True and mouseDown == True:
            print("You have selected credits")
            state = "Credits"
        
        elif Leave == True and mouseDown == True:
            print("You have selected to quit")
            state = "Quit"

    #state 2: playing state!---------------------------
    elif state == "playing":
        if quitGame == True: #pressing quit takes you back to menu
            state = "menu"
        elif mousePos[0]>100 and mousePos[0]<200 and mousePos[1]>500 and mousePos[1]<600:
            button1 = True
        else:
            button1 = False

        if state == "playing" and button1 == True and mouseDown == True:
            state = "menu"
            
    elif state == "credits":
        if quitGame == True: #pressing quit takes you back to menu
            state = "menu"

    elif state == "Mafia":
        if quitGame == True: #pressing quit takes you back to menu
          state = "menu"
        elif mousePos[0]>100 and mousePos[0]<200 and mousePos[1]>500 and mousePos[1]<600:
            button1 = True
        else:
            button1 = False

    elif state == "Agency":
        if quitGame == True: #pressing quit takes you back to menu
            state = "menu"
        elif mousePos[0]>100 and mousePos[0]<200 and mousePos[1]>500 and mousePos[1]<600:
            button1 = True
        else:
            button1 = False

    elif state == "Hunting Dogs":
        if quitGame == True: #pressing quit takes you back to menu
            state = "menu"
        elif mousePos[0]>100 and mousePos[0]<200 and mousePos[1]>500 and mousePos[1]<600:
            button1 = True
        else:
            button1 = False

    elif state == "Decay of the Angel":
        if quitGame == True: #pressing quit takes you back to menu
            state = "menu"
        elif mousePos[0]>100 and mousePos[0]<200 and mousePos[1]>500 and mousePos[1]<600:
            button1 = True
        else:
            button1 = False

    elif state == "The Guild":
        if quitGame == True: #pressing quit takes you back to menu
            state = "menu"
        elif mousePos[0]>100 and mousePos[0]<200 and mousePos[1]>500 and mousePos[1]<600:
            button1 = True
        else:
            button1 = False

    elif state == "Rats in the House of the Dead":
        if quitGame == True: #pressing quit takes you back to menu
            state = "menu"
        elif mousePos[0]>100 and mousePos[0]<200 and mousePos[1]>500 and mousePos[1]<600:
            button1 = True
        else:
            button1 = False
        
    elif state == "Supernatural armed security force":
        if quitGame == True: #pressing quit takes you back to menu
            state = "menu"
        elif mousePos[0]>100 and mousePos[0]<200 and mousePos[1]>500 and mousePos[1]<600:
            button1 = True
        else:
            button1 = False
            
    elif state == "Special division for unusal powers":
        if quitGame == True: #pressing quit takes you back to menu
            state = "menu"
        elif mousePos[0]>100 and mousePos[0]<200 and mousePos[1]>500 and mousePos[1]<600:
            button1 = True
        else:
            button1 = False

    elif state == "Police":
        if quitGame == True: #pressing quit takes you back to menu
            state = "menu"
        elif mousePos[0]>100 and mousePos[0]<200 and mousePos[1]>500 and mousePos[1]<600:
            button1 = True
        else:
            button1 = False
        
    elif state == "citizen":
        if quitGame == True: #pressing quit takes you back to menu
            state = "menu"
        elif mousePos[0]>100 and mousePos[0]<200 and mousePos[1]>500 and mousePos[1]<600:
            button1 = True
        else:
            button1 = False
            
    elif state == "Credits":
        if quitGame == True: #pressing quit takes you back to menu
            state = "menu"
        elif mousePos[0]>100 and mousePos[0]<200 and mousePos[1]>500 and mousePos[1]<600:
            button1 = True
        else:
            button1 = False

    elif state == "Quit":
        print("aaaaa")
        pygame.quit()
        quit()


    #render section
    screen.fill((0,0,0))
    
    #menu state-------------------------------
    if state == "menu":
        #Clear the screen
        screen.fill((0,0,0))
        #Top row
        beginning.draw()
        port.draw()
        agency.draw()
        dog.draw()
        #Middle row
        angel.draw()
        guild.draw()
        rats.draw()
        division.draw()
        #Last row
        security.draw()
        cops.draw()
        player.draw()
        credit.draw()

        Quit.draw()
    
    #game state-------------------------------
    elif state == "playing":
        screen.fill((0,0,0))# Clear the screen green
        pygame.draw.rect(screen, (255, 255, 255), (100, 500, 100, 100))
        
    #Mafia state
    elif state == "Mafia":
        screen.fill((0,0,0))
        file1.draw(mori)

    #Agency state
    elif state == "Agency":
        screen.fill((0,0,0))
        file2.draw(fukuzawa)

    #Hunting dogs state
    elif state == "Hunting Dogs":
         screen.fill((0,0,0))
         file3.draw(fukuchi)

    #Decay of the Angel
    elif state == "Decay of the Angel":
         screen.fill((0,0,0))
         #file.draw()
         
    pygame.display.flip()
                
#end game loop
pygame.quit()
import pygame

resizeScreen = .8 #1 = fullscreen; .8 = 80% resize
screenLength = int(1536 * resizeScreen) # Lenth of the Screen
screenWidth = int(864 * resizeScreen) # Width of the Screen

screen = pygame.display.set_mode((screenLength,screenWidth)) #create screen
pygame.display.set_caption('DVD Loading Screen')

dvdLogoBlk = pygame.image.load("dvdLogo.png")
dvdX = 0
dvdY = 0
DvdSpeed = .3 #speed that the logo moves
directX = 0 # Can be 0 or 1. 0 if the offset amount is less than the length of the screen. 
            # 1 if it is greater than the length.
            # The 1 or 0 determines what what value to start increasing or decreasing.
directY = 0

while True:
    dvdXOffset = dvdX + 250 #307
    dvdYOffset = dvdY + 110 #139
    
    if dvdXOffset >=  screenLength:
        directX = 1
    elif dvdX <= -1:
        directX = 0  
    
    if dvdYOffset >=  screenWidth:
        directY = 1
    elif dvdY <= -1:
        directY = 0
        
    screen.fill((255,255,255)) # Fill the background with white.
    
    if directY == 0:
        dvdY += DvdSpeed
    elif directY == 1:
        dvdY -= DvdSpeed
    
    if directX == 0:
        dvdX += DvdSpeed
    elif directX == 1:
        dvdX -= DvdSpeed
       

    screen.blit(dvdLogoBlk,(dvdX,dvdY)#blit the logo
    pygame.display.flip() #draws to the screen


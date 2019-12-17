#import the package and initialize the game engine
import pygame
pygame.init()
# timeutil.py
import datetime
import math
import colorsys
#Open a new window, caption it "Pong"
screen = pygame.display.set_mode((700, 500))
pygame.display.set_caption("Pong")

# here's the variable that runs our game loop
doExit = False

# the clock will be used to control how fast the sreeen updates
clock = pygame.time.Clock()
#variables to hold paddle postition
#these go above game loop
p1x= 20
p1y= 200
#ball variables
bx = 350 #xposttion
by = 250 #ypostion
bVx = 5 #x veloctiy (horizontal speed)
bVy = 5 #y veloctiy (vertical speed)
p2x= 660
p2y= 200
p2Score = 0
p1Score = 0
h1 = 0

while not doExit:# Game loop
    #custom rainbow code
    h1 = colorsys.hsv_to_rgb((((math.ceil((datetime.datetime.now().timestamp() * 1000) / 20)) / 360)), 1, 1)
    (r, g, b) = h1
    r*=255
    g*=255
    b*=255
    r = round(r)
    g = round(g)
    b = round(b)
    print((r, g, b))
    color = (255, 255, 255)
    rainbow = (r, g, b)
    # math ceil (get system millis / 20 )) % 360 ) / 360
    
    #event quene stuff------------------------------------------
    clock.tick(60)#set the FPS
    for event in pygame.event.get(): #check if uesr did something
        if event.type==pygame.QUIT: # check if uesr clicked  close
            doExit = True #flag that we are done  so we exit game loop
            
    #game logic will go here------------------------------------------
    #ball movement
    bx += bVx
    by += bVy
    
    #reflect ball on side
    if bx < 0:
        bVx *= -1
        p2Score+= 1
    if bx + 20 > 700:
        bVx *= -1
        p1Score += 1
    #reflect ball on bottom / top 
    if by <= 0 or by + 20 >= 500:
        bVy *= -1
    if bx <= p1x + 20 and by + 20 >= p1y and by <= p1y + 100:
        bVx *= -1
    if bx >= p2x - 20 and by + 20 >= p2y and by <= p2y + 100:
        bVx *= -1
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        p1y-=5
    if keys[pygame.K_s]:
        p1y+=5
    if keys[pygame.K_UP]:
        p2y-=5
    if keys[pygame.K_DOWN]:
        p2y+=5
             
    #render sction will here --------------------------------------
    screen.fill(rainbow) #wipe screen black
    
    #draw a line in the middle
    pygame.draw.line(screen, color, [349, 0], [349, 500], 5)
    # draw a rectangle
    pygame.draw.rect(screen, color ,(p1x,p1y, 20,100))
    #draw ball
    pygame.draw.rect(screen,color,(bx,by, 20,20))
    # draw a rectangle 2
    pygame.draw.rect(screen,color,(p2x,p2y, 20,100))
    
    # display scores
    font =pygame.font.Font(None, 74) # use default font
    text =font.render(str(p1Score),1,color)
    screen.blit(text,(250,10))
    
    text =font.render(str(p2Score),1,color)
    screen.blit(text,(420,10))
    
    pygame.display.flip();
            
# END GAME LOOP

pygame.quit()#when game is done close down game
#just stuff you need to import
import pygame
from random import *
from pygame.locals import *

#setup
pygame.init()
#frames/ticks
clock = pygame.time.Clock()
Frames = 60
#setting the screen
bg_width, bg_height = 1280, 720
screen = pygame.display.set_mode([bg_width,bg_height])
#running the while loop
running = True
#getting events
ev = pygame.event.get()
#setting the name of the window
pygame.display.set_caption('Brownian motion')
#animation variables
start = True
#particles list
balls = []
#ticks
tick = 0
#pause
pause = 0
priorPause = 0
#particle size
ballsize = 4.5
#list cap - temporary
listLim = 60
#speed - slow - S
GreSped = 3
BluSped = 8
RedSped = 16

#counting the particles
r = 0
g = 0
b = 0

#averageness
bec = 0
average = 0
deducter = 0

collisX, collisY = True, True
colydercount = 0
redCount, greenCount, blueCount = 0, 0, 0

#spawning boarders
minX, maxX, minY, maxY = int(160 + ballsize), int(1200 - ballsize), int(15 + ballsize), int(700 - ballsize)

#colors
outline = (75,75,75)
words = (80,80,80)
words2 = (85,85,85)
words3 = (180,180,180)
numbers = (90, 125, 125)

#fonts
font = pygame.font.SysFont('Brandish Medium',60)
font2 = pygame.font.SysFont('Brandish Medium',30)
font3 = pygame.font.SysFont('Brandish Medium',70)
font4 = pygame.font.SysFont('Brandish Medium',45)
font5 = pygame.font.SysFont('Brandish Medium',40)

#creating rectangles with outlines
def outlineRect(outline, coloor, x, y, xSpan, ySpan, thickness):
    pygame.draw.rect(screen,coloor,[x, y, xSpan, ySpan])
    pygame.draw.rect(screen,outline,[x, y, xSpan, ySpan], thickness)
#displaying text
def displayingText(text, x, y, colour, fontt):
    ren7 = fontt.render(text,1,colour)
    screen.blit(ren7,(x,y))
#collider count
def collisioncounter(colydercount, lists, r, g, b, pause):
    if pause != 1:
        colydercount = int(colydercount) + 1
        if lists == 1:
            r += 1
            g += 0
            b += 0
            return colydercount, r, g, b
        elif lists == 2:
            r += 0
            g += 1
            b += 0
            return colydercount, r, g, b
        else:
            r += 0
            g += 0
            b += 1
            return colydercount, r, g, b
    else:
        colydercount += 0
        r += 0
        g += 0
        b += 0
        return colydercount, r, g, b
#starting accelerators of the particles
def rando(lis, Sped):
    while 1 == 1:
        bo = randint(Sped * -1 , Sped )
        yo = randint(Sped * -1 , Sped )
        if bo and yo < 0:
            if bo and yo>= (Sped/2 * -1):
                lk = 0
        if bo < 0:
            if bo >= (Sped/2 * -1):
                lk = 0
        if yo < 0:
            if bo >= (Sped/2 * -1):
                lk = 0
        if (bo or yo == 0):
            lk = 0
        if bo and yo > 0:
            if bo + yo == Sped:
                lis[2] = bo
                lis[3] = yo
                break
        elif bo and yo < 0:
            if bo + yo == Sped * -1:
                lis[2] = bo
                lis[3] = yo
                break
        elif bo < 0 and yo > 0:
            bo *= -1
            if bo + yo == Sped:
                lis[2] = bo
                lis[3] = yo
                break
        else:
            yo -= yo * 2
            if bo + yo == Sped:
                lis[2] = bo
                lis[3] = yo
                break
#producing particles
for j in range(0, listLim):
    balls.append([randint(minX,maxX), randint(minY, maxY), 0, 0, randint(1,3)])
    if balls[j][4] == 1:
        g += 1
        rando(balls[j], GreSped)
    elif balls[j][4] == 2:
        b+= 1
        rando(balls[j], BluSped)

    elif balls[j][4] == 3:
        r += 1
        rando(balls[j], RedSped)

while running:
    #don't worry about these
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                exit()
            elif event.key == K_UP:
                balls.append([randint(minX,maxX), randint(minY, maxY), 0, 0, randint(1,3), 1])

                if balls[listLim][4] == 1:
                    g += 1
                    rando(balls[listLim], GreSped)
                elif balls[listLim][4] == 2:
                    b+= 1
                    rando(balls[listLim], BluSped)

                elif balls[listLim][4] == 3:
                    r += 1
                    rando(balls[listLim], RedSped)
                listLim += 1
            elif event.key == K_DOWN:
                if balls[listLim - 1][4] == 1:
                    g -= 1
                elif balls[listLim - 1][4] == 2:
                    b -= 1
                else:
                    r -= 1
                balls.pop(listLim - 1)
                listLim -= 1
            elif event.key == K_SPACE and priorPause == 1:
                pause = 0
                priorPause = 0
            elif event.key == K_SPACE and priorPause == 0:
                pause = 1
                priorPause = 1

        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN or (event.type == pygame.KEYDOWN):
            if 40 <= pygame.mouse.get_pos()[0] <= 110 and (260 <= pygame.mouse.get_pos()[1] <= 320 and listLim < 275):
                balls.append([randint(minX,maxX), randint(minY, maxY), 0, 0, randint(1,3), 1])

                if balls[listLim][4] == 1:
                    g += 1
                    rando(balls[listLim], GreSped)
                elif balls[listLim][4] == 2:
                    b+= 1
                    rando(balls[listLim], BluSped)

                elif balls[listLim][4] == 3:
                    r += 1
                    rando(balls[listLim], RedSped)
                listLim += 1

            elif 40 <= pygame.mouse.get_pos()[0] <= 110 and (260 <= pygame.mouse.get_pos()[1] <= 410)  and listLim > 0:

                if balls[listLim - 1][4] == 1:
                    g -= 1
                elif balls[listLim - 1][4] == 2:
                    b -= 1
                else:
                    r -= 1
                balls.pop(listLim - 1)
                listLim -= 1
            elif 1200 <= pygame.mouse.get_pos()[0] <= 1260 and (650 <= pygame.mouse.get_pos()[1] <= 710):
                pause = 0
                priorPause = 0
            elif 1130 <= pygame.mouse.get_pos()[0] <= 1190 and (650 <= pygame.mouse.get_pos()[1] <= 710):
                pause = 1
                priorPause = 1
    #background
    screen.fill((50,50,50))

    #for checking in collisions and displayment
    for j in balls:

        #collision with the boarder
        #collision with top of the screen
        if j[1] >= 720 - ballsize and collisY == True:
            j[1] -= ballsize
            j[3] *= -1
            collisY = False
            colydercount, redCount, greenCount, blueCount = collisioncounter(colydercount, j[4], redCount, greenCount, blueCount, pause)
        #colission with top of the screen
        if j[1] <= 0 + ballsize and collisX == True:
            j[1] += ballsize
            j[3] *= -1
            collisX = False
            colydercount, redCount, greenCount, blueCount = collisioncounter(colydercount, j[4], redCount, greenCount, blueCount, pause)
        #right screen collision
        if j[0] >= 1280 - ballsize and collisY == True:
            j[0] -= ballsize
            j[2] *= -1
            collisY = False
            colydercount, redCount, greenCount, blueCount = collisioncounter(colydercount, j[4], redCount, greenCount, blueCount, pause)
        #left screen collision
        if j[0] <= 150 + ballsize and collisX == True:
            j[0] += ballsize
            j[2] *= -1
            collisX = False
            colydercount, redCount, greenCount, blueCount = collisioncounter(colydercount, j[4], redCount, greenCount, blueCount, pause)

        #allow collision to turn back on
        if j[1] <= 710 - ballsize:
            collisY = True
        if j[1] >= 10 + ballsize:
            collisX = True
        if j[0] <= 1270 - ballsize:
            collisY = True
        if j[0] >= 160 + ballsize:
            collisX = True

        #collision for other particles
        for i in balls:
            if j[1] != i[1] and j[0] != i[0]:
                #collision with other balls
                if (i[0] <= (j[0] + ballsize * 2) and i[0] >= (j[0] - ballsize * 2 - 2)) and (i[1] <= (j[1] + ballsize * 2) and i[1] >= (j[1] - ballsize * 2)):
                    if ((i[2] < 0 and j[2] > 0) or (j[2] < 0 and i[2])) and ((i[3] < 0 and j[3] > 0) or (j[3] < 0 and i[3])):
                        j[2] *= -1
                        i[2] *= -1
                        j[3] *= -1
                        i[3] *= -1
                    elif (i[2] < 0 and j[2] < 0) or (j[2] > 0 and i[2] > 0):
                        j[2] *= -1
                        j[3] *= -1
                        i[3] *= -1
                    elif (i[3] < 0 and j[3] < 0) or (j[3] > 0 and i[3] > 0):
                        j[2] *= -1
                        j[3] *= -1
                        i[2] *= -1
                    colydercount, redCount, greenCount, blueCount = collisioncounter(colydercount, j[4], redCount, greenCount, blueCount, pause)
        #adding movement
        if pause == 0:
            j[0] += j[2]
            j[1] += j[3]

        #displaying the particles
        if j[4] == 1:
            pygame.draw.circle(screen,(100,220,100),(j[0],j[1]), ballsize)
        elif j[4] == 2:
            pygame.draw.circle(screen,(100,100,220),(j[0],j[1]), ballsize)
        else:
            pygame.draw.circle(screen,(220,100,100),(j[0],j[1]), ballsize)

    #graphics
    outlineRect(outline, (170,170,170), 0, 0, 150, 720, 8)

    outlineRect(outline, (200,200,120), 0, 0, 150, 70, 8)

    outlineRect(outline, (120,140,140), 0, 65, 150, 185, 8)

    outlineRect(outline, (120,120,120), 0, 245, 150, 235, 8)

    #buttons
    #adding button
    outlineRect(outline, (180,180,140), 40, 260, 70, 60, 10)
    pygame.draw.rect(screen,(100,100,100),[45, 265, 60, 50], 5)

    #deducting button
    outlineRect(outline, (180,180,140), 40, 350, 70, 60, 10)
    pygame.draw.rect(screen,(100,100,100),[45, 355, 60, 50], 5)

    #pausing and resuming button
    #resuming
    outlineRect(outline, (170,170,170), 1200, 650, 60, 60, 5)
    pygame.draw.rect(screen,(100,100,100),[1205, 655, 50, 50], 2)

    pygame.draw.polygon(screen,(100,100,100),[(1220, 665), (1240,680), (1220, 695) ])

    #pausing
    outlineRect(outline, (170,170,170), 1130, 650, 60, 60, 5)
    pygame.draw.rect(screen,(100,100,100),[1135, 655, 50, 50], 2)

    pygame.draw.rect(screen,(100,100,100),[1147, 660, 10, 40])
    pygame.draw.rect(screen,(100,100,100),[1165, 660, 10, 40])

    #displaying balls on the stastistics
    for i in balls:
        pygame.draw.circle(screen,(100,220,100),(20 + (ballsize + 8),105),  10)
        pygame.draw.circle(screen,(100,100,220),(20 + (ballsize + 8),165), 10)
        pygame.draw.circle(screen,(220,100,100),(20 + (ballsize + 8),225), 10)

    displayingText('Total: ' + str(listLim), 10, 20, words, font5)

    displayingText('- ' + str(g), 60, 80, words, font)

    displayingText('- ' + str(b), 60, 140, words, font)

    displayingText('- ' + str(r), 60, 200, words, font)

    displayingText('+', 60, 263, words2, font3)

    displayingText('--', 60, 354, words2, font3)

    displayingText('Particle', 20, 415, words3, font4)

    displayingText('amount', 20, 440, words3, font4)

    displayingText('collisions:', 10, 500, words, font2)

    displayingText(str(colydercount), 10, 520, numbers, font2)

    displayingText('red:', 10, 540, words, font2)

    displayingText(str(redCount), 10, 560, numbers, font2)

    displayingText('green:', 10, 580, words, font2)

    displayingText(str(greenCount), 10, 600, numbers, font2)

    displayingText('blue:', 10, 620, words, font2)

    displayingText(str(blueCount), 10, 640, numbers, font2)

    displayingText('Average:', 10, 660, words, font2)

    displayingText(str(average) + '/S', 10, 680, numbers, font2)

    if tick % Frames == 0 and pause == 0:
        deducter += 1
        print(colydercount)
        if deducter == 1:
            bec = colydercount
        if deducter == 2 and pause == 0:
            average = (colydercount - bec) / 2
            print(average)
            deducter = 0


    #graphis end
    #counting every tick/frames
    tick += 1
    #other stuff I need to do for this shit to work
    start = False
    clock.tick(Frames)
    pygame.display.flip()

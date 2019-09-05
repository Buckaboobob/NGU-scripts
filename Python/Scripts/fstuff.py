
import sys
import pygame
from pygame.locals import *
from classes.inputs import Inputs
from classes.window import Window
import coordinates as coords

w = Window()
i = Inputs()

Window.x, Window.y = i.pixel_search(coords.TOP_LEFT_COLOR, 0, 0, 400, 600)

zoom = 1
locx = int(sys.argv[1])
locy = int(sys.argv[2])
sizx = 50
sizy = 50
clickx = round(locx + (sizx // 2 ))
clicky = round(locy + (sizy // 2 ))
global screen
myfill = (0,0,0)

pygame.init()
pygame.key.set_repeat(200, 100)
i.get_screenshot()
image = pygame.image.load(r'screenshots/screen.png')

def getcrop():
    global screen
    global image
    global clickx, clicky
    font = pygame.font.Font('freesansbold.ttf', 24)
    clickx = round(locx + (sizx // 2 ))
    clicky = round(locy + (sizy // 2 ))
#    print(str(sizx)+ " " + str(sizy)+ " " + str(locx)+ " " + str(locy))

#    image = pygame.image.load(r'screenshots/screen.png')

    screen.fill(myfill)
    mytext = "X:" + str(locx)
    text = font.render(mytext, True, ((255, 255, 255)))
    screen.blit(text, (700, 100))
    mytext = "Y:" + str(locy)
    text = font.render(mytext, True, ((255, 255, 255)))
    screen.blit(text, (700, 140))
    mytext = "Cut:" + str(locx) + "x" + str(locy) + "+" + str(locx+sizx) + "+" + str(locy+sizy)
    text = font.render(mytext, True, ((255, 255, 255)))
    screen.blit(text, (440, 450))
    mytext = "Click:" + str(clickx) + ", " + str(clicky)
    text = font.render(mytext, True, ((255, 255, 255)))
    screen.blit(text, (600, 180))
#    screen.blit(pygame.transform.scale(image, (sizx * zoom, sizy * zoom)), (10, 10), (locx, locy, sizx, sizy))

    screen.blit(image, (10, 10), (locx, locy, sizx, sizy))
    pygame.display.update()
    
def main():
    global myfill
    global zoom
    global locx
    global locy
    global sizx
    global sizy
    global screen
    global image
    shift = False
#    call(["/home/me/ngu/scripts/shot.sh"], shell = True)
#    logo = pygame.image.load("tmp/logo.png")
#    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")
    screen = pygame.display.set_mode((840,480))
    getcrop()
    running = True
    pygame.display.update()
    while running:
        for event in pygame.event.get():
            if event.type == KEYUP:
                if event.key == K_LSHIFT:
                    shift = False
            if event.type == KEYDOWN:
#               print('Keydown')
                if event.key == K_ESCAPE:
#                    print('Escape')
                    running = False
                if event.key == K_SPACE:
                    i.get_screenshot()
                    image = pygame.image.load(r'screenshots/screen.png')
                    screen.blit(image, (10, 10), (locx, locy, sizx, sizy))
                    pygame.display.update()
                if event.key == K_LSHIFT:
                    shift = True
                if event.key == K_UP:
                    if shift == True:
                        locy -= 5
                    else :
                        locy -= 1
                    getcrop()
                if event.key == K_DOWN:
                    if shift == True:
                        locy += 5
                    else :
                        locy += 1
                    getcrop()
                if event.key == K_LEFT:
                    if shift == True:
                        locx -= 5
                    else :
                        locx -= 1
                    getcrop()
                if event.key == K_RIGHT:
                    if shift == True:
                        locx += 5
                    else :
                        locx += 1
                    getcrop()
                if event.key == K_KP_PLUS:
                    if zoom < 100:
                        zoom += 5
                    else:
                        zoom += 100
                    getcrop()
                if event.key == K_KP_MINUS:
                    if zoom <= 100:
                        zoom -= 5
                    else:
                        zoom -= 100
                    getcrop()
                if event.key == K_KP8:
                    print("KP8")
                    if shift == True:
                        sizy -= 5
                    else :
                        sizy -= 1
                    getcrop()
                if event.key == K_KP2:
                    if shift == True:
                        sizy += 5
                    else :
                        sizy += 1
                    getcrop()
                if event.key == K_KP4:
                    if shift == True:
                        sizx -= 5
                    else :
                        sizx -= 1
                    getcrop()
                if event.key == K_KP6:
                    if shift == True:
                        sizx += 5
                    else :
                        sizx += 1
                    getcrop()
                if event.key == K_KP_DIVIDE:
                    myfill = (255, 255, 255)
                    getcrop()
                if event.key == K_KP_MULTIPLY:
                    myfill = (0, 0, 0)
                    getcrop()
                    
                    
    print('Exiting')
    pygame.display.quit()
    pygame.quit()
    exit()


if __name__=="__main__":
    # call the main function
    main()

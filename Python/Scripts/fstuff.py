import sys
import pygame
from PIL import Image
from pygame.locals import *
from classes.inputs import Inputs
from classes.window import Window
import coordinates as coords

w = Window()
i = Inputs()

Window.x, Window.y = i.pixel_search(coords.TOP_LEFT_COLOR, 0, 0, 400, 600)

zoom = 1
if len(sys.argv) > 1:
    locx = int(sys.argv[1])
else:
    locx = 1
if len(sys.argv) > 2:
    locy = int(sys.argv[2])
else:
    locy = 1
if len(sys.argv) > 3:
    sizx = int(sys.argv[3])
else:
    sizx = 50
if len(sys.argv) > 4:
    sizy = int(sys.argv[4])
else:
    sizy = 50
clickx = round(locx + (sizx // 2))
clicky = round(locy + (sizy // 2))
global screen
myfill = (0, 0, 0)

pygame.init()
pygame.key.set_repeat(200, 100)
i.get_screenshot()
img = Image.open(r'screenshots/screen.png')


def getcrop():
    global screen
    global image
    global clickx, clicky
    global locx
    global locy
    global sizx
    global sizy
    global zoom
    font = pygame.font.Font('freesansbold.ttf', 24)
    clickx = round(locx + (sizx // 2))
    clicky = round(locy + (sizy // 2))
    screen.fill(myfill)
    mytext = "X:{} Y:{}      Click: {}, {}                 OCRBox: ({}, {}, {}, {})".format(str(locx),
                                                                                            str(locy),
                                                                                            str(clickx),
                                                                                            str(clicky),
                                                                                            str(locx),
                                                                                            str(locy),
                                                                                            str(locx + sizx),
                                                                                            str(locy + sizy))
    text = font.render(mytext, True, (255, 255, 255))
    screen.blit(text, (40, 450))
    cimg = img.crop((locx, locy, locx + sizx, locy + sizy))
    h, w = cimg.size
    cimg = cimg.resize((h * zoom, w * zoom))
    mode = cimg.mode
    size = cimg.size
    data = cimg.tobytes()
    image = pygame.image.fromstring(data, size, mode)
    screen.blit(image, (10, 10))
    pygame.display.update()


def main():
    global myfill
    global zoom
    global locx
    global locy
    global sizx
    global sizy
    global screen
    global img
    shift = False
    pygame.display.set_caption("minimal program")
    screen = pygame.display.set_mode((840, 480))
    getcrop()
    running = True
    pygame.display.update()
    while running:
        for event in pygame.event.get():
            if event.type == KEYUP:
                if event.key == K_LSHIFT:
                    shift = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_SPACE:
                    i.get_screenshot()
                    img = Image.open(r'screenshots/screen.png')
                    getcrop()
                if event.key == K_LSHIFT:
                    shift = True
                if event.key == K_UP:
                    if shift is True:
                        locy -= 5
                    else:
                        locy -= 1
                    getcrop()
                if event.key == K_DOWN:
                    if shift is True:
                        locy += 5
                    else:
                        locy += 1
                    getcrop()
                if event.key == K_LEFT:
                    if shift is True:
                        locx -= 5
                    else:
                        locx -= 1
                    getcrop()
                if event.key == K_RIGHT:
                    if shift is True:
                        locx += 5
                    else:
                        locx += 1
                    getcrop()
                if event.key == K_KP_PLUS:
                    zoom += 1
                    getcrop()
                if event.key == K_KP_MINUS:
                    zoom -= 1
                    getcrop()
                if event.key == K_KP8:
                    if shift is True:
                        sizy -= 5
                    else:
                        sizy -= 1
                    getcrop()
                if event.key == K_KP2:
                    if shift is True:
                        sizy += 5
                    else:
                        sizy += 1
                    getcrop()
                if event.key == K_KP4:
                    if shift is True:
                        sizx -= 5
                    else:
                        sizx -= 1
                    getcrop()
                if event.key == K_KP6:
                    if shift is True:
                        sizx += 5
                    else:
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


if __name__ == "__main__":
    # call the main function
    main()

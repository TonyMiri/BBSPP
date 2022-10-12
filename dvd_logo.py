import sys, time
from random import randint
import bext as bx

bx.fg('yellow')
bx.bg('black')
bx.title('DVD Screensaver')
width, height = bx.size()

x = randint(0, width)
y = randint(0, height)

direction = ["S", "E"]

try:
    while True:
        time.sleep(0.1)
        bx.clear()
        if x == width - 1:
            direction[1] = 'W'
        if x == 1:
            direction[1] = 'E'
        if y == height - 1:
            direction[0] = 'N'
        if y == 0:
            direction[0] = 'S'

        if direction[0] == 'N':
            y -= 1
        if direction[0] == 'S':
            y += 1
        if direction[1] == 'E':
            x += 1
        if direction[1] == 'W':
            x -= 1

        bx.goto(x,y)
        print('DVD')       
except KeyboardInterrupt:
    sys.exit()
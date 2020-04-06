"""Ant, simple animation demo.

Exercises

1. Wrap ant around screen boundaries.
2. Make the ant leave a trail.
3. Change the ant color based on position.
   Hint: colormode(255); color(0, 100, 200)

"""

from random import *
from turtle import *
import time
from freegames import vector

ant = vector(0, 0)
aim = vector(2, 0)
running = True

def wrap(value):
    "Wrap value around -200 and 200."
    if value == (-200):
        aim.rotate(angle=170)
        aim.move(2)
        return(value)
    if value == (200):
        aim.rotate(angle=170)
        aim.move(2)
        return(value)

def move(x,y):
    aim.x = x
    aim.y = y

def draw():
    "Move ant and draw screen."
    ant.move(aim)
    if (ant.x == 200 or ant.x == -200):
        ant.x = 0
        ant.y = 0
        aim.rotate(wrap(ant.x))
    if (ant.y == 200 or ant.y == -200):
        ant.x = 0
        ant.y = 0
        aim.rotate(wrap(ant.y))

    aim.move(1)
    aim.rotate(random())

    clear()
    goto(ant.x, ant.y)
    dot(4)
    update()

    '''if running:
        ontimer(draw, 1)'''
    

def openPage():
    setup(420, 420, 370, 0)
    goto(0,0)
    pendown()
    color('black')
    style = ('courier', 35, 'italic')
    style2 = ('courier', 15, 'italic')
    write('WELCOME TO ANT!', font= style, align= 'center')
    penup()
    goto(0,-25)
    pendown()
    write("Let the Ant do it's thing", font= style2, align= 'center')
    hideturtle()
    time.sleep(4)

def main(): 
    openPage()
    setup(420, 420, 370, 0)
    hideturtle()
    tracer(False)
    up()
    """running = True"""
    onkey(lambda: move(10, 0), 'Right')
    onkey(lambda: move(-10, 0), 'Left')
    onkey(lambda: move(0, 10), 'Up')
    onkey(lambda: move(0, -10), 'Down')
    draw()
    done()

main()

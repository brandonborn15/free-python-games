"""Tron, classic arcade game.

Exercises

1. Make the tron players faster/slower.
2. Stop a tron player from running into itself.
3. Allow the tron player to go around the edge of the screen.
4. How would you create a computer player?

"""

from turtle import *
import time
from freegames import square, vector

p1xy = vector(-100, 0)
p1aim = vector(4, 0)
p1body = set()

p2xy = vector(100, 0)
p2aim = vector(-4, 0)
p2body = set()

def inside(head):
    "Return True if head inside screen."
    return -300 < head.x < 300 and -300 < head.y < 300

def draw():
    "Advance players and draw game."
    p1xy.move(p1aim)
    p1head = p1xy.copy()

    p2xy.move(p2aim)
    p2head = p2xy.copy()

    if not inside(p1head) or p1head in p2body:
        blue = blue+1
        print('Tron wins!')
        time.sleep(1.5)
        clear()
        color('blue')
        style = ('courier', 35, 'italic')
        write("Clu was Derezzed", font = style, align = "center" )
        

    if not inside(p2head) or p2head in p1body:
        red = red+1
        print('Clu wins!')
        time.sleep(1.5)
        clear()
        goto(0,0)
        color('red')
        style = ('courier', 35, 'italic')
        write("Tron was Derezzed", font = style, align = "center" )

        

    p1body.add(p1head)
    p2body.add(p2head)

    square(p1xy.x, p1xy.y, 3, 'red')
    square(p2xy.x, p2xy.y, 3, 'blue')
    update()
    ontimer(draw, 50)

def tronLogo():
    hideturtle()
    width(3)
    goto(-210,0)
    pendown()
    color('cyan')
    forward(30)
    left(90)
    forward(20)
    left(90)
    forward(30)
    left(90)
    forward(20)
    penup()

    goto(-175,0)
    pendown()
    left(180)
    forward(20)
    right(90)
    forward(135)
    right(90)
    forward(20)
    right(90)
    forward(115)
    left(90)
    forward(80)
    right(90)
    forward(20)
    right(90)
    forward(100)
    penup()

    goto(-115,-10)
    pendown()
    right(90)
    forward(20)
    right(90)
    forward(70)
    right(90)
    forward(20)
    right(90)
    forward(70)
    penup()

    goto(-90,-10)
    pendown()
    right(90)
    forward(50)
    right(90)
    forward(20)
    right(90)
    forward(30)
    left(115)
    forward(55)
    right(115)
    forward(20)
    right(65)
    forward(60)
    right(25)
    forward(15)
    penup()

    goto(60,-30)
    pendown()
    circle(30)
    penup()
    goto(85,-30)
    pendown()
    circle(55)
    penup()

    goto(100,20)
    pendown()
    right(90)
    forward(15)
    right(65)
    forward(50)
    right(25)
    forward(20)
    right(90)
    forward(15)
    left(90)
    forward(40)
    right(90)
    forward(20)
    right(90)
    forward(105)
    penup()

    goto(160,20)
    pendown()
    right(90)
    forward(20)
    right(90)
    forward(105)
    right(90)
    forward(15)
    right(65)
    forward(45)
    right(25)
    forward(20)
    right(90)
    forward(15)
    left(90)
    forward(45)
    penup()

def openpage():
    setup(620, 620, 570, 0)
    bgcolor('black')
    goto(0,50)
    pendown()
    color('cyan')
    style = ('courier', 35, 'italic')
    style2 = ('courier', 15, 'italic')
    write('WELCOME TO', font= style, align= 'center')
    penup()
    tronLogo()

def run():
    clear()
    setup(620, 620, 570, 0)
    bgcolor('black')
    hideturtle()
    tracer(False)
    listen()
    onkey(lambda: p1aim.rotate(90), 'Right')
    onkey(lambda: p1aim.rotate(-90), 'Left')

    onkey(lambda: p2aim.rotate(90), 'a')
    onkey(lambda: p2aim.rotate(-90), 'd')
    draw()
    done()

def main():
    openpage()
    goto(0,-150)
    color('cyan')
    style = ('courier', 15, 'italic')
    write("Start", font = style, align = "center" )
    time.sleep(1)
    run()
    
main()
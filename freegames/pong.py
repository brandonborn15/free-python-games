"""Pong, classic arcade game.

Exercises

1. Change the colors.
2. What is the frame rate? Make it faster or slower.
3. Change the speed of the ball.
4. Change the size of the paddles.
5. Change how the ball bounces off walls.
6. How would you add a computer player?
6. Add a second ball.

"""

from random import choice, random
from turtle import *
import time
from freegames import vector


def value():
    "Randomly generate value between (-5, -3) or (3, 5)."
    return (3 + random() * 2) * choice([1, -1])

ball = vector(0, 0)
aim = vector(7, 7)
state = {1: 0, 2: 0}

def move(player, change):
    "Move player position by change."
    state[player] += change

def rectangle(x, y, width, height):
    "Draw rectangle at (x, y) with given width and height."
    up()
    goto(x, y)
    down()
    begin_fill()
    for count in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)
    end_fill()

def draw():
    "Draw game and move pong ball."
    player1 = 0
    player2 = 0

    color('white')
    clear()

    fillcolor("blue")
    begin_fill()
    rectangle(-200, state[1], 10, 50)
    end_fill()

    fillcolor("red")
    begin_fill()
    rectangle(190, state[2], 10, 50)
    end_fill()

    color('cyan')
    ball.move(aim)
    x = ball.x
    y = ball.y

    up()
    goto(x, y)
    dot(10)
    update()

    if y < -200 or y > 200:
        aim.y = -aim.y

    if x < -185:
        low = state[1]
        high = state[1] + 50

        if low <= y <= high:
            aim.x = -aim.x
        else:
            player1 = player1+1
            print(player1)
            ball.x = 0
            ball.y = 0
            time.sleep(1)

    if x > 185:
        low = state[2]
        high = state[2] + 50

        if low <= y <= high:
            aim.x = -aim.x
        else:
            player2 = player2+1
            print(player2)
            ball.x = 0
            ball.y = 0
            time.sleep(1)

        

    ontimer(draw, 50)

def openpage():
    setup(420, 420, 370, 0)
    bgcolor('grey')
    goto(0,0)
    pendown()
    color('black')
    style = ('courier', 35, 'italic')
    style2 = ('courier', 15, 'italic')
    write('WELCOME TO PONG!', font= style, align= 'center')
    penup()

    goto(0,-25)
    pendown()
    write('Move the paddles and beat your opponets', font= style2, align= 'center')
    penup()

    color('blue')
    goto(-90,-70)
    pendown()
    write('player 2 controls \nW and S keys', font= style2, align= 'center')
    penup()

    color('red')
    goto(90,-70)
    pendown()
    write('player 2 controls \nUp and down keys', font= style2, align= 'center')
    hideturtle()
    time.sleep(4)  

def run():
    setup(420, 420, 370, 0)
    bgcolor('grey')
    hideturtle()
    tracer(False)
    listen()
    onkey(lambda: move(1, 25), 'w')
    onkey(lambda: move(1, -25), 's')
    onkey(lambda: move(2, 25), 'Up')
    onkey(lambda: move(2, -25), 'Down')
    draw()
    done()

def main():
    openpage()
    run()
main()

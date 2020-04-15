"""Tic Tac Toe

Exercises

1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot?
3. How would you detect when someone has won?
4. How could you create a computer player?

"""

from turtle import *
import time
from freegames import line

def grid():
    "Draw tic-tac-toe grid."
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)

def drawx(x, y):
    "Draw X player."
    pensize(10)
    line(x, y, x + 133, y + 133)
    line(x, y + 133, x + 133, y)

def drawo(x, y):
    "Draw O player."
    up()
    pensize(10)
    goto(x + 67, y + 5)
    down()
    circle(62)

def floor(value):
    "Round value down to grid with square size 133."
    return ((value + 200) // 133) * 133 - 200

state = {'player': 0}
players = [drawx, drawo]

def tap(x, y):
    "Draw X or O in tapped square."
    x = floor(x)
    y = floor(y)
    player = state['player']
    draw = players[player]
    draw(x, y)
    update()
    state['player'] = not player

def openPage():
    setup(420, 420, 370, 0)
    goto(0,0)
    pendown()
    color('black')
    style = ('courier', 35, 'italic')
    style2 = ('courier', 15, 'italic')
    write('WELCOME TO \nTIC TAC TOE!', font= style, align= 'center')
    penup()
    hideturtle()
    time.sleep(4)

def main(): 
    openPage()
    clear()
    setup(420, 420, 370, 0)
    hideturtle()
    tracer(False)
    grid()
    update()
    onscreenclick(tap)
    done()
main()

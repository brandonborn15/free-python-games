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

#board
box1 = ''
box2 = ''
box3 = ''
box4 = ''
box5 = ''
box6 = ''
box7 = ''
box8 = ''
box9 = ''

def grid():
    "Draw tic-tac-toe grid."
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)

def drawx(x, y):
    "Draw X player."
    print(x)
    print(y)
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

def checkwin():
    'checks to see if someone won'
    global box1, box2, box3, box4, box5, box6, box7, box8, box9
    wins = [[box1, box2, box3], [box4, box5, box6], [box7, box8, box9], [box1, box4, box7], [box2, box5, box8], [box3, box6, box9], [box1, box5, box9], [box3, box5, box7]]
    for scenario in wins:
        if scenario[0] == scenario[1] == scenario[2] and scenario[0] != '':
            print("CONGRATULATIONS, " + scenario[0] + ' wins!')
            main()

def floor(value):
    "Round value down to grid with square size 133."
    return ((value + 200) // 133) * 133 - 200

def aiturn():
    "AI's turn"
    global box1, box2, box3, box4, box5, box6, box7, box8, box9
    wins = [[box1, box2, box3], [box4, box5, box6], [box7, box8, box9], [box1, box4, box7], [box2, box5, box8], [box3, box6, box9], [box1, box5, box9], [box3, box5, box7]]
    prospects = []
    for scenario in wins:
        xcount = 0
        spacecount = 0
        ocount = 0
        for box in scenario:
            if box == 'x':
                xcount += 1
            elif box == '':
                spacecount += 1
            else:
                ocount += 1
        prospects.append([scenario, xcount, spacecount, ocount])
    for prospect in prospects:
        if prospect[3] == 2 and prospect[2] == 1:
            for box in prospect[0]:
                if box == '':
                    box = 'o'
                    #CODE TO DRAW THE O
                    checkwin()
                    update()
    for prospect in prospects:
        if prospect[1] == 2 and prospect[2] == 1:
            for box in prospect[0]:
                if box == '':
                    box = 'o'
                    #CODE TO DRAW THE O
                    checkwin()
                    update()
    #CODE TO PICK A RANDOM NUMBER 1-9 and check to see if it has been chosen already
    #CODE TO DRAW THE O
    update()

def tap(x, y):
    'Draw X or O in tapped square.'
    global box1, box2, box3, box4, box5, box6, box7, box8, box9
    if x < -67 and y > 67 and box1 == '':
        box1 = 'x'
    elif -67 <= x <= 67 and y > 67 and box2 == '':
        box2 = 'x'
    elif x > 67 and y > 67 and box3 == '':
        box3 = 'x'
    elif x < -67 and -67 <= y <= 67 and box4 == '':
        box4 = 'x'
    elif -67 <= x <= 67 and -67 <= y <= 67 and box5 == '':
        box5 = 'x'
    elif x > 67 and -67 <= y <= 67 and box6 == '':
        box6 = 'x'
    elif x < -67 and y < -67 and box7 == '':
        box7 = 'x'
    elif -67 <= x <= 67 and y < -67 and box8 == '':
        box8 = 'x'
    elif x > 67 and y < -67 and box9 == '':
        box9 = 'x'
    else:
        print('invalid box')
    x = floor(x)
    y = floor(y)
    drawx(x, y)
    checkwin()
    aiturn()
    update()

def openPage():
    'Creates a title screen'
    setup(420, 420, 370, 0)
    goto(0, 0)
    pendown()
    color('black')
    style = ('courier', 35, 'italic')
    style2 = ('courier', 15, 'italic')
    write('WELCOME TO \nTIC TAC TOE!', font=style, align='center')
    penup()
    hideturtle()
    time.sleep(4)

def main():
    'main function'
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

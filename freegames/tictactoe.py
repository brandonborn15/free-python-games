"""Tic Tac Toe

Exercises

1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot?
3. How would you detect when someone has won?
4. How could you create a computer player?

"""
import random
from turtle import *
import time
from freegames import line

#board
boxes = ['', '', '', '', '', '', '', '', '']

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
    checkwin()

def drawo(x, y):
    "Draw O player."
    up()
    pensize(10)
    goto(x + 67, y + 5)
    down()
    circle(62)
    checkwin()

def checkwin():
    'checks to see if someone won'
    global boxes
    wins = [[boxes[0], boxes[1], boxes[2]], [boxes[3], boxes[4], boxes[5]], [boxes[6], boxes[7], boxes[8]], [boxes[0], boxes[3], boxes[6]], [boxes[1], boxes[4], boxes[7]], [boxes[2], boxes[5], boxes[8]], [boxes[0], boxes[4], boxes[8]], [boxes[2], boxes[4], boxes[6]]]
    for scenario in wins:
        if scenario[0] == scenario[1] == scenario[2] and scenario[0] != '':
            print("CONGRATULATIONS, " + scenario[0] + ' wins!')
            clearBoard()
            run()

def floor(value):
    "Round value down to grid with square size 133."
    return ((value + 200) // 133) * 133 - 200

def aiturn():
    "AI's turn"
    global boxes
    wins = [[boxes[0], boxes[1], boxes[2]], [boxes[3], boxes[4], boxes[5]], [boxes[6], boxes[7], boxes[8]], [boxes[0], boxes[3], boxes[6]], [boxes[1], boxes[4], boxes[7]], [boxes[2], boxes[5], boxes[8]], [boxes[0], boxes[4], boxes[8]], [boxes[2], boxes[4], boxes[6]]]
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
            elif box == 'o':
                ocount += 1
        prospects.append([xcount, spacecount, ocount, wins.index(scenario)])
    temp = []
    win = False
    block = False
    for prospect in prospects:
        if prospect[2] == 2 and prospect[1] == 1:
            temp = prospect
            win = True
            break
        elif prospect[0] == 2 and prospect[1] == 1:
            temp = prospect
            block = True
            break
    if win == True or block == True:
        print("Block")
        print(temp)
        boxFinder(temp)
    else:
        print("idk")
        tempi = 9
        valid = False
        while valid == False:
            index = random.randrange(0, 8)
            if boxes[index] == '':
                tempi = index
                valid = True
        makeMove(tempi)

def boxFinder(prospect):
    global boxes
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for index in wins[prospect[3]]:
        if boxes[index] == '':
            boxes[index] = 'tbd'
    for num in range(0, 8):
        if boxes[num] == 'tbd':
            theChosenOne = num
            boxes[num] = 'o'
            makeMove(theChosenOne)

def makeMove(index):
    if index == 0:
        drawo(-200.0, 66.0)
        print("1")
    elif index == 1:
        drawo(-67.0, 66.0)
    elif index == 2:
        drawo(66.0, 66.0)
    elif index == 3:
        drawo(-200.0, -67.0)
    elif index == 4:
        drawo(-67.0, -67.0)
    elif index == 5:
        drawo(66.0, -67.0)
    elif index == 6:
        drawo(-200.0, -200.0)
    elif index == 7:
        drawo(-67.0, -200.0)
    elif index == 8:
        drawo(66.0, -200.0)
    else:
        print("ERROR")
    update()

def tap(x, y):
    'Draw X or O in tapped square.'
    global boxes
    if x < -67 and y > 67 and boxes[0] == '':
        boxes[0] = 'x'
    elif -67 <= x <= 67 and y > 67 and boxes[1] == '':
        boxes[1] = 'x'
    elif x > 67 and y > 67 and boxes[2] == '':
        boxes[2] = 'x'
    elif x < -67 and -67 <= y <= 67 and boxes[3] == '':
        boxes[3] = 'x'
    elif -67 <= x <= 67 and -67 <= y <= 67 and boxes[4] == '':
        boxes[4] = 'x'
    elif x > 67 and -67 <= y <= 67 and boxes[5] == '':
        boxes[5] = 'x'
    elif x < -67 and y < -67 and boxes[6] == '':
        boxes[6] = 'x'
    elif -67 <= x <= 67 and y < -67 and boxes[7] == '':
        boxes[7] = 'x'
    elif x > 67 and y < -67 and boxes[8] == '':
        boxes[8] = 'x'
    else:
        print('invalid box')
    x = floor(x)
    y = floor(y)
    drawx(x, y)
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
    run()

def run():
    clear()
    setup(420, 420, 370, 0)
    hideturtle()
    tracer(False)
    grid()
    update()
    onscreenclick(tap)
    done()

def clearBoard():
    global boxes
    for box in boxes:
        box = ''

main()

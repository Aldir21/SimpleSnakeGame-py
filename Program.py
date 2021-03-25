import os
import random

Width = 11
Height = 11

Block = "="
Blank = " "
Snake = "◆"
Food = "◈"
Tail = "◇"

GameOver = False

Snake_Position = [1,1]
Food_Position = [0,0]

Tail_Positions = []

def isTailPos(x,y):
    Same = False
    if len(Tail_Positions) > 0:
        for i in range(0, len(Tail_Positions)):
            if Tail_Positions[i][0] == x and Tail_Positions[i][1] == y:
                Same = True
    return Same

def RandomizeFoodPos():
    AvailablePos = [[1,1]]

    for y in range(1, Height+1):
        for x in range(1, Width+1):
            if x % 2 != 0 and y % 2 != 0 and x != Snake_Position[0] and y != Snake_Position[1] and [x,y] not in Tail_Positions:
                AvailablePos.insert(0, [x,y])
    random.shuffle(AvailablePos)
    Food_Position[0] = AvailablePos[0][0]
    Food_Position[1] = AvailablePos[0][1]

def ReDraw():
    os.system('cls')
    print("ASWD To Control")
    print("Length : ", len(Tail_Positions))
    print("\n")
    for y in range(0, Height+2):
        for x in range(0, Width+2):
            if x == Snake_Position[0] and y == Snake_Position[1]:
                print(Snake, end="")
                continue
            if isTailPos(x,y):
                print(Tail, end="")
                continue
            if x == Food_Position[0] and y == Food_Position[1]:
                print(Food, end="")
                continue
            if x %  2 == 0 and y % 2 == 0 or x == 0 or x == Width+1 or y == 0  or y == Height+1:
                print(Block, end="")
            else:
                print(Blank, end="")
        print("")

def GameOverCheck():
    x = Snake_Position[0]
    y = Snake_Position[1]
    CheckPos = [[x+1,y], [x-1,y], [x,y+1], [x,y-1]]

    blockedPoint = 0
    for p in CheckPos:
        isBlock = p[0] % 2 != 0 and p[1] % 2 != 0
        isTail = p in Tail_Positions
        if isBlock or isTail:
            blockedPoint += 1
    GameOver = blockedPoint >= 4
    if GameOver:
        os.system('cls')
        print("Game Over!")

def Move(x, y):
    lastPosX = Snake_Position[0]
    lastPosY = Snake_Position[1]
    Snake_Position[0] += x
    Snake_Position[1] += y

    if Snake_Position[0] == 0:
        Snake_Position[0] = Width
    if Snake_Position[0] == Width+1:
        Snake_Position[0] = 1
    if Snake_Position[1] == 0:
        Snake_Position[1] = Height
    if Snake_Position[1] == Height + 1:
        Snake_Position[1] = 1
    if Snake_Position[0] % 2 == 0 and Snake_Position[1] % 2 == 0:
        Snake_Position[0] = lastPosX
        Snake_Position[1] = lastPosY
    else:
        if len(Tail_Positions) > 0:
            Tail_Positions.insert(0, [lastPosX, lastPosY])
            Tail_Positions.pop(len(Tail_Positions) - 1)
    

def CheckEatFood():
    if Snake_Position[0] == Food_Position[0] and Snake_Position[1] == Food_Position[1]:
        if len(Tail_Positions) > 0:
            Tail_Positions.insert(len(Tail_Positions) - 1, Tail_Positions[len(Tail_Positions) - 1])
        else:
            Tail_Positions.append(Snake_Position)
        RandomizeFoodPos()
def Control():

    Valid = False
    while Valid == False:
        nav_Dir = str(input(""))
        if nav_Dir.upper() == "D":
            Move(1,0)
            Valid = True
        if nav_Dir.upper() == "A":
            Move(-1,0)
            Valid = True
        if nav_Dir.upper() == "S":
            Move(0,1)
            Valid = True
        if nav_Dir.upper() == "W":
            Move(0,-1)
            Valid = True


RandomizeFoodPos()
while GameOver == False:
    ReDraw()
    Control()
    CheckEatFood()
    GameOverCheck()

#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor)
from pybricks.parameters import Port, Color
from rubikscolorresolver.solver import resolve_colors
import time

ev3 = EV3Brick()

ev3.light.on(Color.RED)
ev3.screen.clear()
ev3.screen.draw_text(x=50, y=50, text="Starting")

frontMotor = Motor(Port.A)
backMotor = Motor(Port.B)
leftMotor = Motor(Port.C)
rightMotor = Motor(Port.D)

button = TouchSensor(Port.S1)
sensor = ColorSensor(Port.S2)

i = 0
color = Color.WHITE
color = []

# In progress

# while i < 54:
#     while not button.pressed():
#         color = sensor.color()

#         if color != None:
#             ev3.screen.clear()
#             ev3.screen.draw_text(x=50, y=75, text=("%d/54" % i))
#             if color == Color.GREEN:
#                 ev3.screen.draw_text(x=50, y=50, text="GREEN")
#             elif color == Color.RED:
#                 ev3.screen.draw_text(x=50, y=50, text="RED")
#             elif color == Color.BLUE:
#                 ev3.screen.draw_text(x=50, y=50, text="BLUE")
#             elif color == Color.WHITE:
#                 ev3.screen.draw_text(x=50, y=50, text="WHITE")
#             elif color == Color.YELLOW:
#                 ev3.screen.draw_text(x=50, y=50, text="YELLOW")
#             elif color == Color.BLACK:
#                 ev3.screen.draw_text(x=50, y=50, text="ORANGE")
#         else:
#             ev3.screen.clear()
#             ev3.screen.draw_text(x=50, y=50, text=("%d/54" % i))
#         time.sleep(0.5)
    
#     if color != None:
#         i = i+1
#         ev3.speaker.beep(frequency=300)
#     else:
#         ev3.speaker.beep(frequency=100)
#     time.sleep(0.1)
# cube = Cube("WWWWWWWWWGGGRRRBBBOOOOOOGGGRRRBBBOOOGGGRRRBBBYYYYYYYYY")

solve = resolve_colors("cube.txt")

scramble = solve

movesList = scramble.split(" ")

count = 0
moves = []

while count < len(movesList):
    item = movesList[count]
    item2 = movesList[count+1]
    item3 = "X"
    if count+2 < len(movesList):
        item3 = movesList[count+2]

    if ((item == item2) and (item2 == item3)):
        moves.append(item+"'")
        count = count+3
    elif ((item == item2) and (item2 != item3)):
        moves.append(item+"2")
        count = count+2
    elif ((item != item2) and (item2 == item3)):
        moves.append(item)
        count = count+1
    elif ((item != item2) and (item2 != item3)):
        moves.append(item)
        count = count+1

while not button.pressed():
    ev3.screen.clear()
    ev3.screen.draw_text(x=50, y=50, text="Place the Cube")
    time.sleep(0.1)

for move in moves:
    ev3.light.on(Color.ORANGE)
    ev3.screen.clear()
    ev3.screen.draw_text(x=50, y=50, text="Resolution")

    fA = frontMotor.angle()
    rA = rightMotor.angle()
    bA = backMotor.angle()
    lA = leftMotor.angle()

    if move == "F":
        frontMotor.run_target(1000, fA+90)
    if move == "F'":
        frontMotor.run_target(1000, fA-90)
    if move == "F2":
        frontMotor.run_target(1000, fA+180)
    if move == "F2'":
        frontMotor.run_target(1000, fA+-180)
      
    if move == "R":
        rightMotor.run_target(1000, rA-90)
    if move == "R'":
        rightMotor.run_target(1000, rA+90)
    if move == "R2":
        rightMotor.run_target(1000, rA-180)
    if move == "R2'":
        rightMotor.run_target(1000, rA+180)
      
    if move == "B":
        backMotor.run_target(1000, bA+90)
    if move == "B'":
        backMotor.run_target(1000, bA-90)
    if move == "B2":
        backMotor.run_target(1000, bA+180)
    if move == "B2'":
        backMotor.run_target(1000, bA-180)
      
    if move == "L":
        leftMotor.run_target(1000, lA-90)
    if move == "L'":
        leftMotor.run_target(1000, lA+90)
    if move == "L2":
        leftMotor.run_target(1000, lA-180)
    if move == "L2'":
        leftMotor.run_target(1000, lA+180)

    # The U and D movements are not present because the EV3 can only support 4 motors while the cube requires 6.

ev3.light.on(Color.GREEN)
ev3.screen.clear()
ev3.screen.draw_text(x=50, y=50, text="Resolved")
ev3.speaker.beep()

time.sleep(3)
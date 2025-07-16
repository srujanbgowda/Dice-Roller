from vpython import *
import random 
import time

scene.title = "3D Dice Roller"
scene.background = color.gray(0.2)
scene.center = vector(0, 0, 0)
scene.center = vector(-1,-1,-1)

die = box(size=vector(2,2,2),color=color.white,opacity=1)

abels = [
    label(pos=vector(0, 0, 1.1), text='1', height=0.8, box=False, color=color.black),
    label(pos=vector(0, 0, -1.1), text='6', height=0.8, box=False, color=color.black),
    label(pos=vector(1.1, 0, 0), text='3', height=0.8, box=False, color=color.black),
    label(pos=vector(-1.1, 0, 0), text='4', height=0.8, box=False, color=color.black),
    label(pos=vector(0, 1.1, 0), text='5', height=0.8, box=False, color=color.black),
    label(pos=vector(0, -1.1, 0), text='2', height=0.8, box=False, color=color.black)
]

def roll_die():
    for i in range(30):
        rate(30)
        die.rotate(angle=pi/8, axis=vector(random.random(), random.random(), random.random()))
    result = random.randint(1, 6)
    print(f"\n🎲 You rolled a {result}!\n")
    return result

# Main loop
while True:
    input("Press ENTER to roll the die...")
    roll_die()
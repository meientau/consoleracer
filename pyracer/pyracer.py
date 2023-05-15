#!/bin/python
import shutil, random, time, keyboard

car = "#"
left = "<"
right = ">"
consolewidth = shutil.get_terminal_size().columns
roadwidth = 30
roadx = (consolewidth - roadwidth - 3) // 2
bendx = 0
carx = consolewidth // 2
directions = { 'a': -1, 'd': 1 }

def keydirection():
    key = keyboard.getkey()
    if not key or key not in directions:
        return 0

    return directions[key]

def limit(value, mini, maxi):
    return max(mini, min(maxi, value))

orig_settings = None
try:
    orig_settings = keyboard.configure()
    while True:
        carx = limit(carx + keydirection(), roadx, roadx + roadwidth + 2)
        bendx = limit(bendx + random.uniform(-0.5, 0.5), -1, 1)
        roadx = limit(roadx + bendx, 0, consolewidth - roadwidth - 3)

        # .........left...........car.....................right......
        # ............<............#......................>..........
        # <- iroadx -> <- offset -> <- roadwidth-offset -> <- rest ->
        iroadx = round(roadx)
        offset = carx - iroadx - 1

        if not -1 < offset < roadwidth:
            break

        print((" "*iroadx)+left+(" "*offset)+car+(" "*(roadwidth - offset - 1))+right)
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Byeee!")
finally:
    if orig_settings:
        keyboard.restore(orig_settings)

boom = ["  ** * ** * **  ", "** * Booom! * **", "  ** * ** * **  "]
boomlen = len(boom[0])
indent = limit(int(carx - boomlen // 2), 0, consolewidth - boomlen)
for line in boom:
    print((" "*indent) + line)

# Idea: after some time, increase the difficulty
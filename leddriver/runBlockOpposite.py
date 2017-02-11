#!/usr/bin/python3
import colorschemes
import sys
from apa102 import colorRef
args = sys.argv

if args[1].startswith("0x"): # base 16
    ledColor = int(args[1][2:],16)
else: # base 10
    ledColor = colorRef.colors[args[1]]
barLength = int(args[2])

numLEDs = 420

print("block chase oposite")
myCycle = colorschemes.blockChaseOpposite(numLEDs=numLEDs, pauseValue=0.00, numStepsPerCycle = 50*numLEDs, numCycles = 150, globalBrightness=30, barLength = barLength, ledColor = ledColor)
myCycle.start()

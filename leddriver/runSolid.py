#!/usr/bin/python3
import colorschemes
import sys
from apa102 import colorRef
args = sys.argv

if args[1].startswith("0x"): # base 16
    ledColor = int(args[1][2:],16)
else: # base 10
    ledColor = colorRef.colors[args[1]]

A=ledColor
B = int(args[2])
numLEDs = 420 

# One Cycle with one step and a pause of one second. Hence one second of white light
#print("solid")
myCycle = colorschemes.SolidColor(numLEDs=numLEDs, pauseValue=10, numStepsPerCycle = 100, numCycles = 100,ledColor = A,globalBrightness = B)
myCycle.start()

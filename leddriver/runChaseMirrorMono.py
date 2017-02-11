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

pauseVal = int(args[3])/100

numLEDs = 420

print("theatre chase mirror mono")
myCycle = colorschemes.TheaterChaseMirrorMono(numLEDs=numLEDs, \
                                              pauseValue=pauseVal, \
                                              numStepsPerCycle = 7*50, \
                                              numCycles = 150, \
                                              globalBrightness=30, \
                                              barLength=barLength, \
                                              ledColor=ledColor)
myCycle.start()

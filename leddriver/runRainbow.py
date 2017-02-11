#!/usr/bin/python3
import colorschemes
import sys

numLEDs = 420

print("slow rainbow")
myCycle = colorschemes.Rainbow2(numLEDs=numLEDs, pauseValue=0, numStepsPerCycle = 255, numCycles = 1000, globalBrightness=30)
myCycle.start()

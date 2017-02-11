import colorschemes
import sys

numLEDs = 420 

# One Cycle with one step and a pause of one second. Hence one second of white light
#print("solid")
myCycle = colorschemes.SolidColor(numLEDs=numLEDs, pauseValue=0, numStepsPerCycle = 1, numCycles = 1, ledColor = 0x0000FF)
myCycle.start()
myCycle = colorschemes.SolidColor(numLEDs=numLEDs, pauseValue=0, numStepsPerCycle = 1, numCycles = 1, ledColor = 0x000000)
myCycle.start()

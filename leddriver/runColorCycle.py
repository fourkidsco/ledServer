#!/usr/bin/python3
import colorschemes
import sys

numLEDs = 420

# One Cycle with one step and a pause of one second. Hence one second of white light
print("solid")
myCycle = colorschemes.SolidColor(numLEDs=numLEDs, pauseValue=2, numStepsPerCycle = 1, numCycles = 1,globalBrightness = 30,ledColor = 0xFFFFFF )
myCycle.start()
# Go twice around the clock
#print("roundandround")
#myCycle = colorschemes.RoundAndRound(numLEDs=numLEDs, pauseValue=0, numStepsPerCycle = numLEDs, numCycles = 2)
#myCycle.start()
# One cycle of red, green and blue each
#print("redgreenblue")
#myCycle = colorschemes.StrandTest2(numLEDs=numLEDs, pauseValue=0.5, numStepsPerCycle = numLEDs, numCycles = 3, globalBrightness=10)
#myCycle.start()
# Two slow trips through the rainbow
print("slow rainbow")
myCycle = colorschemes.Rainbow(numLEDs=numLEDs, pauseValue=0, numStepsPerCycle = 255, numCycles = 100, globalBrightness=30)
myCycle.start()
print("slow rainbow")
myCycle = colorschemes.Rainbow2(numLEDs=numLEDs, pauseValue=0, numStepsPerCycle = 255, numCycles = 100, globalBrightness=30)
myCycle.start()
# Five quick trips through the rainbow
print("theatre chase")
myCycle = colorschemes.TheaterChaseMono(numLEDs=numLEDs, pauseValue=0.05, numStepsPerCycle = 735, numCycles = 150, globalBrightness=30,ledColor=0xFF0000)
myCycle.start()
print("theatre chase")
myCycle = colorschemes.TheaterChaseMono(numLEDs=numLEDs, pauseValue=0.05, numStepsPerCycle = 735, numCycles = 150, globalBrightness=30,ledColor=0x00FF00)
myCycle.start()
print("theatre chase")
myCycle = colorschemes.TheaterChaseMono(numLEDs=numLEDs, pauseValue=0.05, numStepsPerCycle = 735, numCycles = 150, globalBrightness=30,ledColor=0x0000FF)
myCycle.start()
#
print("theatre chase mirror")
myCycle = colorschemes.TheaterChaseMirror(numLEDs=numLEDs, pauseValue=0.05, numStepsPerCycle = 7*50, numCycles = 150, globalBrightness=30)
myCycle.start()
#
print("block chase")
myCycle = colorschemes.blockChase(numLEDs=numLEDs, pauseValue=0.0, numStepsPerCycle = 50*420, numCycles = 150, globalBrightness=10,barLength=50)
myCycle.start()
#
print("block chase oposite")
myCycle = colorschemes.blockChaseOpposite(numLEDs=numLEDs, pauseValue=0.00, numStepsPerCycle = 50*420, numCycles = 150, globalBrightness=30, barLength = 60)
myCycle.start()
#
print("ryellow fade")
myCycle = colorschemes.oneColorFade(numLEDs=numLEDs, pauseValue=0.05, numStepsPerCycle = 511, numCycles = 150, globalBrightness=30)
myCycle.start()

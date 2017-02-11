from colorcycletemplate import ColorCycleTemplate
def rotate(lst,n):
    return lst[-n:] + lst[:-n]

class blockChase(ColorCycleTemplate):
    def update(self, strip, numLEDs, numStepsPerCycle, currentStep, currentCycle):
        colorIndex = 0x0000FF #strip.wheel(int(round(255/numStepsPerCycle * currentStep, 0)))
        pixList = [0x00FF00 for i in range(numLEDs)]
        blockLen = self.barLength
        for i in range(blockLen):
            indx = (i+currentStep) % numLEDs
            #indx = (i+currentStep) % self.barLength
            #print(indx)
            pixList[indx] = colorIndex 
        #print(pixList)
        for pixel in range(numLEDs):
            strip.setPixelRGB(pixel, pixList[pixel])
        return 1

class blockChaseOpposite(ColorCycleTemplate):
    def update(self, strip, numLEDs, numStepsPerCycle, currentStep, currentCycle):
        colorIndex1 = self.ledColor
        #colorIndex2 = 0x0000FF
        colorIndex2 = colorIndex1
        pixList1 = [0x000000 for i in range(numLEDs)]
        pixList2 = [0x000000 for i in range(numLEDs)]
        blockLen = self.barLength
        for i in range(blockLen):
            indx = (i+currentStep) % numLEDs
            pixList1[indx] = colorIndex1
            pixList2[indx] = colorIndex2
        revPixList2 = list(reversed(pixList2))
        #print(pixList)
        newPixList2 = []
        newPixList2.extend(revPixList2)
        #print(pixList1)
        #print(newPixList2)
        for pixel in range(numLEDs):
            strip.setPixelRGB(pixel, pixList1[pixel] + newPixList2[pixel])
        return 1
    
class oneColorFade(ColorCycleTemplate):
    def update(self, strip, numLEDs, numStepsPerCycle, currentStep, currentCycle):
        colorIndex = abs(0xFF - currentStep)
        
        newColorIndex = colorIndex<<16 ^ colorIndex<<8
        pixList = [newColorIndex for i in range(numLEDs)]
        for i in range(numLEDs):
            strip.setPixelRGB(i,pixList[i])
        return 1
        
class StrandTest(ColorCycleTemplate):
    def init(self, strip, numLEDs):
        self.color = 0x000000  # Initialize with black

    def update(self, strip, numLEDs, numStepsPerCycle, currentStep, currentCycle):
        # One cycle = The 9 Test-LEDs wander through numStepsPerCycle LEDs.
        if (currentStep == 0): self.color >>= 8  # Red->green->blue->black
        if (self.color == 0): self.color = 0xFF0000  # If black, reset to red

        head = (currentStep + 9) % numStepsPerCycle # The head pixel that will be turned on in this cycle
        print(str(head) + ',' + str(currentStep))
        tail = currentStep # The tail pixel that will be turned off
        strip.setPixelRGB(head, self.color)  # Paint head
        strip.setPixelRGB(tail, 0)  # Clear tail

        return 1 # Repaint is necessary
    
class StrandTest2(ColorCycleTemplate):
    def init(self, strip, numLEDs):
        self.color = 0x000000  # Initialize with black

    def update(self, strip, numLEDs, numStepsPerCycle, currentStep, currentCycle):
        # One cycle = The 9 Test-LEDs wander through numStepsPerCycle LEDs.
        if (currentStep == 0): self.color >>= 8  # Red->green->blue->black
        if (self.color == 0): self.color = 0xFF0000  # If black, reset to red
        for i in range(numLEDs):
            print(i)
            strip.setPixelRGB(i, self.color)  # Paint head
        for i in range(numLEDs):
            strip.setPixelRGB(i, 0)  # Clear tail

        return 1 # Repaint is necessary


class TheaterChase(ColorCycleTemplate):
    def update(self, strip, numLEDs, numStepsPerCycle, currentStep, currentCycle):
        # One cycle = One thrip through the color wheel, 0..254
        # Few cycles = quick transition, lots of cycles = slow transition
        # Note: For a smooth transition between cycles, numStepsPerCycle must be a multiple of 7
        startIndex = currentStep % 7 # Each segment is 7 dots long: 2 blank, and 5 filled
        colorIndex = strip.wheel(int(round(255/numStepsPerCycle * currentStep, 0)))
        #pixList = []
        for pixel in range(numLEDs):
            # Two LEDs out of 7 are blank. At each step, the blank ones move one pixel ahead.
            if ((pixel+startIndex) % 7 == 0) or ((pixel+startIndex) % 7 == 1): 
                strip.setPixelRGB(pixel, 0)
                #pixList.append(0)
            else: 
                strip.setPixelRGB(pixel, colorIndex)
                #print(type(pixel))
                #print(type(colorIndex))
                #pixList.append(colorIndex)
        #print(pixList)
        return 1

class TheaterChaseMirror(ColorCycleTemplate):
    def update(self, strip, numLEDs, numStepsPerCycle, currentStep, currentCycle):
        blockLen = self.barLength
        # One cycle = One thrip through the color wheel, 0..254
        # Few cycles = quick transition, lots of cycles = slow transition
        # Note: For a smooth transition between cycles, numStepsPerCycle must be a multiple of 7
        startIndex = currentStep % blockLen # Each segment is 7 dots long: 2 blank, and 5 filled
        colorIndex = strip.wheel(int(round(255/numStepsPerCycle * currentStep, 0)))
        pixList = []
        for pixel in range(int(numLEDs/2)):
            if ((pixel+startIndex) % blockLen == 0) or ((pixel+startIndex) % blockLen == 1): pixList.append(0)
            else: pixList.append(colorIndex)
        revPixList = list(reversed(pixList))
        allPixList = list()
        allPixList.extend(pixList)
        allPixList.extend(revPixList)
        for pixel in range(numLEDs):
            # Two LEDs out of 7 are blank. At each step, the blank ones move one pixel ahead.
            strip.setPixelRGB(pixel, allPixList[pixel])
            #print(str(pixel) + ',' + str(currentStep) + ',' + str(currentCycle))
        return 1

class TheaterChaseMirrorMono(ColorCycleTemplate):
    def update(self, strip, numLEDs, numStepsPerCycle, currentStep, currentCycle):
        blockLen = self.barLength
        # One cycle = One thrip through the color wheel, 0..254
        # Few cycles = quick transition, lots of cycles = slow transition
        # Note: For a smooth transition between cycles, numStepsPerCycle must be a multiple of 7
        startIndex = currentStep % blockLen # Each segment is 7 dots long: 2 blank, and 5 filled
        colorIndex = self.ledColor #strip.wheel(int(round(255/numStepsPerCycle * currentStep, 0)))
        pixList = []
        for pixel in range(int(numLEDs/2)):
            if ((pixel+startIndex) % blockLen == 0) or ((pixel+startIndex) % blockLen == 1): pixList.append(0)
            else: pixList.append(colorIndex)
        revPixList = list(reversed(pixList))
        allPixList = list()
        allPixList.extend(pixList)
        allPixList.extend(revPixList)
        for pixel in range(numLEDs):
            # Two LEDs out of 7 are blank. At each step, the blank ones move one pixel ahead.
            strip.setPixelRGB(pixel, allPixList[pixel])
            #print(str(pixel) + ',' + str(currentStep) + ',' + str(currentCycle))
        return 1
    
class TheaterChaseMono(ColorCycleTemplate):
    def update(self, strip, numLEDs, numStepsPerCycle, currentStep, currentCycle):
        # One cycle = One thrip through the color wheel, 0..254
        # Few cycles = quick transition, lots of cycles = slow transition
        # Note: For a smooth transition between cycles, numStepsPerCycle must be a multiple of 7
        startIndex = currentStep % 7 # Each segment is 7 dots long: 2 blank, and 5 filled
        colorIndex = self.ledColor
        for pixel in range(numLEDs):
        	  # Two LEDs out of 7 are blank. At each step, the blank ones move one pixel ahead.
            if ((pixel+startIndex) % 7 == 0) or ((pixel+startIndex) % 7 == 1): strip.setPixelRGB(pixel, 0)
            else: strip.setPixelRGB(pixel, colorIndex)
        return 1

class RoundAndRound(ColorCycleTemplate):

    def init(self, strip, numLEDs):
        strip.setPixelRGB(0, 0xFF0000);
        strip.setPixelRGB(1, 0x00FF00);

    def update(self, strip, numLEDs, numStepsPerCycle, currentStep, currentCycle):
        # Simple class to demonstrate the "rotate" method
        strip.rotate()
        return 1


class SolidColor(ColorCycleTemplate):

    def init(self, strip, numLEDs):
    	  for led in range(0, numLEDs):
    	  	  strip.setPixelRGB(led,self.ledColor) # Paint black 

    def update(self, strip, numLEDs, numStepsPerCycle, currentStep, currentCycle):
    	  # Do nothing: Init lit the strip, and update just keeps it this way
    	  return 0


class Rainbow(ColorCycleTemplate):
    def update(self, strip, numLEDs, numStepsPerCycle, currentStep, currentCycle):
        # One cycle = One thrip through the color wheel, 0..254
        # Few cycles = quick transition, lots of cycles = slow transition
        # -> LED 0 goes from index 0 to 254 in numStepsPerCycle cycles. So it might have to step up
        #     more or less than one index depending on numStepsPerCycle.
        # -> The other LEDs go up to 254, then wrap arount to zero and go up again until the last one is just
        #     below LED 0. This way, the strip always shows one full rainbow, regardless of the number of LEDs
        scaleFactor = 255 / numLEDs # Value for the index change between two neighboring LEDs
        startIndex = 255 / numStepsPerCycle * currentStep # Value of LED 0
        for i in range(numLEDs):
            ledIndex = startIndex + i * scaleFactor # Index of LED i, not rounded and not wrapped at 255
            ledIndexRoundedAndWrappedAround = int(round(ledIndex, 0)) % 255 # Now rounded and wrapped
            pixelColor = strip.wheel(ledIndexRoundedAndWrappedAround) # Get the actual color out of the wheel
            strip.setPixelRGB(i, pixelColor);
        return 1 # All pixels are set in the buffer, so repaint the strip now

class Rainbow2(ColorCycleTemplate):
    def update(self, strip, numLEDs, numStepsPerCycle, currentStep, currentCycle):
        # One cycle = One trip through the color wheel, 0..254
        # Few cycles = quick transition, lots of cycles = slow transition
        # -> LED 0 goes from index 0 to 254 in numStepsPerCycle cycles. So it might have to step up
        #     more or less than one index depending on numStepsPerCycle.
        # -> The other LEDs go up to 254, then wrap arount to zero and go up again until the last one is just
        #     below LED 0. This way, the strip always shows one full rainbow, regardless of the number of LEDs
        mf = 5.1 
        sc = 255*mf
        
        scaleFactor = 510 / numLEDs # Value for the index change between two neighboring LEDs
        startIndex = 255 / numStepsPerCycle * currentStep # Value of LED 0
        for i in range(numLEDs):
            ledIndex = startIndex + i * scaleFactor # Index of LED i, not rounded and not wrapped at 255
            ledIndexRoundedAndWrappedAround = int(round(ledIndex, 0)) % 255 # Now rounded and wrapped
            pixelColor = strip.wheel(ledIndexRoundedAndWrappedAround) # Get the actual color out of the wheel
            strip.setPixelRGB(i, pixelColor);
        return 1 # All pixels are set in the buffer, so repaint the strip now

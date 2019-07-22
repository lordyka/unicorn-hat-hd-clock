#!/usr/bin/env python

import time
import datetime

try:
    import unicornhathd as unicorn
    print("unicorn hat hd detected")
except ImportError:
    from unicorn_hat_sim import unicornhathd as unicorn

unicorn.rotation(90)
unicorn.brightness(0.1)

ifvar = 1

def changestate(x)
  global ifvar
  if x == 1:
    ifvar = 1
  if x == 0:
    ifvar = 0

# Composition methods
def fullLine(start, row):
  for x in range(start, start+7):
    unicorn.set_pixel(x, row, 255, 255, 255)

def bothSides(start, row):
  unicorn.set_pixel(start, row, 255, 255, 255)
  unicorn.set_pixel(start+6, row, 255, 255, 255)

def leftSide(start, row):
  unicorn.set_pixel(start, row, 255, 255, 255)

def rightSide(start, row):
  unicorn.set_pixel(start+6, row, 255, 255, 255)

# Numbers
def displayZero(x, y):
  clearNumberPixels(x, y)
  fullLine(x, y)
  bothSides(x, y-1)
  bothSides(x, y-2)
  bothSides(x, y-3)
  bothSides(x, y-4)
  bothSides(x, y-5)
  fullLine(x, y-6)
  unicorn.show()

def displayOne(x, y):
  clearNumberPixels(x, y)
  rightSide(x, y)
  rightSide(x, y-1)
  rightSide(x, y-2)
  rightSide(x, y-3)
  rightSide(x, y-4)
  rightSide(x, y-5)
  rightSide(x, y-6)
  unicorn.show()

def displayTwo(x, y):
  clearNumberPixels(x, y)
  fullLine(x, y)
  rightSide(x, y-1)
  rightSide(x, y-2)
  fullLine(x, y-3)
  leftSide(x, y-4)
  leftSide(x, y-5)
  fullLine(x, y-6)
  unicorn.show()

def displayThree(x, y):
  clearNumberPixels(x, y)
  fullLine(x, y)
  rightSide(x, y-1)
  rightSide(x, y-2)
  fullLine(x, y-3)
  rightSide(x, y-4)
  rightSide(x, y-5)
  fullLine(x, y-6)
  unicorn.show()

def displayFour(x, y):
  clearNumberPixels(x, y)
  bothSides(x, y)
  bothSides(x, y-1)
  bothSides(x, y-2)
  fullLine(x, y-3)
  rightSide(x, y-4)
  rightSide(x, y-5)
  rightSide(x, y-6)
  unicorn.show()

def displayFive(x, y):
  clearNumberPixels(x, y)
  fullLine(x, y)
  leftSide(x, y-1)
  leftSide(x, y-2)
  fullLine(x, y-3)
  rightSide(x, y-4)
  rightSide(x, y-5)
  fullLine(x, y-6)
  unicorn.show()

def displaySix(x, y):
  clearNumberPixels(x, y)
  fullLine(x, y)
  leftSide(x, y-1)
  leftSide(x, y-2)
  fullLine(x, y-3)
  bothSides(x, y-4)
  bothSides(x, y-5)
  fullLine(x, y-6)
  unicorn.show()

def displaySeven(x, y):
  clearNumberPixels(x, y)
  fullLine(x, y)
  rightSide(x, y-1)
  rightSide(x, y-2)
  rightSide(x, y-3)
  rightSide(x, y-4)
  rightSide(x, y-5)
  rightSide(x, y-6)
  unicorn.show()

def displayEight(x, y):
  clearNumberPixels(x, y)
  fullLine(x, y)
  bothSides(x, y-1)
  bothSides(x, y-2)
  fullLine(x, y-3)
  bothSides(x, y-4)
  bothSides(x, y-5)
  fullLine(x, y-6)
  unicorn.show()

def displayNine(x, y):
  clearNumberPixels(x, y)
  fullLine(x, y)
  bothSides(x, y-1)
  bothSides(x, y-2)
  fullLine(x, y-3)
  rightSide(x, y-4)
  rightSide(x, y-5)
  fullLine(x, y-6)
  unicorn.show()

def displayNumber(x,y, number):
  if number == 0:
    displayZero(x,y)
  elif number == 1:
    displayOne(x,y)
  elif number == 2:
    displayTwo(x,y)
  elif number == 3:
    displayThree(x,y)
  elif number == 4:
    displayFour(x,y)
  elif number == 5:
    displayFive(x,y)
  elif number == 6:
    displaySix(x,y)
  elif number == 7:
    displaySeven(x,y)
  elif number == 8:
    displayEight(x,y)
  elif number == 9:
    displayNine(x,y)

# Clears the pixels in a rectangle. x,y is the top left corner of the rectangle
# and its dimensions are 7X7
def clearNumberPixels(x, y):
  for y1 in range(y, y-7, -1):
    for x1 in range(x, x+7):
      # print("x1 = "+str(x1)+" y1 = "+str(y1))
      unicorn.set_pixel(x1, y1, 0, 0, 0)
  unicorn.show()



# Gets a specific part of the current time, passed to strftime, then it is
# split into its individual numbers and converted into integers. Used to feed
# the display with numbers

def getTimeParts(timePart):
  parts = datetime.datetime.now().strftime(timePart)
  return [int(x) for x in parts]  

displayedHourParts = getTimeParts('%H')
displayedMinuteParts = getTimeParts('%M')

# Display Current Time
displayNumber(0,15, displayedHourParts[0])
displayNumber(8,15, displayedHourParts[1])
displayNumber(0,6, displayedMinuteParts[0])
displayNumber(8,6, displayedMinuteParts[1])


try:
  while True:
    if ifvar == 1:
      hourParts = getTimeParts('%H')
      minuteParts = getTimeParts('%M')
    
      # TIME Details
      # Only update first hour number if it is different to what is currently displayed
      if hourParts[0] != displayedHourParts[0]:
        displayedHourParts[0] = hourParts[0]
        displayNumber(0,15, hourParts[0])

      # Only update second hour number if it is different to what is currently displayed
      if hourParts[1] != displayedHourParts[1]:
        displayedHourParts[1] = hourParts[1]
        displayNumber(8,15, hourParts[1])

      # Only update first minute number if it is different to what is currently displayed
      if minuteParts[0] != displayedMinuteParts[0]:
        displayedMinuteParts[0] = minuteParts[0]
        displayNumber(0,6, minuteParts[0])

      # Only update second minute number if it is different to what is currently displayed
      if minuteParts[1] != displayedMinuteParts[1]:
        displayedMinuteParts[1] = minuteParts[1]
        displayNumber(8,6, minuteParts[1])

      # Sleep for 0.5 because the display doesn't need to update that often
      time.sleep(1)
    else:
      unicorn.off()
      time.sleep(1)
except KeyboardInterrupt:
  unicorn.off()

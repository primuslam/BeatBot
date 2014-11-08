# Test of PyMyo - same functionality as hello-myo.exe
# Paul Lutz
# Scott Martin

from myo import Myo
import sys
import time
import serial
import math
import Beats

data = []
extremes = []
prev = [0, 0, 0, 0, 0]

def ismax(prev): #Prev is a list with odd # of elements
  # print(prev)
  l = len(prev)
  for i in range(l //2):
    if prev[i] > prev[i + 1] or prev[l - 1 - i] >= prev[l -2 -1] :
      return False
  return True

def ismin(prev):
  l = len(prev)
  for i in range(l //2):
    if prev[i] < prev[i + 1] or prev[l - 1 - i] <= prev[l -2 -1] :
      return False
  return True

def update(prev, val):
  for i in range(len(prev) - 1):
    prev[i] = prev[i+1]
  prev[-1] = val
  # print("updated"+str(prev))


drumbeat = Beats.Beat(Beats.Beat.beat2)
i = 0
temp = 0
ser  = serial.Serial(2)
def printData(myo):
  global i
  global last_pose, temp
  (roll, pitch, yaw) = myo.getRotationScaled(2*math.pi)
  temp, param = pitch, pitch-temp
  
  if ismax(prev) or ismin(prev):
    ser.write(drumbeat.next_beat())

  update(prev, temp)
  i += 1
  # Print out the rotation and arm state on the same line each update
  # print '\r{:17s}'.format('*'*int(param/10))
 
def main():
  myMyo = Myo(callback=printData)
  myMyo.daemon = True
  myMyo.start()
  raw_input("Press enter to exit")
  print("END")
  print(data)
  print(extremes)   
  ser.close()
if __name__ == "__main__":
    main()
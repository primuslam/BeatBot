# Test of PyMyo - same functionality as hello-myo.exe
# Paul Lutz
# Scott Martin

from myo import Myo
import sys
import time
import serial
import math
import Beats

def ismax(prev, k = 1):
  l = len(prev)
  for i in range(l-(1+k)):
    if prev[i] >= prev[-(1+k)]:
      return False
  for i in range(k):
    if prev[-(1+k)] < prev[-(k-i)]:
      return False
  return True

def ismin(prev, k = 1):
  l = len(prev)
  for i in range(l-(1+k)):
    if prev[i] <= prev[-(1+k)]:
      return False
  for i in range(k):
    if prev[-(1+k)] > prev[-(k-i)]:
      return False
  return True

def update(prev, val):
  for i in range(len(prev) - 1):
    prev[i] = prev[i+1]
  prev[-1] = val
  # print("updated"+str(prev))

def find_tempo(extremes):
  return sum([extremes[-(i+1)] - extremes[-(i+2)]  for i in range(4)])/16

i, j = 0, 0
drumbeat = Beats.Beat(Beats.Beat.beat2)
ser  = serial.Serial(2)
prev = [9, 9, 9, 9, 9, 9, 9, 9, 9]
downstrokes = [0, 0, 0, 0, 0]
tempo = 0
def printData(myo):
  global tempo
  global i, j
  (roll, pitch, yaw) = myo.getRotationScaled(2*math.pi)
  (ax, ay, az) = myo.getAcceleration()
  param = (1 + ax + pitch/3)
  string = str(param)+'*'*int(param* 10)


  if ismax(prev, 2):
    ser.write(drumbeat.next_beat())
    downstrokes.append(i)
    j = 0
    tempo = find_tempo(downstrokes)
    string += "MAX"
  else: 
    if ismin(prev, 2):
      ser.write(drumbeat.next_beat())
      string += "MIN"
    if (j == tempo):
      ser.write(drumbeat.next_beat())  

  print(string)
  i, j = i + 1, j + 1
  update(prev, param)
 
def main():
  myMyo = Myo(callback=printData)
  myMyo.daemon = True
  myMyo.start()
  raw_input("Press enter to exit")
  print("END")
  print(prev)
  ser.close()

if __name__ == "__main__":
    main()
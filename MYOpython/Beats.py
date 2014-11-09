import Sound
import time

class Beat:
  beat1 = ["110", "000", "100", "000", "101", "000", "100", "000",
          "110", "000", "110", "000", "101", "000", "100", "000"]
  beat2 = ["110", "000", "100", "000", "101", "000", "100", "000"]
  beat3 = ["110", "000", "100", "000", "101", "000", "100", "000",
          "110", "000", "110", "000", "101", "000", "100", "001"]
  beat4 = ["110", "000", "100", "000", "101", "000", "100", "000",
          "110", "000", "100", "000", "101", "000", "110", "000"]
  beat5 = ["110", "100", "100", "110", "101", "100", "100", "100",
          "100", "110", "100", "110", "101", "100", "100", "100"]
  beat6 = ["110", "100", "100", "100", "100", "100", "100", "110"]
  def __init__(self, pattern):
    self.pattern = pattern
  def next_beat(self):
    note = self.pattern.pop(0)
    self.pattern += [note]
    return note

def loop(beat):
  k = 0
  a = Beat(beat)
  for i in range(32):
    n = a.pattern.pop(0)
    print(n)
    Sound.play(n)
    a.pattern.append(n)
    for j in range(1000000):
      k += 10
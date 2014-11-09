import pyglet

snare = pyglet.media.load("../sound/snare.aif", streaming=False)
kick = pyglet.media.load("../sound/kick.aif", streaming=False)
hihat = pyglet.media.load("../sound/hihat.aif", streaming=False)

def play(inputcode):
  if inputcode[0] == '1':
    hihat.play()
  if inputcode[1] == '1':
    kick.play()
  if inputcode[2] == '1':
    snare.play()
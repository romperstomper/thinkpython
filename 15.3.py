
import sys
import copy

class Rect():
  def __init__(self, origin=(0,0), acorner=(0,0), bcorner=(3,3)):
    self.origin = origin
    self.acorner = acorner
    self.bcorner = bcorner

  def move_rect(self, a):
    newrec = copy.deepcopy(a)
    return newrec


def main():
  rec = Rect() 
  newrect = rec.move_rect(rec)
  print newrect.acorner, newrect.bcorner


if __name__ == '__main__':
  main()

import sys


a= sys.argv[1]
b= sys.argv[2]

class Rect():
  def __init__(self, origin=(0,0), acorner=(0,0), bcorner=(3,3)):
    self.origin = origin
    self.acorner = acorner
    self.bcorner = bcorner

  def move_rect(self, a, b):
    self.acorner = (self.acorner[0] + int(a), self.acorner[1] + int(b))
    self.bcorner = (self.bcorner[0] + int(a), self.bcorner[1] + int(b))


def main(a, b):
  rec = Rect() 
  rec.move_rect(a, b)
  print rec.acorner, rec.bcorner


if __name__ == '__main__':
  main(a, b)

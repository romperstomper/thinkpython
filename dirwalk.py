import os

class mus(object):
  def __init__(self):
    self.total = 0

  def dirwalk(self, a):
    for i in os.listdir(a):
      if os.path.isdir(a + '/' + i):
        self.dirwalk(a + '/' + i)
      else:
        self.total += os.path.getsize(a + '/' + i)
    return self.total

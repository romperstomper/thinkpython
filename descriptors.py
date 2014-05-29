#!/usr/bin/python

class Mycircle(object):
  PI = 3.14
  def __init__(self, radius):
    self.radius = radius

  @property
  def circum(self):
    return self.PI * 2 * self.radius

a = Mycircle(2)
print a.circum
a.radius = 3
print a.circum

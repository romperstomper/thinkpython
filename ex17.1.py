#!/usr/bin/python

import sys

class Time(object):
  def __init__(self, seconds=None, minutes=None, hours=None):
    self.seconds = seconds
    self.minutes = minutes
    self.hours = hours

  def time_to_int(self):
    """Converts times to integers. """
    minutes = self.hours * 60 + self.minutes
    seconds = minutes * 60 + self.seconds
    return seconds

a = Time(sys.argv[1], sys.argv[2], sys.argv[3])
print a.time_to_int()


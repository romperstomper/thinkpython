#!/usr/bin/python

class Time(object):
  def __init__(self, hours=0, minutes=0, seconds=0):
    self.seconds = seconds
    self.minutes = minutes
    self.hours = hours

  def print_time(self):
    """Prints a time in the form of hour:minute:second"""
    print '%.2d:%.2d:%.2d' % (self.hours, self.minutes, self.seconds)

  def time_to_int(self):
    """Converts times to integers. """
    minutes = self.hours * 60 + self.minutes
    seconds = minutes * 60 + self.seconds
    return seconds

  def int_to_time(self, seconds):
    """Converts ints to times. """
    self.hours = seconds/3600
    self.minutes = (seconds%3600)/60
    self.seconds = (seconds%3600)%60

  def increment(self, seconds):
    """Adds a certain number of seconds the time object."""
    current = self.time_to_int()
    new = current + seconds
    return self.int_to_time(new)

  def __add__(self, other):
    if isinstance(other, Time):
      return self.add_time(other)
    else:
      return self.increment(other)

  def add_time(self, other):
    first = self.time_to_int()
    print 'first is %s' % first
    second = other.time_to_int()
    print 'second is %s' % second
    seconds = first + second
    self.int_to_time(seconds)
    self.print_time()

  def __radd__(self, other):
    return self.__add__(other)




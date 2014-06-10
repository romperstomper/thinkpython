"""Exercise 18.1
Write a __cmp__ method for Time objects. Hint: you can use tuple comparison, but
you also might consider using integer subtraction.
"""


class Time(object):
  def __init__(self, hours=0, minutes=0, seconds=0):
    self.seconds = seconds
    self.minutes = minutes
    self.hours = hours

  def __str__(self):
    """Prints a time in the form of hour:minute:second.

    Returns:
      (str) representation of the Time object
    """
    return '%.2d:%.2d:%.2d' % (self.hours, self.minutes, self.seconds)

  def to_int(self):
    """Converts times to integers.

    Returns:
      seconds: (int) Current time represented in Seconds
    """
    minutes = self.hours * 60 + self.minutes
    seconds = minutes * 60 + self.seconds
    return seconds

  def from_int(self, seconds):
    """Converts ints to times.

    Args:
      seconds: (int) number of seconds to increment by
    """
    self.hours = seconds/3600
    self.minutes = (seconds%3600)/60
    self.seconds = (seconds%3600)%60

  def increment(self, seconds):
    """Adds a certain number of seconds the time object.

    Args:
      seconds: (int) number of seconds to increment by
    """
    current = self.to_int()
    new = current + seconds
    self.from_int(new)

  def __add__(self, other):
    """Adds two time objects by calling either add_time or increment.

    Args:
      other: Time (object) or (int)
    """
    if isinstance(other, Time):
      totaltime = self.add_time(other)
    else:
      self.increment(other)
    return str(totaltime)

  def add_time(self, other):
    """Adds two time objects by converting them to ints, then sum the ints and
       represent again in original time format.

    Args:
      other: Time object
    """
    newtime = Time()
    first = self.to_int()
    second = other.to_int()
    total = first + second
    newtime.from_int(total)
    return newtime

  def __radd__(self, other):
    """Adds two time objects by implementing a right hand add for Time objects.

    Args:
      other: (object) Time
    """
    return self.__add__(other)

  def __cmp__(self, other):
    """Compares two time objects value.

    Args:
      other: Time object

    Returns:
      (int) -1 if other is greater, 0 if equal, 1 otherwise.
    """
    t1 = (self.hours, self.minutes, self.seconds)
    t2 = (other.hours, other.minutes, other.seconds)
    return cmp(t1, t2)


a = Time(1, 0, 2)
b = Time(2, 0, 0)
c = Time(1, 0, 1)
print a.__cmp__(b)
print a.__cmp__(a)
print a.__cmp__(c)




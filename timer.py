
class Time(object):
  def __init__(self, hours=0, minutes=0, seconds=0):
    self.seconds = seconds
    self.minutes = minutes
    self.hours = hours

  def print_time(self):
    """Prints a time in the form of hour:minute:second"""
    print '%.2d:%.2d:%.2d' % (self.hours, self.minutes, self.seconds)

  def time_to_int(self):
    """Converts times to integers.

    Returns:
      seconds: (int) Current time represented in Seconds
    """
    minutes = self.hours * 60 + self.minutes
    seconds = minutes * 60 + self.seconds
    return seconds

  def int_to_time(self, seconds):
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
    current = self.time_to_int()
    new = current + seconds
    self.int_to_time(new)

  def __add__(self, other):
    """Adds two time objects by calling either add_time or increment.

    Args:
      other: Time object
    """
    if isinstance(other, Time):
      self.add_time(other)
    else:
      self.increment(other)

  def add_time(self, other):
    """Adds two time objects by converting them to ints, then sum the ints and
       represent again in original time format.

    Args:
      other: Time object
    """
    first = self.time_to_int()
    print 'first is %s' % first
    second = other.time_to_int()
    print 'second is %s' % second
    seconds = first + second
    self.int_to_time(seconds)
    self.print_time()

  def __radd__(self, other):
    """Adds two time objects by implementing a right hand add for Time objects.

    Args:
      other: Time object
    """
    return self.__add__(other)

  def __cmp__(self, other):
    """Compares two time objects value.

    Args:
      other: Time object

    Returns:
      (int) -1 if other is greater, 0 if equal, 1 otherwise.
    """
    for elem in other.__dict__:
      print self.__dict__[elem], other.__dict__[elem]  # Debug
      if self.__dict__[elem] > other.__dict__[elem]:
        return 1
      if self.__dict__[elem] > other.__dict__[elem]:
        return -1
    return 0





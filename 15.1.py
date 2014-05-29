# Reads in user supplied co-ordinates and calcutes the distance between them.


import sys


def parse_input():
  """Parse the uesr supplied string arguments and return two tuples containing
     integers.

  Returns:
    a, b: (tuple) a pair of tuple containing integers.
  """
  try:
    a = sys.argv[1]
    b = sys.argv[2]
  except IndexError:
    print '2 sets of co-ordinates required'
    return
  print (int(a[0]), int(a[1])), (int(b[0]), int(b[1]))



def main():
  try:
    a, b = parse_input()
  except TypeError:
    return
  print 'a: %s, b; %s' % (a, b)

  xdiff = int(a[0]) - int(b[0])
  ydiff = int(a[0]) - int(b[0])
  print xdiff, ydiff

if __name__ == '__main__':
  main()

import datetime as dt
import sys


def nextmummy(mummy):
  """Figure out the next mummy to show and return that mummy.

  Args:
    mummy: (str) current mummy on show

  Returns:
    nextmummy: (str) next mummy to show
  """
  mummies = ['B', 'G', 'L']
  currentpos = mummies.index(mummy)
  nextpos = (currentpos+1)%3
  nextmummy = mummies[nextpos]
  return nextmummy


def main():
  try:
    mummy = sys.argv[1].upper()
  except IndexError:
    'print you must supply todays mummy'
  start = dt.datetime.now()
  end = dt.timedelta(days=60)+start
  while start <= end:
    for i in range(14):
      print '%s %s' % (start, mummy) 
      start = start + dt.timedelta(days=1)
    mummy = nextmummy(mummy)


if __name__ == '__main__':
  main()

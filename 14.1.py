import os
import sys

if not len(sys.argv) > 1:
  dirname = os.getcwd()
else:
  dirname = sys.argv[1]


def walkdir(dirname):
  res = os.walk(dirname)
  tmp = res.next()
  todo = tmp[1]
  while True:
    print 'directory is %s\n' % tmp[0]
    for filename in tmp[2]:
      print os.path.join(tmp[0], filename)
    print '_' * 50
    try:
      tmp = res.next()
    except StopIteration:
      break
      

if __name__ == '__main__':
  print '\n',  '_' * 50
  walkdir(dirname)

import sys
def most_frequent(fd):
  d = {}
  for line in fd:
    for char in line:
      if char in d:
        d[char]+=1
      else:
        d[char]=1
  return d

def sortdict(d):
  l = []
  for chr, freq in d.iteritems():
    l.append((freq, chr))
  l.sort(reverse=True)
  print l
  
def main():
  fil = sys.argv[1]
  fd = open(fil, 'r')
  dic = most_frequent(fd)
  print sortdict(dic)

if __name__ == '__main__':
  main()

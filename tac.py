
def tac(a):
  fh = open(a)
  buf = ''
  fh.seek(0, 2)
  end = fh.tell()
  fh.seek(-32, 2)
  everyline = []
  while fh.tell() >= 64:
    moo = fh.read(32)
    if moo.count('\n') == 0: 
      buf += moo
    elif moo.count('\n') == 1:everyline
      buf += moo[moo.index('\n'):]
      print buf
      buf =  moo[:moo.index('\n')]
    fh.seek(-64, 1)
    

  print 'last is %s ' % fh.read()


tac('mummy.py')



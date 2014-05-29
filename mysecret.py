#!/usr/bin/python
class mysecret(object):
  def __init__(self, secret=None):
    self.secret = secret

  @property
  def getsecret(self):
    print 'called getsecret: %s' % self._secret
    return self._secret

  @getsecret.setter
  def getsecret(self, newvalue):
    print 'called setsecret'
    self._secret = newvalue

  @getsecret.deleter
  def getsecret(self):
    print 'deleting %s' % self._secret
    del self._secret
  
a=mysecret()
a.getsecret = 'moo'
a.getsecret 
del a.getsecret 

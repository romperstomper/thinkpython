class See(object):
  def __init__(self):
    secret = ''
    self._secret = secret
 
  @property
  def secret(self):
    return self._secret
 
  @secret.setter
  def secret(self, newpass):
    if self._secret != newpass:
      self._secret = newpass
      print('New password is: ', newpass)
    else:
      print("Invalid password")
 
a = See()


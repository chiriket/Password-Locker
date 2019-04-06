class User:
  """
  Class that generates new instances of users
  """
  
  User = []

  def __init__(self, login_name, password):
     '''
     __init__ method that helps us define properties for our objects.
      
      
        self.login_name = New user login name.
        self.password  = New user password.
    '''

  def save_user(self):
        '''
        method to save a new users
        '''

        User.user_list.append(self)

  @classmethod
  def user_login(cls, login):
    '''
    method to check login credentials
    '''
    for User in cls.user_list:
    if User.login_name == login:
    return User


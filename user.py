class User:
  """
  Class that generates new instances of users.
  """
  
  user_list = []

  def __init__(self, login_name, password):
     '''
     __init__ method that helps us define properties for our objects.
      
     Args:
        self.login_name: New user login name.
        self.password: New user password.
     '''
      
     self.login_name = login_name
     self.password   = password

  def save_user(self):
        ''' 
        method to save a new user
        '''

        User.user_list.append(self)

  


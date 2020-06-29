import string
import random

class Users:
    """
    class that contains the users methods and attributes
    """
    user_info = []

    def __init__(self,first,last,password):
        """
        Information needed to create a password saving object
        """
        self.first = first
        self.last = last
        self.password = password

    def create_user(self):
        """
        create an instance of a new user
        """
        self.user_info.append(self)
 
class Credentials(Users):
    """
    class that holds credential information and associated methods
    """
    Credentials_info = []
    user_cred_info = []

    @classmethod
    def user_check(cls,first,password):
        """
        checks for matching credentials in user_info
        """
        for cred in cls.user_info:
            if cred.first == first and cred.password == password:
                identity = cred.first
                return identity

    def __init__(self,name,username,platform,password):
        """
        Initialize new credentials object
        """
        self.name = name
        self.username = username
        self.platform = platform
        self.password = password

    def save_cred(self):
        Credentials.Credentials_info.append(self)
    
    def password_gen(self,size):
        """
        generate a random string of letters and digits
        """
        lettersAndNumbers = string.ascii_letters + string.digits
        password = ''.join(random.choice(lettersAndNumbers) for i in range(int(size)))
        return password

    @classmethod
    def show_credentials(cls,username):
        """
        shows the saved credentials
        """
        for cred in cls.Credentials_info:
            if cred.username == username:
                cls.user_cred_info.append(cred)

                return cls.user_cred_info

    @classmethod
    def find_platform(cls,platform):
        """
        finds the platform's credentials
        """
        for cred in cls.Credentials_info:
            if cred.platform == platform:
                return cred

    @classmethod
    def del_cred(cls,cred):
        for credential in cls.Credentials_info:
            if credential == cred:
                del credential
                return "Deleted"
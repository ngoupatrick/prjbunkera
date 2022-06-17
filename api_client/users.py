from . import baseLocalURL
from . import baseREMOTEURL
from . import requests
class Users:
    uri=None
    
    def __init__(self, base_uri=baseLocalURL, **kwargs):
        super().__init__(**kwargs)
        self.uri=base_uri
        
    def getAllUsers(self):
        return requests.get(self.uri+"/users").json()
        
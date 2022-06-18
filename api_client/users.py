from . import baseLocalURL
from . import baseREMOTEURL
from . import requests


class Users:
    uri = None

    def __init__(self, base_uri=baseLocalURL, **kwargs):
        super().__init__(**kwargs)
        self.uri = base_uri+"/users"

    def getAllUsers(self):
        return requests.get(url=self.uri).json()

    def getUser(self, key):
        #status_code
        return requests.get(url=self.uri+"/"+key).json()

    def saveUser(self, data):
        return requests.post(url=self.uri, json=data).json()
    
    def updateUser(self,data):
        key=data.pop("key","")
        return requests.put(url=self.uri+"/"+key, json=data).json()
    
    def deleteUser(self, key):
        return requests.delete(url=self.uri+"/"+key).json()

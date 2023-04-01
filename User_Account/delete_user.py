import json
import requests
from Create_User.dataenter import Data_enter

class DeleteUser:
    def getuser(self):
        list=requests.get("https://reqres.in/api/users?page=2")
        print(list.json())
        print(list)



obj4 = DeleteUser()
obj4.caller()

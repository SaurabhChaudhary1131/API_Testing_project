import json
import requests


class UserAccount:
    list_of_users = {}

    def dataenter(self):
        user = {"name": input(), "email": input(), "salary": input(), "id": input()}
        stringify = json.dumps(user)
        open("data.json", "w").write(stringify)
        val = {user["id"]: user} #puchna h ki upr dict me ese append kia ?
        self.list_of_users.update(val)
        print(self.list_of_users)
        return user

    def new_user(self,name, email, salary, id):
        mydata = open("data.json", "r").read()
        endpoint = requests.post("https://reqres.in/api/users", params="page=2", data=json.loads(mydata))
        print(endpoint, endpoint.json())
        #print(endpoint.url)
        assert endpoint.status_code == 201, "User was not created"
        assert endpoint.json()["id"] == id, "ID mismatched"
        assert endpoint.json()["name"] == name, "Name mismatched"
        assert endpoint.json()["email"] == email, "Job mismatched"
        assert endpoint.json()["salary"]== salary, "salary mismatched"

    def delete_user(self, user_id):
        delete = requests.delete("https://reqres.in/api/users/"+user_id)
        assert delete.status_code == 204, "User Not Deleted"
        self.list_of_users.pop(user_id)
        print(self.list_of_users)

    def multi_create_caller(self):
        make_user = 'Y'
        while make_user == 'Y' or make_user == 'y':
            user_created = self.dataenter()
            self.new_user(user_created["name"], user_created["email"], user_created["salary"], user_created["id"])
            make_user = input('Do you want to make another user?\nPress Y or y for True\nPress any key for False\n')

    def multi_delete_caller(self):
        delete_user = 'Y'
        while delete_user == 'Y' or delete_user == 'y':
            user_id = input()
            self.delete_user(user_id)
            delete_user = input('Do you want to delete another user?\nPress Y or y for Yes\nPress any key for No\n')



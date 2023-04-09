import requests
import json

class Accounts:
    positive = {"name" : "jack", "acc_no":123456, "balance":100000}
    duplicate = {"name" : "abc", "acc_no":1234567, "balance":500000}
    minimum = {"name" : "rock", "acc_no":12345, "balance":1000}

    def check_the_user(self):
        print("Enter the name on account")
        a = input()
        if a == self.positive["name"]:
            print("user exists")
            request = requests.post("https://reqres.in/api/users?page=2")
            print(request)
            code = request.status_code
            assert code == 201, "user does not exist"
        else:
            req = requests.post("https://reqres.in/api/register")
            print(req)
            print("user doesnot exist")
            code1 = req.status_code
            assert code1 == 400, "something wrong happens"


    def duplicate_user(self):
        print("Enter the name")
        name = input()
        print("Enter account number")
        account = int(input())
        if account == self.duplicate["acc_no"]:
            print(name)
            print(self.duplicate["acc_no"])
            print("account already present can not make duplicate account")
            req = requests.post("https://reqres.in/api/register")
            print(req)
            code = req.status_code
            assert code == 400,"something wrong happens"
        else:
            print("Incorrect account number/Account does not exists")

    def deposit(self):
        print("enter the account number for depositing money")
        a = int(input())
        if a == self.positive["acc_no"]:
            print("enter deposit money")
            b = int(input())
            if b>=10000:
                print("can not deposit this much amount in a single transaction")
            else:
                c = self.positive["balance"]+b
                print("Updated balance is",c)
                req = requests.post("https://reqres.in/api/users")
                print(req)
                code = req.status_code
                assert code == 201 , "something went wrong"
        else:
            print("wrong account number")

    def withdrawl(self):
        print("enter the account number for withdrawing money")
        a = int(input())
        if a == self.positive["acc_no"]:
            print("enter the amount")
            b=int(input())
            if b>= (self.positive["balance"])*.9:
                print("you cannot withdraw 90 percent amount from account in one time")
            else:
                print("updated balance is", self.positive["balance"] -b)
                req = requests.post("https://reqres.in/api/users")
                print(req)
                code = req.status_code
                assert code == 201, "something went wrong"
        else:
            print("wrong account number")

    def minimum_amount(self):
        print("enter the account number for withdrawing money")
        a = int(input())
        if a == self.minimum["acc_no"]:
            print("enter the amount")
            b = int(input())
            c = self.minimum["balance"]-b
            if c >= 100:
                print("updated balance is", c)
                req = requests.post("https://reqres.in/api/users")
                print(req)
                code = req.status_code
                assert code == 201, "something went wrong"
            else:
                print("Account should have minimum balance of $100")
        else:
            print("account does not match")


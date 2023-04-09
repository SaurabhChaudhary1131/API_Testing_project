from User_Account.user_account_blueprint import UserAccount
from Account_maintain.account_maintain import Accounts
class UserAccountExecution:

    def user_account_action(self):
        user_manipulation = UserAccount()
        accounts = Accounts()
        want_operation = True
        while want_operation:
            options = input("What do you want to do?\nPress 1 for User Accounts Creation.\nPress 2 for User Account "
                            "Deletion.\nPress 3 for User Check.\nPress 4 for Checking the Duplicate User.\nPress 5 to "
                            "Deposit Money.\nPress 6 to Withdraw Money.\nPress 7 to check if Account has sufficient "
                            "Minimum Balance.\n")
            if options == "1":
                print("please provide 'Name', 'Email' , 'Salary' and 'Id'")
                user_manipulation.multi_create_caller()

            elif options == "2":
                print("give the user id for deleting")
                user_manipulation.multi_delete_caller()

            elif options == "3":
                accounts.check_the_user()

            elif options == "4":
                accounts.duplicate_user()

            elif options == "5":
                accounts.deposit()

            elif options == "6":
                accounts.withdrawl()

            elif options == "7":
                accounts.minimum_amount()

            else:
                print("Please provide the correct input.\n********** Session Terminated **********\n")
                return

            another_operation = input("Do you want to make another operation?\nPress 1 for yes.\nPress 2 for No.\n")
            if another_operation == "2":
                want_operation = False
            else:
                want_operation = True

obj = UserAccountExecution()
obj.user_account_action()

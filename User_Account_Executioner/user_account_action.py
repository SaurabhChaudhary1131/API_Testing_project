from User_Account.user_account_blueprint import UserAccount

class UserAccountExecution:

    def user_account_action(self):
        user_manipulation = UserAccount()
        want_operation = True
        while want_operation:
            options = input("What do you want to do?\nPress 1 for User Accounts Creation.\nPress 2 for User Account "
                            "Deletion.\n")
            if options == "1":
                user_manipulation.multi_create_caller()

            elif options == "2":
                print("give the user id for deleting")
                user_manipulation.multi_delete_caller()

            another_operation = input("Do you want to make another operation?\nPress 1 for yes.\nPress 2 for No.\n")
            if another_operation == "2":
                want_operation = False
            else:
                want_operation = True

obj = UserAccountExecution()
obj.user_account_action()

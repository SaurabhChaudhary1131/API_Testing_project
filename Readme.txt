Assignment API TEsting scripts 
	

The assignment contains two type of approaches for the requirements and all will give the API responce on passing and failing

1- For first two requirements  of multiple users and deleting those users by providing the ID are stored in a Python Dictionary and will take dynamic value that is user defined 

2- For other requirements User are created already and the tasks will be performed on a static data 

created users are :
 
1- positive = {"name" : "jack", "acc_no":123456, "balance":100000}
2- duplicate = {"name" : "abc", "acc_no":1234567, "balance":500000}
3- minimum = {"name" : "rock", "acc_no":12345, "balance":1000}



Run the (user_account_action.py) file from (User_Account_Executioner) package
The scripts will run in such a way that it will ask to perform the task :


What do you want to do?
Press 1 for User Accounts Creation.
Press 2 for User Account Deletion.
Press 3 for User Check.
Press 4 for Checking the Duplicate User.
Press 5 to Deposit Money.
Press 6 to Withdraw Money.
Press 7 to check if Account has sufficient Minimum Balance.




Press 1 for User Accounts Creation. (This will allow user to create multiple or single user) *Give "name", "email", "salary", "id" and user will be stored in the datastructure*

Press 2 for User Account Deletion. (This will allow to delete user by giving the ID of that user) 

Press 3 for User Check. (This will check the user if presemt by giving the name of user) *Give name as jack for passing the testcases otherwise give any for failing*

Press 4 for Checking the Duplicate User. (This will check if the user is duplicate by giving the account number) *Give acc_no as 1234567 for passing otherwise give any for failing*

Press 5 to Deposit Money. (This will allow to deposit money on account by giving account numner) *Give acc_no as 123456 for passing the testcase otherwise give any for failing*

Press 6 to Withdraw Money.(This will allow to withdraw money from account by giving account numner) *Give acc_no as 123456 for passing otherwise give any for failing*

Press 7 to check if Account has sufficient Minimum Balance.(This will allow user to check that the minimum balance should be $100) *Give Account no as 12345 for passing otherwise give any for failing*




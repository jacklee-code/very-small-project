#[Estimated originality & practicality: 9/10 Estimated difficulty: 9/10]
# The proposed topic looks interesting and feasible.
# The system appears to assume a fixed number of users and books.
# It may be better to allow users to add or delete books to demonstrate your programming skills.
# On the other hand, the users part may be omitted to reduce the unnecessary complexity of the system.

# TODO LIST:
# Register (OK) (TESTED)
# Login (OK) (TESTED)
# Load library (OK) (TESTED)
# Standardize output (OK) (TESTED)
# Borrow Book + Error Msg (ADD update library function) (OK) (TESTED)
# Function : Save Data to File (OK) (TESTED)
# Function : Save Library to File (OK) (TESTED)
# Return Book (OK) (TESTED)
# Add Library List (OK)(TESTED)
# Remove Library List (OK)(TESTED)
# Save every important action (OK) (TESTED)
# Search Book By ID/Name/Author (OK) (TESTED)

from AccountManager import Account
from LibraryManager import Library
import RuleManager as rule

########## TEST FUNCTION #######################
#This is for test and create account
def test_register():
    while True:
        print('Register Test')
        account = Account()
        account.Username = input('Please input username : ')
        account.Password = input('Please input password : ')
        if account.register():
            print('Register OK')
            return

def test_Login():
    while True:
        account = Account()
        print('Login Test')
        ac = input('Please input username : ')
        pw = input('Please input password : ')
        if account.login(ac, pw):
            print('Login OK\n')
            return  account
        print('Login Fail. Please Retry')
###############################################


####This is just for me to test if my function works
def test():
    Library.loadLibrary()
    print(Library.getAllRecords())
    ac = test_Login()

    ac.borrowBooks(['LN001', 'I am Error Book', 'DS001', 'DS003'])

    print('My current book')
    print(rule.OutputRule.getLibraryHeader())
    for i in ac.MyBookList:
        print(i.getRecord())
    print()

    print('Search Book')
    print(Library.getBookRecordByAuthor('RowLing'))
################END test section#################################

def main():
    #TODO : Your Code Here
    #Test account : Jack
    #Test password : a
    #Your can register your own account by using register() function in AccountManager.Account
    #Or you can just  use my test function -- test_register() to quickly create an account
    pass

if __name__ == '__main__':
    #TODO : Please change test() to main()
    #NOTE: test() is only used to test the correctness of the function for me
    test()
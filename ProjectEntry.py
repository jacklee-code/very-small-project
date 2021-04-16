# [Estimated originality & practicality: 9/10 Estimated difficulty: 9/10]
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
# This is for test and create account
def register():
    while True:
        account = Account()
        account.Username = input('Please input username : ')
        account.Password = input('Please input password : ')
        if account.register():
            print('Register OK')
            return account


def login():
    while True:
        account = Account()
        ac = input('Please input username : ')
        pw = input('Please input password : ')
        if account.login(ac, pw):
            return account
        print('Login Fail. Please Retry')


###############################################


####This is just for me to test if my function works
def test():
    Library.loadLibrary()
    print(Library.getAllRecords())
    ac = login()

    ac.borrowBooks(['LN001', 'I am Error Book', 'DS001', 'DS003'])

    print('My current book')
    print(rule.OutputRule.getLibraryHeader())
    for i in ac.MyBookList:
        print(i.getRecord())
    print()

    print('Search Book')
    print(Library.getBookRecordByAuthor('RowLing'))


################END test section#################################

menu = [
    "1. Book list",
    "2. Search",
    "3. Borrow",
    "4. Return",
    "5. Add book to library",
    "6. Remove book from library",
    "7. Exit"
]


def getAccountBy(action_code):
    if action_code == '1':
        return register()
    elif action_code == '2':
        return login()
    elif action_code == '3':
        return testAccountLogin()
    else:
        print("Please enter a valid action code.")
        return None


def testAccountLogin():
    account = Account()
    account.login('jack', 'a')
    return account


def showLoginMenu():
    print("Welcome User")
    print("1. Register")
    print("2. Login")
    print("3. Login with test account\n")


def showMainMenu():
    print('--------------------------')
    for operation in menu:
        print(operation)
    print()


def showSearchMenu():
    print('1. Search by book ID')
    print('2. Search by book name')
    print('3. Search by book author')
    print('4. Quit searching')
    print('--------------------------')


def searchBookByID():
    book_id = input("Book ID to search: ")
    if Library.isBookExist(book_id):
        book = Library.getBookByID(book_id)
        print(book.getRecord())
    else:
        print("No such book found.")


def searchBookByName():
    book_name = input("Book name to search: ")
    print(Library.getBookRecordByName(book_name))


def searchBookByAuthor():
    book_author = input("Author to search: ")
    print(Library.getBookRecordByAuthor(book_author))


def handleSearch():
    showSearchMenu()
    end_search = False
    while not end_search:
        search_mode = input('Enter search mode: ')
        if search_mode == '1':
            searchBookByID()
        elif search_mode == '2':
            searchBookByName()
        elif search_mode == '3':
            searchBookByAuthor()
        elif search_mode == '4':
            end_search = True
        else:
            print("Please enter valid search mode.")


def handleBorrow(account):
    id_str = input("IDs of the book (you may use comma to separate IDs)")
    id_str = id_str.replace(' ', '')
    id_list = id_str.split(',')
    account.borrowBooks(id_list)


def handleReturn(account):
    id_str = input("IDs of the book (use comma to separate IDs)")
    id_str = id_str.replace(' ', '')
    id_list = id_str.split(',')
    account.returnBooks(id_list)


def newBookToLibrary():
    book_id = input('ID for the new book: ')
    book_name = input('Name of the new book: ')
    book_author = input('Author of the new book: ')
    if Library.addBook(book_id, book_name, book_author):
        print('Book added successfully.')
    else:
        print('Failed to add the book.')
        print('The ID might be occupied.')


def removeBookFromLibrary(account):
    id_str = input("IDs of the book (use comma to separate IDs)")
    id_str = id_str.replace(' ', '')
    id_list = id_str.split(',')
    Library.removeBooks(id_list, account)


def handleOperations(action_code, account):
    if action_code == '1':
        print(Library.getAllRecords())
    elif action_code == '2':
        handleSearch()
    elif action_code == '3':
        handleBorrow(account)
    elif action_code == '4':
        handleReturn(account)
    elif action_code == '5':
        newBookToLibrary()
    elif action_code == '6':
        removeBookFromLibrary(account)
    elif action_code == '7':
        return True
    elif action_code == '8':
        showMainMenu()


def main():
    # Test account : jack
    # Test password : a
    # Your can register your own account by using register() function in AccountManager.Account
    # Or you can just  use my test function -- test_register() to quickly create an account

    account = Account()
    while (account is None) or (account.Username == ""):
        showLoginMenu()
        action_code = input("Enter action code: ")
        account = getAccountBy(action_code)
    print('\nLogin successfully.')
    print(f'Welcome {account.Username}')

    Library.loadLibrary()  # Init Library
    showMainMenu()  # Show main menu

    terminated = False
    while not terminated:
        action_code = input("Enter action code (8 to show menu):")
        print()
        terminated = handleOperations(action_code, account)


def returnTest():
    Library.loadLibrary()
    print(Library.getAllRecords())
    ac = login()

    ac.returnBooks(['LN001'])


if __name__ == '__main__':
    main()
    # returnTest()

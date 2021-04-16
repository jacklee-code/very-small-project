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
from collections import OrderedDict


################Login and Registration#################################
def register():
    while True:
        account = Account()
        account.Username = input('Username : ')
        account.Password = input('Password : ')
        if account.register():
            print('Registration Success.')
            return account


def login():
    while True:
        account = Account()
        ac = input('Username : ')
        pw = input('Password : ')
        if account.login(ac, pw):
            return account
        print('Login Fail. Please Retry\n')

################Login and Registration#################################

login_menu = {
    "Register": "1",
    "Login": "2",
    "Login with test account": "3",
}

main_menu = {
    "Book list": "1",
    "Show my books": "2",
    "Search": "3",
    "Borrow": "4",
    "Return": "5",
    "Add book to library": "6",
    "Remove book from library": "7",
    "Exit": "8"
}

search_menu = {
    "Search by book ID": "1",
    "Search by book name": "2",
    "Search by book author": "3",
    "Quit searching": "4",
}

login_menu = OrderedDict(login_menu.items())
main_menu = OrderedDict(main_menu.items())
search_menu = OrderedDict(search_menu.items())


def getAccountBy(action_code):
    if action_code == '1':
        return register()
    elif action_code == '2':
        return login()
    elif action_code == '3':
        return testAccountLogin()
    else:
        print("Please enter a valid command.")
        return None


def testAccountLogin():
    account = Account()
    account.login('jack', 'a')
    return account


def showLoginMenu():
    print("Welcome User")
    for key, value in login_menu.items():
        print(f'{value}.{key}')
    print()


def showMainMenu():
    print('--------------------------')
    for key, value in main_menu.items():
        print(f'{value}.{key}')
    print()


def showSearchMenu():
    for key, value in search_menu.items():
        print(f'{value}.{key}')
    print()


def searchBookByID():
    book_id = input("Book ID to search: ")
    print(Library.getBookRecordByID(book_id))


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
        print('--------------------------')


def handleBorrow(account):
    print("Use comma to separate IDs if more than one book is involved.")
    id_str = input("IDs of the book you would like to return: ").upper()
    id_str = id_str.replace(' ', '')
    id_list = id_str.split(',')
    account.borrowBooks(id_list)
    showUerBookList(account)


def handleReturn(account):
    print("Use comma to separate IDs if more than one book is involved.")
    id_str = input("IDs of the book you would like to return: ").upper()
    id_str = id_str.replace(' ', '')
    id_list = id_str.split(',')
    print(id_list)
    account.returnBooks(id_list)
    # account.returnBooks(['FN003'])


def newBookToLibrary():
    book_id = input('ID for the new book: ').upper()
    book_name = input('Name of the new book: ')
    book_author = input('Author of the new book: ')
    if Library.addBook(book_id, book_name, book_author):
        showLibrary()
        print('Book added successfully.')
    else:
        print('Failed to add the book.')
        print('The ID might be occupied.')


def removeBookFromLibrary(account):
    id_str = input("IDs of the book (use comma to separate IDs):").upper()
    id_str = id_str.replace(' ', '')
    id_list = id_str.split(',')
    Library.removeBooks(id_list, account)


def showLibrary():
    print(Library.getAllRecords())


def handleOperations(action_code, account):
    if action_code == main_menu["Book list"]:
        print(Library.getAllRecords())

    elif action_code == main_menu["Show my books"]:
        showUerBookList(account)

    elif action_code == main_menu["Search"]:
        handleSearch()

    elif action_code == main_menu["Borrow"]:
        showLibrary()
        handleBorrow(account)

    elif action_code == main_menu["Return"]:
        showUerBookList(account)
        handleReturn(account)

    elif action_code == main_menu["Add book to library"]:
        newBookToLibrary()

    elif action_code == main_menu["Remove book from library"]:
        removeBookFromLibrary(account)
        showLibrary()

    elif action_code == main_menu["Exit"]:
        return True

    else:
        print("Please enter a valid command.")


def showUerBookList(account):
    print("Your borrowed books:")
    print(Library.getBookRecordByOwner(account.Username))


def main():
    # Test account : jack
    # Test password : a
    # Your can register your own account by using register() function in AccountManager.Account
    # Or you can just  use my test function -- test_register() to quickly create an account

    account = Account()
    while (account is None) or (account.Username == ""):
        showLoginMenu()
        action_code = input("Enter command: ")
        account = getAccountBy(action_code)
    print('\nLogin successfully.')
    print(f'Welcome {account.Username}')

    Library.loadLibrary()  # Init Library

    terminated = False
    while not terminated:
        showMainMenu()
        action_code = input("Enter command:")
        print()
        terminated = handleOperations(action_code, account)


def returnTest():
    Library.loadLibrary()
    print(Library.getAllRecords())
    ac = Account()
    ac.login('jack', 'a')
    # ac.borrowBooks(['LN001'])
    ac.returnBooks(['LN001'])


if __name__ == '__main__':
    main()
    # returnTest()

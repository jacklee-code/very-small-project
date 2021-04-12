import hashlib
import base64
import RuleManager
from LibraryManager import Library
from os import path


class Account:
    # Data Structure
    # Username.usrfile
    # ---MD5(Password)
    # ---MyBookList (BK001;BK002;BK003)

    def __init__(self, ac = '', pw = ''):
        self.Username = ac
        #password need to be encrypt (Propery Password will auto encrypt the assigned string)
        self.Password = pw
        self.MyBookList = []

    ###Private methods
    def __getMD5(self, txt):
        md5 = hashlib.md5()
        md5.update(txt.encode('ascii'))
        return md5.hexdigest()

    def __base64encode(self, txt):
        return base64.b64encode(txt.encode()).decode('ascii')

    def __base64decode(self, txt):
        return base64.decodebytes(txt.encode()).decode('ascii')

    def __loadBooksByIds(self, idS : str):
        self.MyBookList.clear()
        for id in idS.split(';'):
            book = Library.getBookByID(id)
            if (not book is None) and (book.Owner == self.Username):
                self.MyBookList.append(book)

    def __booksToFileData(self):
        if len(self.MyBookList) == 0:
            return ''
        datastring = ''
        for book in self.MyBookList:
            if Library.isBookExist(book.ID):
                datastring += book.ID + ';'
        return datastring[:-1]


    #Public methods
    # Verification system ###############
    def register(self):
        #check if the user exists
        if path.exists(self.Username + RuleManager.DataRule.ACCOUNT_FILE_FORMAT) :
            print('User already exists (username : ' + self.Username + '). Please try again.')
            return False
        else:
            userdata = self.__password + '\n'
            f = open(self.Username + RuleManager.DataRule.ACCOUNT_FILE_FORMAT, 'w')
            userdata = self.__base64encode(userdata)
            f.write(userdata)
            f.close()
            return True

    def login(self, ac : str, pw : str):
        #User Exist?
        if not path.exists((ac + RuleManager.DataRule.ACCOUNT_FILE_FORMAT)):
            return False
        f = open(ac + RuleManager.DataRule.ACCOUNT_FILE_FORMAT)
        data = self.__base64decode(f.read()).split('\n')
        f.close()
        md5pw = data[RuleManager.DataRule.ACCOUNT_PASSWORD_INDEX]
        #Password Correct?
        if not md5pw == self.__getMD5(pw):
            return False
        #Initialize Data
        #1. Load All data to memory
        self.Username = ac
        self.Password = pw
        #2. Load all book string to Book[] and Check all the book in booklist contain in library
        ids = data[RuleManager.DataRule.ACCOUNT_BOOKLIST_INDEX]
        self.__loadBooksByIds(ids)
        self.saveFile()
        return True


    # Core Functions ##########################
    def returnBooks(self, ids : list):
        counter = 0
        for id in ids:
            book = Library.getBookByID(id)
            if book is None:
                print('ERROR :: Cannot find Book ID: ' + id + '\nPlease enter the correct id\n')
                continue
            elif book.Owner != self.Username:
                print('ERROR :: Fail to return Book ID: ' + id + '\nYou have not borrowed this book.' + '\n')
                continue
            self.MyBookList.remove(book)
            # Update book status in Library
            Library.setBookStatus(id)
            counter += 1
        print(str(counter) + ' books have been successfully returned.\n')
        self.saveFile()

    def borrowBooks(self, ids : list):
        counter = 0
        for id in ids:
            book = Library.getBookByID(id)
            if book is None:
                print('ERROR :: Cannot find Book ID: ' + id + '\nPlease enter the correct id\n')
                continue
            elif not book.Borrowable:
                print('ERROR :: Fail to borrow Book ID: ' + id + '\nThe book has been borrowed by User: ' + book.Owner + '\n')
                continue
            self.MyBookList.append(book)
            #Update book status in Library
            Library.setBookStatus(id, self.Username, False)
            counter += 1
        print(str(counter) + ' books have been successfully borrowed.\n')
        self.saveFile()

    def refreshBookList(self):
        tempList = []
        for book in self.MyBookList:
            if Library.isBookExist(book.ID):
                tempList.append(book)
        self.MyBookList = tempList
        self.saveFile()

    #write all data to file
    def saveFile(self):
        f = open(self.Username + RuleManager.DataRule.ACCOUNT_FILE_FORMAT, 'w')
        f.write(self.__base64encode(self.Password + '\n' + self.__booksToFileData()))
        f.close()

    ###Properties
    @property
    def Password(self):
        return self.__password

    @Password.setter
    def Password(self, pw):
        self.__password = self.__getMD5(pw)
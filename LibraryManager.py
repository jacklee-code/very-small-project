from BookManager import Book
import RuleManager as rule

#Initalize the Library
class Library:

    BookList = []

    @classmethod
    def saveLibrary(cls):
        f = open(rule.DataRule.LIBRARY_NAME, 'w')
        data = ''
        for book in cls.BookList:
            data += f'{book.ID};{book.Name};{book.Author};{book.Borrowable};{book.Owner}\n'
        data = data[:-1]
        f.write(data)
        f.close()

    @classmethod
    def loadLibrary(cls):
        cls.BookList.clear()
        f = open(rule.DataRule.LIBRARY_NAME, 'r')
        booksTxt = f.read().split('\n')
        for booktxt in booksTxt:
            b = Book(booktxt)
            cls.BookList.append(b)
        f.close()

    @classmethod
    def getAllRecords(cls):
        outputStr = rule.OutputRule.getLibraryHeader()
        for book in cls.BookList:
            outputStr += book.getRecord() + '\n'
        return outputStr

    @classmethod
    def isBookExist(cls, id : str):
        return not (cls.getBookByID(id) is None)

    @classmethod
    def getBookByID(cls, id : str):
        for book in cls.BookList:
            if book.ID == id:
                return book
        return None

    @classmethod
    def getBookRecordByName(cls, bookname : str):
        records = rule.OutputRule.getLibraryHeader()
        for book in cls.BookList:
            if bookname.lower() in book.Name.lower():
                records += book.getRecord() + '\n'
        return records[:-1] #Remove the last \n

    @classmethod
    def getBookRecordByAuthor(cls, author : str):
        records = rule.OutputRule.getLibraryHeader()
        for book in cls.BookList:
            if author.lower() in book.Author.lower():
                records += book.getRecord() + '\n'
        return records[:-1]  # Remove the last \n

    @classmethod
    def getBookRecordByID(cls, id : str):
        records = rule.OutputRule.getLibraryHeader()
        for book in cls.BookList:
            if id.lower() in book.ID.lower():
                records += book.getRecord() + '\n'
        return records[:-1]  # Remove the last \n

    #Register the book ownership and status - do not use it in Borrow System!!!!!!!!!!!!! Use Account.borrowBooks()
    @classmethod
    def setBookStatus(cls, id, username = 'NONE', canBorrow = True):
        for i in range(len(cls.BookList)):
            if cls.BookList[i].ID == id:
                cls.BookList[i].Borrowable = canBorrow
                cls.BookList[i].Owner = username
        cls.saveLibrary()

    @classmethod
    def addBook(cls, bookID, bookName, bookAuthor):
        if not cls.isBookExist(bookID):
            bookCode = f'{bookID};{bookName};{bookAuthor};True;NONE'
            newBook = Book(bookCode)
            cls.BookList.append(newBook)
            cls.saveLibrary()
            return True
        return False


    @classmethod
    def removeBooks(cls, idS : list, account):
        for id in idS:
            bookPointer = cls.getBookByID(id)
            if bookPointer is None:
                print('ERROR :: Fail to remove Book ID: ' + id + '\nPlease enter the correct id\n')
                continue
            cls.BookList.remove(bookPointer)
            print(f'BookID:{id} removed.')
        account.refreshBookList()
        cls.saveLibrary()
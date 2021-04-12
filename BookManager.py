import RuleManager

class Book:

    #book code = 'ID;Name;Author;Borrowable;Owner'
    def __init__(self, bookCode = ''):
        self.__lazyList = []
        self.loadThisBook(bookCode)

    #Convert my lazy list [0..N] to meaningful name -- Convenient for users to understand
    @property
    def ID(self):
        return self.__lazyList[0]
    @ID.setter
    def ID(self, id):
        self.__lazyList[0] = id

    @property
    def Name(self):
        return self.__lazyList[1]

    @Name.setter
    def Name(self, name):
        self.__lazyList[1] = name

    @property
    def Author(self):
        return self.__lazyList[2]

    @Author.setter
    def Author(self, author):
        self.__lazyList[2] = author

    @property
    def Borrowable(self):
        return (self.__lazyList[3] == True) or (self.__lazyList[3] == 'True')

    @Borrowable.setter
    def Borrowable(self, bool_):
        self.__lazyList[3] = (bool_ == 'True') or (bool_ == True)

    @property
    def Owner(self):
        return self.__lazyList[4]

    @Owner.setter
    def Owner(self, user):
        self.__lazyList[4] = user

    #Convert a string 'ID;NAME;Author;...' to Book
    def loadThisBook(self, string):
        texts = string.split(';')
        self.__lazyList.clear()
        for text in texts:
            self.__lazyList.append(text)

    #Get formatted String Record | ID |  Name  | Author |
    def getRecord(self):
        # the width of each column
        record = '|'
        for (item, width) in zip(self.__lazyList, RuleManager.OutputRule.WIDTH_OF_EACH_COLUMN):
            record += str(item).center(width) + '|'
        return record
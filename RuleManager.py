class DataRule:
    LIBRARY_NAME = 'library.db'
    ACCOUNT_FILE_FORMAT = '.user'

    # Location of pawword and booklist column in decrypted data file
    ACCOUNT_PASSWORD_INDEX = 0
    ACCOUNT_BOOKLIST_INDEX = 1

class OutputRule:
    # Width of each column of the book list
    WIDTH_OF_EACH_COLUMN = [8, 71, 29, 16, 19]
    LIBRARY_HEADER = ['Book ID'.center(WIDTH_OF_EACH_COLUMN[0]),
                      'Book Name'.center(WIDTH_OF_EACH_COLUMN[1]),
                      'Author'.center(WIDTH_OF_EACH_COLUMN[2]),
                      'Borrowable'.center(WIDTH_OF_EACH_COLUMN[3]),
                      'Borrowed User'.center(WIDTH_OF_EACH_COLUMN[4])]

    @classmethod
    def printLibraryHeader(cls):
        for column in cls.LIBRARY_HEADER:
            print(f'|{column}', end='')
        print('|')

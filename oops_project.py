import time

class Library:
    def __init__(self, book_list, lib_name, dict, customer_name):
        self.books = book_list
        self.lib_name = lib_name
        self.dict = dict
        self.cust = customer_name

    def display_all_books(self):
        for i in self.books:
            print(i)
        return f"the books mentioned above belongs to {self.lib_name}"
    #def donate_books(self):
    #  book = str(input("give the name of the book you want to donate to us"))
    #   self.books.append(book)
    #   print(self.books)




    def issue(self):
        ask = str(input("give the name of the book that you want to issue"))
        if ask in self.dict:
            print("let us check if this books is available or not......")
            time.sleep(3)
            if self.dict[ask] != None:
                print("we are really sorry but the book has already been issued to other customer")
                print("and the customer is", self.dict[ask])

            else:
                print("The book is avalaible with us!")
                self.dict[ask] = self.cust
                time.sleep(3)
                print("the book has been issued to you")
                print(self.dict)

        else:
            print("we are really sorry but the book isnt even present in the library at this moment")

        return "Thanks for visiting"

    def donate_books(self):

        book = str(input("give the name of the book you want to donate to us"))
        self.books.append(book)
        self.dict[book] = None
        print("We've successfully added your book",book,"into our library")
        print(self.books)
        print( self.dict)
        return "thanks for visiting"

    def return_book(self):
        ret = str(input("give the name of the book you want to return to us"))
        print("Hello!",self.dict[ret],",We've successfully disissued the book", ret)
        self.dict[ret] = None
        #self.books.append(ret)

        print(self.dict)
        print(self.books)
        return "Thanks for visiting"


Books = Library(["RD Sharma", "RS Agrawal", "Alchemist"], "BSF Library",
                {"RD Sharma":"Vaibhav", "RS Agrawal":"Aditya", "Alchemist":None}, "Ashish")
#print(Books.issue())
#print(Books.display_all_books())

#print(Books.dict)
#print("Please tell us which one of the following functions you would like to operate in the library")
#print("1. Do you want to issue a book?")
#print("2. Do you want to donate a book?")
#print("3. Do you want to return a book")

#x = int(input("kindly typr the sr no of the function that you want to carry out"))
#def Main_func():
#    if x ==1:
#        print(Books.issue())
#
#    elif x ==2:
#        print(Books.donate_books())
#
#    elif x ==3:
#        print(Books.return_book())
#
#    else:
#        print("input provided wasn't in the options given")
#
#    return "bye"
#
#print(Main_func())

var = 1
while var ==1:
    print("Please tell us which one of the following functions you would like to operate in the library")
    print("1. Do you want to issue a book?")
    print("2. Do you want to donate a book?")
    print("3. Do you want to return a book")

    x = int(input("kindly typr the sr no of the function that you want to carry out"))

    if x == 1:
        print(Books.issue())

    elif x ==2:
        print(Books.donate_books())

    elif x ==3:
        print(Books.return_book())

    else:
        print("input provided wasn't in the options given")



from library_books import library_books
from datetime import datetime, timedelta


# -------- Level 1 --------
user_Choice = input("What would you like to do? \n1. Look at available books \n2. Search for a book \n3. Checkout a book \n4. Return a book \n5. Check overdue list ")
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author
def available_books(library_books):
    print("Available Books:")
    for book in library_books:
        if book.get('available') is True:
            print(f"Title: {book.get('title')}, Author: {book.get('author')}, ID: {book.get('id')}")

if user_Choice == "1":
    available_books(library_books)



# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching books

search_result = []

def search_tool(library_books):
    for book in library_books:
        if user_search == "author":
            author_search = input("What is the name of the author? ")
            if author_search.lower() == book["author"].lower():
                book_search = print(f"Title: {book.get('title')}, Author: {book.get('author')}, ID: {book.get('id')}")
                search_result.append(book_search)
                print(search_result)
                break
        if user_search == "genre":
            genre_search = input("What is the name of the genre? ")
            if genre_search.lower() == book["genre"].lower():
                book_search = print(f"Title: {book.get('title')}, Author: {book.get('author')}, ID: {book.get('id')}")
                search_result.append(book_search)
                print(search_result)
                break


if user_Choice == "2":
    user_search = input("Are you searching for an author or genre? ")
    search_tool(library_books)

    


#Input: if user is searching for genre or author, name of genre or author
#create a new and empty list
#get user input to search for book from either a single author or single genre
#for loop to check against items in list
#if user searching for author search.lower == author
#if user searching for genre search.lower == genre
#.append matching books to new list
#print new list with matching books
#Output:List of books matching input

# -------- Level 3 --------
# TODO: Create a function to checkout a book by ID
# If the book is available:
#   - Mark it unavailable
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
# If it is not available:
#   - Print a message saying it's already checked out



def Checkout(library_books):
    checkout_Id = input("What is the ID of the book you want to check out? ")
    for b in library_books:
        if b['available'] is True:
            for book in library_books:
                if book.get('id') == checkout_Id:
                    book['available'] = False
                    book['due_date'] = timedelta(weeks=2)
                    book['checkouts'] += 1
                    print("You have succesfully checked out the book.")
                break
            else:
                print("That is an invalid Id")
            break
    else:
            print("That book is unavailable")
    
        

if user_Choice == "3":
    Checkout(library_books)
    available_books(library_books)

#ask the user for input on what book they want to check out
#if available = true
#make due date = 2 weeks
#Checkouts += 1
#elif book unavailable return print saying unavailable
#else say Id not valid


# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date

#ask the user for book ID they are returning
#run a for loop for books in library books
#if return ID == ID AND that book is unavailable
#set availability to true
#clear due date
#elIf return ID != ID print invalid ID
#elif book is already available print book is already in system
def return_Book(library_books):
    return_id = input("What is the ID of the book you are returning? ")
    for book in library_books:
        if book.get('id') == return_id:   # This is wrong it isnt accepting ID of books actually missing 
                if book['available'] == False:
                    book['available'] = True
                    print("You have returned the book.")
                    break

                if book['available'] == True:
                    print("That book hasn't been checked out")
                
    else:
        print("That is an Invalid ID")
    
            
        
if user_Choice == '4':
    return_Book(library_books)

#Use if statement for library books with their due date greater than the current date
#If the due date is greater or later than today 
#Split into two if statements based on if it is still checked out
#If still checked out print overdue
#else print that the due date is coming up
#for fiorst if statement print else That book hasnt been checked out yet.
#fork any overdue books into a new list
#print new list of overdue books
overdue_list = []
current_date = datetime.now()

def overdue(library_books):
    for book in library_books:
        date_string = book.get('due_date')
        if date_string:
            due = datetime.strptime(date_string, "%Y-%m-%d")
            if due < current_date:
                if book["available"] == False:
                    overdue_list.append
                    break
            else:
                print("That book hasn't been checked out yet")
                break
        else:
            print("No books are overdue currently")
            break

if user_Choice == "5":
    overdue(library_books)
    print(f"These are all the overdue books {overdue_list}")
# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out


# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.

# -------- Optional Advanced Features --------
# You can implement these to move into Tier 4:
# - Add a new book (via input) to the catalog
# - Sort and display the top 3 most checked-out books
# - Partial title/author search
# - Save/load catalog to file (CSV or JSON)
# - Anything else you want to build on top of the system!

#if __name__ == "__main__":
    # You can use this space to test your functions
    pass

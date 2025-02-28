import sqlite3

# Create database file ebookstore.db
ebookstore = sqlite3.connect('ebookstore.db')

# Create cursor object
cursor = ebookstore.cursor()

# Functions


# Table creation and column establishment and definition.
def create_table():

    try:
        cursor.execute('''CREATE TABLE IF NOT EXISTS book(
                        id INTEGER PRIMARY KEY,
                        title VARCHAR,
                        author VARCHAR,
                        qty INTEGER)''')

    # Commit changes to database
    finally:
        ebookstore.commit()
        print("Welcome!")


# Fill in initial values for ebookstore db to start with
def fill():
    try:
        # Define values for book 1
        book_1_id = 9781573353946
        book_1_title = 'A Tale of Two Cities'
        book_1_author = 'Charles Dickens'
        book_1_qty = 30

        # Define values for book 2
        book_2_id = 9780747532743
        book_2_title = "Harry Potter and the Philosopher's Stone"
        book_2_author = 'J.K. Rowling'
        book_2_qty = 40

        # Define values for book 3
        book_3_id = 9780060234812
        book_3_title = 'The Lion, the Witch and the Wardrobe'
        book_3_author = ' C. S. Lewis'
        book_3_qty = 25

        # Define values for book 4
        book_4_id = 9780395595114
        book_4_title = 'The Lord of the Rings'
        book_4_author = 'J.R.R Tolkien'
        book_4_qty = 37

        # Define values for book 5
        book_5_id = 9781101997369
        book_5_title = 'Alice in Wonderland'
        book_5_author = 'Lewis Carroll'
        book_5_qty = 12

        # Accumulate values to be fed to ebookstore table book
        old_books = {(book_1_id, book_1_title, book_1_author, book_1_qty),
                     (book_2_id, book_2_title, book_2_author, book_2_qty),
                     (book_3_id, book_3_title, book_3_author, book_3_qty),
                     (book_4_id, book_4_title, book_4_author, book_4_qty),
                     (book_5_id, book_5_title, book_5_author, book_5_qty)}

        # Populate the book table
        cursor.executemany('''INSERT INTO book(id, title, author, qty)
                            VALUES(?, ?, ?, ?)''', (old_books))

        # Commit changes to the database
        ebookstore.commit()
        print("Database loaded.")

    # Handle duplicate or reattempted loading of information to the db
    except sqlite3.IntegrityError:
        print("Database has been loaded already!")
        pass


# Retrieve and insert new book information to book table
def new_book():
    try:
        # Acquisition of information
        book_id = int(input("What is the ISBN of the new book?"))
        book_title = input("What is the title of the new book?")
        book_author = input("Who authored the new  book?")
        book_qty = int(input("How many new books are currently in stock?"))

        # Deposition of information
        cursor.execute('''INSERT INTO book(id, title, author, qty)
                        VALUES(?, ?, ?, ?)''', (book_id, book_title,
                                                book_author, book_qty))

    # Error handling for duplicate entries
    except sqlite3.IntegrityError:
        print("You have tried to make an entry that already exists!")
        print("Please try again!")
        new_book()

    # Commit information to ebookstore db
    finally:
        ebookstore.commit()
        print("Successfully added! ")


# Retrieve updated information about a specific book and
# update information in the book table
def update():
    try:
        # Acquisition of information
        book_id = int(input("What is the ISBN of the book to update?"))
        updated_qty = int(input("How many books with the ISBN: " +
                                f"{str(book_id)}" +
                                " are there in stock?"))
        # Deposition of information
        cursor.execute('''UPDATE book SET qty = ?
                    WHERE id = ?''', (updated_qty, book_id))
        # Show new record to user for visual confirmation of success
        cursor.execute('''SELECT id, title, author, qty FROM book
                          WHERE id = ?''', (book_id,))
        book_details = cursor.fetchone()
        print(f"This is the updated record of book with ISBN: {book_id}")
        print(book_details)

    # Possible exception handling
    except Exception:
        print("You have made an invalid selection, please try again")
        update()

    # Commit information to ebookstore db
    finally:
        ebookstore.commit()
        print("Successfully updated !")


# Delete a specific book record by identifying id number
def delete():

    try:
        # Acquisition of relevant details
        book_id = int(input("What is the ISBN of the book to delete?"))
        # Deletion of corresponding record
        cursor.execute('''DELETE FROM book
                          WHERE id = ?''', (book_id,))

    # Possible exception handling
    except Exception:
        print("You have made an invalid selection, please try again")
        delete()

    # Commit information to ebookstore db
    finally:
        ebookstore.commit()
        print("Successfully deleted !")


# Search for specific record via id number/ primary key
def search():

    try:
        # Acquisition of data
        book_id = int(input("What is the ISBN of the book to search?"))

        # Show new record to user for visual confirmation of success
        cursor.execute('''SELECT id, title, author, qty FROM book
                          WHERE id = ?''', (book_id,))
        book_details = cursor.fetchone()
        print(f"This is the record of book ISBN: {book_id}")
        print(book_details)

    # Possible exception handling
    except Exception:
        print("You have made an invalid selection, please try again")
        search()


# Menu
menu = True
create_table()
fill()

while True:
    # Menu display and input acquisition
    selection = int(input('''
                All book specific actions will require the ISBN
                of the book as an ID.
                This ISBN number is found in close proximity to
                the barcode on the back of the book.
                1. Enter book
                2. Update book
                3. Delete book
                4. Search books
                0. Exit
                '''))

    if selection == 0:
        # Exit program
        ebookstore.close()
        print("Goodbye :)")
        exit()

    elif selection == 1:
        # Enter book to database
        new_book()

    elif selection == 2:
        # Update book in database
        update()

    elif selection == 3:
        # Delete book fromm database
        delete()

    elif selection == 4:
        # Search books in database
        search()

    else:
        # Inform user of erroneous input and reattempt selection
        print("You have made an invalid selection, please try again.")
        pass

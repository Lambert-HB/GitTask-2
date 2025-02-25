# GitTask-2 E-Book_store

The e_book_store.py project is a simple solution to the management of stock in a book store. This project uses SQLite3 to provide database fuctionalities, including: adding a new book, updating book quantities, deleting a book from record, and searching for a specific book by it's book ID. The program ensures data integtiry via ensuring that book IDs have to be unique.

## Table of contents
1. [Installation](#installation)
2. [Usage](#usage)

## Installation
1. Ensure that you have python installed on your computer in some form(MS Visual Studio Code, Python Interpreter etc.)
2. Download or clone the project locally.
3. Either double click on the e_book_store.py to go directly to your interpreter and run the file or open the command terminal and navigate to the directory where the .py file is stored and run the command: python e_book_store.py

## Usage

Here is rundown of how to use the program:
When the file is run there will be a menu that displays the following options:
1. Enter book: This will allow you to enter the relevant details for a new book to be added to the database.
2. Update book: Update the quantity of a book that is already in the database.   
3. Delete book: Identify by its Id a book to be removed from the datbase.
4. Search books: Return the relevant information about a book idenntiefied by it's ID.
0. Exit: This will terminate the program.

You can enter the corresponding number to the option that you woukld like to select and follow the prompts to perform the task.
If you make an erroneous input the program will inform you, the same is true for the success and failure of operations performed during the use of the application.

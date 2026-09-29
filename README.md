# Library Management System

## Introduction

The Library Management System is a beginner-friendly Python project developed to manage basic library book records. The project provides a simple menu-driven interface that allows users to perform common operations such as adding books, viewing available books, searching for a book, and deleting book records.

The main purpose of this project is to demonstrate how fundamental Python programming concepts can be combined to create a practical application. The system uses file-based storage so that book information can be saved and accessed when the program is run again.

## Features

* Add new book records
* View all stored books
* Search for a book using its ID
* Delete a book record
* Store book information in a file
* Validate basic user input
* Menu-driven command-line interface
* Automated testing of important operations
* Modular Python program structure

## Technologies Used

* Python 3
* JSON/file storage
* Python standard library
* Git and GitHub

No external Python packages are required to run this project.

## Python Concepts Used

This project demonstrates several important Python concepts:

* Variables and data types
* Strings
* Lists and dictionaries
* Conditional statements
* For and while loops
* Functions
* Modules and imports
* File handling
* JSON data storage
* Exception handling
* Input validation
* Assertions and automated testing

## How the System Works

When the program starts, a main menu is displayed. The user can select an operation by entering the corresponding number.

The **Add Book** option collects information about a book and saves the record.

The **View Books** option displays the stored book records.

The **Search Book** option allows the user to find a specific book using its book ID.

The **Delete Book** option removes a selected book record from the stored data.

The **Exit** option safely closes the program.

## Project Structure

* `main.py` – Controls the main menu and program flow.
* `library_data.py` – Handles book records and data storage.
* `library_display.py` – Displays book information.
* `library_utils.py` – Handles input and basic validation.
* `library_words.py` – Contains basic library-related data.
* `library_reports.py` – Provides library summary information.
* `test_project.py` – Contains automated tests.
* `books.json` – Stores book records.
* `README.md` – Contains project documentation.
* `statement.md` – Contains the project statement and scope.

## Requirements

To run this project, you need:

1. Python 3 or above.
2. A terminal or Python IDLE.
3. The project files downloaded or cloned to your computer.

No additional packages are required.

## How to Run

Open the project folder in a terminal and run:

```text
python main.py
```

Alternatively, open `main.py` using Python IDLE and select **Run Module**.

Follow the options shown on the screen to manage the library records.

## Testing

The project includes `test_project.py` to check important library operations.

Run:

```text
python test_project.py
```

The test program checks the main record-management operations and confirms whether they work correctly.

## Future Enhancements

The project can be expanded by adding book issue and return functionality, student/member records, due dates, fine calculation, book categories, availability status, login functionality, and database support.

## Conclusion

The Library Management System demonstrates how basic Python concepts can be used to develop a useful record-management application. Its modular structure makes the project easy to understand, test, and extend with additional library features in the future.


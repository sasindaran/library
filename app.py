import mysql.connector
import json
from datetime import datetime

# Connect to the database
conn = mysql.connector.connect(
    host="localhost",
    user="root", 
    password="", 
    database="library_db"
)

cursor = conn.cursor()

# Function to add a student
def add_student(student_id, name):
    query = "INSERT INTO students (student_lib_id, student_name, borrowed_books, history) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (student_id, name, json.dumps([]), json.dumps([])))  # Initialize empty lists for books and history
    conn.commit()

# Function to add a book to a student
def add_book_to_student(student_id, book_code):
    # Fetch the student's data
    cursor.execute("SELECT borrowed_books FROM students WHERE student_lib_id = %s", (student_id,))
    result = cursor.fetchone()
    
    if result:
        borrowed_books = json.loads(result[0])
        
        if len(borrowed_books) >= 5:
            print("Borrow limit reached.")
            return False
        
        # Check if the book is already borrowed
        cursor.execute("SELECT book_code FROM books WHERE book_code = %s", (book_code,))
        if not cursor.fetchone():
            print("Invalid book code.")
            return False
        
        # Check if the book is already borrowed by someone
        for book in borrowed_books:
            if book['code'] == book_code and book['return_date'] is None:
                print("Book already borrowed.")
                return False

        # Add the book with the current date of borrowing
        borrowed_books.append({
            'code': book_code,
            'borrow_date': datetime.now().strftime('%Y-%m-%d'),
            'return_date': None
        })

        # Update the student record
        cursor.execute("UPDATE students SET borrowed_books = %s WHERE student_lib_id = %s", (json.dumps(borrowed_books), student_id))
        conn.commit()
        print("Book borrowed successfully.")
        return True
    else:
        print("Student not found.")
        return False

# Function to drop a book from a student (i.e., mark as returned)
def drop_book_from_student(student_id, book_code):
    cursor.execute("SELECT borrowed_books, history FROM students WHERE student_lib_id = %s", (student_id,))
    result = cursor.fetchone()
    
    if result:
        borrowed_books = json.loads(result[0])
        history = json.loads(result[1])
        
        for book in borrowed_books:
            if book['code'] == book_code and book['return_date'] is None:
                # Set the return date
                book['return_date'] = datetime.now().strftime('%Y-%m-%d')
                
                # Move the book to history
                history.append(book)
                
                # Update the borrowed books and history
                cursor.execute("UPDATE students SET borrowed_books = %s, history = %s WHERE student_lib_id = %s", (json.dumps(borrowed_books), json.dumps(history), student_id))
                conn.commit()
                print("Book returned successfully.")
                return True
        
        print("Book not found or already returned.")
        return False
    else:
        print("Student not found.")
        return False

# Function to display student details
def display_student_details(student_id):
    cursor.execute("SELECT student_name, borrowed_books, history FROM students WHERE student_lib_id = %s", (student_id,))
    result = cursor.fetchone()
    
    if result:
        name, borrowed_books, history = result
        borrowed_books = json.loads(borrowed_books)
        history = json.loads(history)
        
        print(f"Student: {name}")
        print("Currently Borrowed Books:")
        for book in borrowed_books:
            if book['return_date'] is None:
                print(f" - {book['code']} (Borrowed on: {book['borrow_date']})")
        
        print("Borrow History:")
        for book in history:
            print(f" - {book['code']} (Borrowed on: {book['borrow_date']}, Returned on: {book['return_date']})")
    else:
        print("Student not found.")

# Menu system
while True:
    print("\nLibrary System Menu")
    print("1. Add a book to a student")
    print("2. Drop a book from a student")
    print("3. Add a student")
    print("4. Display student details")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        student_id = input("Enter student ID: ")
        book_code = input("Enter book code: ")
        add_book_to_student(student_id, book_code)
    
    elif choice == '2':
        student_id = input("Enter student ID: ")
        book_code = input("Enter book code: ")
        drop_book_from_student(student_id, book_code)

    elif choice == '3':
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        add_student(student_id, name)

    elif choice == '4':
        student_id = input("Enter student ID: ")
        display_student_details(student_id)

    elif choice == '5':
        break

    else:
        print("Invalid choice. Please try again.")

# Close the connection
conn.close()

import mysql.connector
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
    cursor.execute(query, (student_id, name, "", "")) 
    conn.commit()


def add_book_to_student(student_id, book_code):
    cursor.execute("SELECT borrowed_books FROM students WHERE student_lib_id = %s", (student_id,))
    result = cursor.fetchone()
    
    if result:
        borrowed_books = result[0]

        
        if len(borrowed_books.split(',')) >= 5 and borrowed_books != '':
            print("Borrow limit reached.")
            return False
        
        
        cursor.execute("SELECT book_code FROM books WHERE book_code = %s", (book_code,))
        if not cursor.fetchone():
            print("Invalid book code.")
            return False


        if book_code in borrowed_books:
            print("Book already borrowed.")
            return False


        borrow_date = datetime.now().strftime('%Y-%m-%d')
        if borrowed_books:
            borrowed_books += f",{book_code}:{borrow_date}:None"
        else:
            borrowed_books = f"{book_code}:{borrow_date}:None"

        cursor.execute("UPDATE students SET borrowed_books = %s WHERE student_lib_id = %s", (borrowed_books, student_id))
        conn.commit()
        print("Book borrowed successfully.")
        return True
    else:
        print("Student not found.")
        return False


def drop_book_from_student(student_id, book_code):
    cursor.execute("SELECT borrowed_books, history FROM students WHERE student_lib_id = %s", (student_id,))
    result = cursor.fetchone()
    
    if result:
        borrowed_books, history = result
        updated_borrowed_books = []
        updated_history = history if history else ""


        borrowed_books_list = borrowed_books.split(',') if borrowed_books else []

        for book in borrowed_books_list:
            book_data = book.split(':')
            code, borrow_date, return_date = book_data

            if code == book_code and return_date == "None":

                return_date = datetime.now().strftime('%Y-%m-%d')


                if updated_history:
                    updated_history += f",{book_code}:{borrow_date}:{return_date}"
                else:
                    updated_history = f"{book_code}:{borrow_date}:{return_date}"
            else:
                updated_borrowed_books.append(f"{code}:{borrow_date}:{return_date}")

        cursor.execute("UPDATE students SET borrowed_books = %s, history = %s WHERE student_lib_id = %s", 
                       (",".join(updated_borrowed_books), updated_history, student_id))
        conn.commit()
        print("Book returned successfully.")
        return True
    else:
        print("Student not found.")
        return False


def display_student_details(student_id):
    cursor.execute("SELECT student_name, borrowed_books, history FROM students WHERE student_lib_id = %s", (student_id,))
    result = cursor.fetchone()

    if result:
        name, borrowed_books, history = result
        
        print(f"Student: {name}")
        print("Currently Borrowed Books:")
        if borrowed_books:
            for book in borrowed_books.split(','):
                book_code, borrow_date, return_date = book.split(':')
                print(f" - {book_code} (Borrowed on: {borrow_date}, Return by: {return_date if return_date != 'None' else 'Not returned yet'})")
        else:
            print("No borrowed books.")
        
        print("\nBorrow History:")
        if history:
            for book in history.split(','):
                book_code, borrow_date, return_date = book.split(':')
                print(f" - {book_code} (Borrowed on: {borrow_date}, Returned on: {return_date})")
        else:
            print("No history available.")
    else:
        print("Student not found.")


def display_books_status():
    cursor.execute("SELECT book_code FROM books")
    all_books = cursor.fetchall()
    
    borrowed_books = set()

    
    cursor.execute("SELECT borrowed_books FROM students")
    all_borrowed_books = cursor.fetchall()

    for borrowed in all_borrowed_books:
        if borrowed[0]:
            books = borrowed[0].split(',')
            for book in books:
                book_code = book.split(':')[0]
                borrowed_books.add(book_code)

    print("Available Books:")
    for book in all_books:
        if book[0] not in borrowed_books:
            print(f" - {book[0]}")

    print("\nNot Available Books:")
    for book in all_books:
        if book[0] in borrowed_books:
            print(f" - {book[0]} (Currently borrowed)")


def display_all_students():
    cursor.execute("SELECT student_name, student_lib_id FROM students")
    all_students = cursor.fetchall()

    print("All Students:")
    for student in all_students:
        print(f" - {student[0]} (ID: {student[1]})")


while True:
    print("\nLibrary System Menu")
    print("1. Add a book to a student")
    print("2. Drop a book from a student")
    print("3. Add a student")
    print("4. Display student details")
    print("5. Display book status (Available/Not Available)")
    print("6. Display all students and their IDs")
    print("7. Exit")

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
        display_books_status()

    elif choice == '6':
        display_all_students()

    elif choice == '7':
        break

    else:
        print("Invalid choice. Please try again.")

# Close the connection
conn.close()

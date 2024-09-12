from student import add_student, delete_student, display_student_details, display_all_students
from book import add_book_to_student, drop_book_from_student, display_books_status

def display_menu(cursor, conn):
    while True:
        print("\nLibrary System Menu")
        print("1. Add a book to a student")
        print("2. Drop a book from a student")
        print("3. Add a student")
        print("4. Display student details")
        print("5. Display book status (Available/Not Available)")
        print("6. Display all students and their IDs")
        print("7. Delete a student by ID")  # New option for deleting a student
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            student_id = input("Enter student ID: ")
            book_code = input("Enter book code: ")
            add_book_to_student(cursor, conn, student_id, book_code)

        elif choice == '2':
            student_id = input("Enter student ID: ")
            book_code = input("Enter book code: ")
            drop_book_from_student(cursor, conn, student_id, book_code)

        elif choice == '3':
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            add_student(cursor, conn, student_id, name)

        elif choice == '4':
            student_id = input("Enter student ID: ")
            display_student_details(cursor, student_id)

        elif choice == '5':
            display_books_status(cursor)

        elif choice == '6':
            display_all_students(cursor)

        elif choice == '7':  # Handle deletion of student
            student_id = input("Enter student ID to delete: ")
            delete_student(cursor, conn, student_id)

        elif choice == '8':  # Exit
            break
        else:
            print("Invalid choice. Please try again.")

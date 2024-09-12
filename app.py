students = {}

# Add a student
def add_student(student_id, name):
    if student_id not in students:
        students[student_id] = {'name': name, 'books': []}
        return True
    return False

# Add a book to a student
def add_book_to_student(student_id, book):
    if student_id in students:
        if len(students[student_id]['books']) < 5:
            students[student_id]['books'].append(book)
            return True
    return False

# Drop a book from a student
def drop_book_from_student(student_id, book):
    if student_id in students:
        if book in students[student_id]['books']:
            students[student_id]['books'].remove(book)
            return True
    return False

# Display student details
def display_student_details(student_id):
    if student_id in students:
        student = students[student_id]
        print(f"ID: {student_id}, Name: {student['name']}")
        if student['books']:
            print(f"Books: {', '.join(student['books'])}")
        else:
            print("No books borrowed.")
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
        book = input("Enter book name: ")
        if add_book_to_student(student_id, book):
            print("Book added successfully.")
        else:
            print("Failed to add book (student might not exist or limit reached).")
    
    elif choice == '2':
        student_id = input("Enter student ID: ")
        book = input("Enter book name: ")
        if drop_book_from_student(student_id, book):
            print("Book dropped successfully.")
        else:
            print("Failed to drop book (book not found or student not found).")

    elif choice == '3':
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        if add_student(student_id, name):
            print("Student added successfully.")
        else:
            print("Student already exists.")
    
    elif choice == '4':
        student_id = input("Enter student ID: ")
        display_student_details(student_id)
    
    elif choice == '5':
        break
    
    else:
        print("Invalid choice. Please try again.")
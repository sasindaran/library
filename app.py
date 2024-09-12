# Initialize default books with unique codes and names in a nested array
books = [
    ["B001", "Introduction to the Theory of Computation"],
    ["B002", "Computer Systems: A Programmer's Perspective"],
    ["B003", "Operating System Concepts"],
    ["B004", "Database System Concepts"],
    ["B005", "Artificial Intelligence: A Modern Approach"],
    ["B006", "Computer Networking: A Top-Down Approach"],
    ["B007", "Computer Architecture: A Quantitative Approach"],
    ["B008", "Algorithms"],
    ["B009", "Data Structures and Algorithm Analysis in C++"],
    ["B010", "Introduction to Machine Learning"],
    ["B011", "Modern Operating Systems"],
    ["B012", "Compilers: Principles, Techniques, and Tools"],
    ["B013", "Software Engineering: A Practitioner's Approach"],
    ["B014", "Computer Vision: Algorithms and Applications"],
    ["B015", "Digital Design and Computer Architecture"],
    ["B016", "Introduction to Quantum Computing"],
    ["B017", "Data Mining: Concepts and Techniques"],
    ["B018", "Computer Graphics: Principles and Practice"],
    ["B019", "Principles of Compiler Design"],
    ["B020", "Computer Organization and Design: The Hardware/Software Interface"],
    ["B021", "Introduction to Computer Science Using Python"],
    ["B022", "Introduction to Information Systems"],
    ["B023", "Computer Science: An Overview"],
    ["B024", "Understanding Machine Learning: From Theory to Algorithms"],
    ["B025", "Computer Vision: A Modern Approach"],
    ["B026", "Design Patterns: Elements of Reusable Object-Oriented Software"],
    ["B027", "Operating Systems: Internals and Design Principles"],
    ["B028", "Computer Security: Principles and Practice"],
    ["B029", "Human-Computer Interaction"],
    ["B030", "Introduction to Cloud Computing"]
]

# Initialize book availability status
book_availability = {code: True for code, _ in books}

# Initialize empty student records
students = {}

# Add a student
def add_student(student_id, name):
    if student_id not in students:
        students[student_id] = {'name': name, 'borrowed_books': []}
        return True
    return False

# Add a book to a student
def add_book_to_student(student_id, book_code):
    if student_id in students:
        if len(students[student_id]['borrowed_books']) < 5:
            if book_code in book_availability and book_availability[book_code]:
                students[student_id]['borrowed_books'].append(book_code)
                book_availability[book_code] = False  # Mark book as borrowed
                return True
            return False  # Book code not valid or already borrowed
        return False  # Borrow limit reached
    return False  # Student not found

# Drop a book from a student
def drop_book_from_student(student_id, book_code):
    if student_id in students:
        if book_code in students[student_id]['borrowed_books']:
            students[student_id]['borrowed_books'].remove(book_code)
            book_availability[book_code] = True  # Mark book as available
            return True
        return False  # Book not found in borrowed list
    return False  # Student not found

# Display student details
def display_student_details(student_id):
    if student_id in students:
        student = students[student_id]
        print(f"ID: {student_id}, Name: {student['name']}")
        if student['borrowed_books']:
            borrowed_books = [book_name for code, book_name in books if code in student['borrowed_books']]
            print(f"Books: {', '.join(borrowed_books)}")
        else:
            print("No books borrowed.")
    else:
        print("Student not found.")

# Check book status
def check_book_status(book_code):
    if book_code in book_availability:
        if book_availability[book_code]:
            borrowed_by = next((s_id for s_id, s_data in students.items() if book_code in s_data['borrowed_books']), None)
            if borrowed_by:
                print(f"Book is borrowed by student ID: {borrowed_by}")
            else:
                print("Book is available.")
        else:
            print("Book is not available.")
    else:
        print("Book is not available in this library.")

# Menu system
while True:
    print("\nLibrary System Menu")
    print("1. Add a book to a student")
    print("2. Drop a book from a student")
    print("3. Add a student")
    print("4. Display student details")
    print("5. Check book status")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        student_id = input("Enter student ID: ")
        book_code = input("Enter book code: ")
        if add_book_to_student(student_id, book_code):
            print("Book added successfully.")
        else:
            print("Failed to add book (check code validity, availability, or borrow limit).")
    
    elif choice == '2':
        student_id = input("Enter student ID: ")
        book_code = input("Enter book code: ")
        if drop_book_from_student(student_id, book_code):
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
        book_code = input("Enter book code: ")
        check_book_status(book_code)
    
    elif choice == '6':
        break
    
    else:
        print("Invalid choice. Please try again.")

def add_student(cursor, conn, student_id, name):
    query = "INSERT INTO students (student_lib_id, student_name, borrowed_books, history) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (student_id, name, "", ""))  
    conn.commit()

def display_student_details(cursor, student_id):
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

def delete_student(cursor, conn, student_id):
    # Check if the student exists
    cursor.execute("SELECT * FROM students WHERE student_lib_id = %s", (student_id,))
    result = cursor.fetchone()

    if result:
        # Delete the student from the database
        cursor.execute("DELETE FROM students WHERE student_lib_id = %s", (student_id,))
        conn.commit()
        print(f"Student with ID {student_id} has been deleted.")
    else:
        print("Student not found.")

def display_all_students(cursor):
    cursor.execute("SELECT student_name, student_lib_id FROM students")
    all_students = cursor.fetchall()

    print("All Students:")
    for student in all_students:
        print(f" - {student[0]} (ID: {student[1]})")
        


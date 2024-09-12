from datetime import datetime

def add_book_to_student(cursor, conn, student_id, book_code):
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

def drop_book_from_student(cursor, conn, student_id, book_code):
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

def display_books_status(cursor):
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

from menu import display_menu
from database import setup_database, close_connection

if __name__ == "__main__":
    
    conn, cursor = setup_database()

    
    display_menu(cursor, conn)

    
    close_connection(conn)

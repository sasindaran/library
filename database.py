import mysql.connector

def setup_database():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",  
        password="",  
        database="library_db" 
    )
    cursor = conn.cursor()
    return conn, cursor

def close_connection(conn):
    conn.close()

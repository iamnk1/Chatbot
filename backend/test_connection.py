import sqlite3

def test_db_connection():
    try:
        # Update the path to your SQLite database file
        connection = sqlite3.connect("path_to_your_database.db")
        print("Database connection successful.")

        cursor = connection.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        if tables:
            print("Tables in the database:")
            for table in tables:
                print(table[0])
        else:
            print("No tables found in the database.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        if connection:
            connection.close()
            print("Database connection closed.")

if __name__ == "__main__":
    test_db_connection()

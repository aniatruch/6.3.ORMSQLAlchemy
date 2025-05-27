import sqlite3

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        print("Połączono z bazą:", db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
        return None

def create_tables(conn):
    books_sql = """
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        year INTEGER
    );"""

    readers_sql = """
    CREATE TABLE IF NOT EXISTS readers (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    );"""

    loans_sql = """
    CREATE TABLE IF NOT EXISTS loans (
        id INTEGER PRIMARY KEY,
        book_id INTEGER NOT NULL,
        reader_id INTEGER NOT NULL,
        loan_date TEXT NOT NULL,
        return_date TEXT,
        FOREIGN KEY (book_id) REFERENCES books(id),
        FOREIGN KEY (reader_id) REFERENCES readers(id)
    );"""

    cur = conn.cursor()
    cur.execute(books_sql)
    cur.execute(readers_sql)
    cur.execute(loans_sql)
    conn.commit()

def add_book(conn, book):
    sql = "INSERT INTO books(title, author, year) VALUES(?,?,?)"
    cur = conn.cursor()
    cur.execute(sql, book)
    conn.commit()
    return cur.lastrowid

def add_reader(conn, reader):
    sql = "INSERT INTO readers(name, email) VALUES(?,?)"
    cur = conn.cursor()
    cur.execute(sql, reader)
    conn.commit()
    return cur.lastrowid

def add_loan(conn, loan):
    sql = "INSERT INTO loans(book_id, reader_id, loan_date, return_date) VALUES(?,?,?,?)"
    cur = conn.cursor()
    cur.execute(sql, loan)
    conn.commit()
    return cur.lastrowid

def get_all(conn, table):
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table}")
    return cur.fetchall()

def update_return_date(conn, loan_id, return_date):
    sql = "UPDATE loans SET return_date = ? WHERE id = ?"
    cur = conn.cursor()
    cur.execute(sql, (return_date, loan_id))
    conn.commit()

def delete_reader(conn, reader_id):
    sql = "DELETE FROM readers WHERE id = ?"
    cur = conn.cursor()
    cur.execute(sql, (reader_id,))
    conn.commit()

if __name__ == "__main__":
    conn = create_connection("library.db")
    create_tables(conn)

    book_id = add_book(conn, ("Hobbit", "J.R.R. Tolkien", 1937))
    reader_id = add_reader(conn, ("Anna Nowak", "anna@example.com"))
    loan_id = add_loan(conn, (book_id, reader_id, "2025-05-22", None))

    print("\nKsiążki:")
    for row in get_all(conn, "books"):
        print(row)

    print("\nCzytelnicy:")
    for row in get_all(conn, "readers"):
        print(row)

    print("\nWypożyczenia:")
    for row in get_all(conn, "loans"):
        print(row)

    update_return_date(conn, loan_id, "2025-05-25")

    print("\nPo aktualizacji daty zwrotu:")
    for row in get_all(conn, "loans"):
        print(row)

    delete_reader(conn, reader_id)
    print("\n❌ Czytelnicy po usunięciu:")
    for row in get_all(conn, "readers"):
        print(row)

    conn.close()
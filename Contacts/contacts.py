import sqlite3


def create_connection(path):
    connection = sqlite3.connect(path)
    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    result = cursor.fetchall()
    return result

CREATE_QUERY = """
    CREATE TABLE IF NOT EXISTS contacts(
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
    type TEXT,
    name TEXT,
    age INTEGER,
    number TEXT NOT NULL UNIQUE
    )
    """

INSERT_QUERY = """
    INSERT INTO contacts(type, name, age, number)
    VALUES ("personal", "?", 404, "Unknown Number")
    """

READ_QUERY = """
    SELECT * FROM contacts
    """

connection = create_connection("contacts.sqlite")
#execute_query(connection, CREATE_QUERY)
#execute_query(connection, INSERT_QUERY)
results = execute_query(connection, READ_QUERY)

print(results)

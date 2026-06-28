import sqlite3

conn = sqlite3.connect("database/memory.db")

cursor = conn.cursor()

cursor.execute("""

CREATE TABLE IF NOT EXISTS memory(

customer TEXT,

query TEXT

)

""")

conn.commit()

def save_memory(customer,query):

    cursor.execute(

        "INSERT INTO memory VALUES(?,?)",

        (customer,query)

    )

    conn.commit()

def get_last_query(customer):

    cursor.execute(

        "SELECT query FROM memory WHERE customer=? ORDER BY ROWID DESC LIMIT 1",

        (customer,)

    )

    row = cursor.fetchone()

    if row:

        return row[0]

    return "No previous conversation."
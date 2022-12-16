import psycopg2
from fastapi import FastAPI

app = FastAPI()

# Connect to the database
conn = psycopg2.connect(
    host="localhost",
    user="user",
    password="pwd",
    dbname="database"
)

@app.get("/users")
def read_users():
    # Execute a SELECT query to retrieve data from the "users" table
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()

    # Return the retrieved data as a list of dictionaries
    return [{"id": row[0], "name": row[1]} for row in rows]

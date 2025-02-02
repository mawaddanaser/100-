import sqlite3

# Connect to the database
connection = sqlite3.connect("example.db")

# Create a cursor object
cursor = connection.cursor()

# Execute a SQL query
cursor.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER, name TEXT)")

# Insert data
cursor.execute("INSERT INTO students (id, name) VALUES (?, ?)", (1, "Alice"))

# Fetch data
cursor.execute("SELECT * FROM students")
result = cursor.fetchall()

# Display result
print(result)

# Close connection
connection.close()

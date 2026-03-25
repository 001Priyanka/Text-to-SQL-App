import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
connection = sqlite3.connect("student_grades.db")
cursor = connection.cursor()

# Create a table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS grades (
        id INTEGER PRIMARY KEY,
        name TEXT,
        subject TEXT,
        score INTEGER,
        grade TEXT
    )
""")

# Insert some dummy data
data = [
    (1, "Aman", "Math", 95, "A"),
    (2, "Anshu", "Math", 78, "C"),
    (3, "Akshu", "History", 88, "B"),
    (4, "Rahul", "History", 92, "A"),
    (5, "Divyansh", "Science", 85, "B"),
    (6, "Nandini", "Math", 65, "D"),
    (7, "Priyanka", "Science", 90, "A"),
    (8, "Rohit", "History", 70, "C"),
    (9, "Sonia", "Math", 80, "B"),
    (10, "Vikram", "Science", 75, "C"),
    (11, "Mahendra", "Accountancy", 82, "B")
]

cursor.executemany("INSERT OR IGNORE INTO grades VALUES (?, ?, ?, ?, ?)", data)
connection.commit()
connection.close()

print("Database created and populated successfully!")
import sqlite3


DATABASE_NAME = "complaints.db"


def create_database():
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS complaints (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student TEXT NOT NULL,
            category TEXT NOT NULL,
            priority TEXT NOT NULL,
            subject TEXT NOT NULL,
            description TEXT NOT NULL,
            status TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def add_complaint(student, category, priority, subject, description):
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO complaints
        (student, category, priority, subject, description, status)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (student, category, priority, subject, description, "Pending"))

    connection.commit()

    complaint_id = cursor.lastrowid

    connection.close()

    return complaint_id


def get_student_complaints(student):
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, student, category, priority, subject, description, status
        FROM complaints
        WHERE student = ?
        ORDER BY id
    """, (student,))

    complaints = cursor.fetchall()

    connection.close()

    return complaints


def get_all_complaints():
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, student, category, priority, subject, description, status
        FROM complaints
        ORDER BY id
    """)

    complaints = cursor.fetchall()

    connection.close()

    return complaints


def update_complaint_status(complaint_id, status):
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE complaints
        SET status = ?
        WHERE id = ?
    """, (status, complaint_id))

    connection.commit()

    updated = cursor.rowcount

    connection.close()

    return updated
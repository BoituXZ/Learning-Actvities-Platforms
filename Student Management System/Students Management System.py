import sqlite3

def create_table():
    conn = sqlite3.connect('Students.db')
    cursor = conn.cursor()
    
    cursor.ex('''
              CREATE TABLE IF NOT EXISTS Students (
                  id TEXT
                  name TEXT
                  programme TEXT
                  status TEXT)''')
    conn.commit()
    conn.close()
    
    
def fetch_students():
    conn = sqlite3.connect('Students.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Students')
    students = cursor.fetchall()
    conn.close()
    return students

def insert_students(id, name, programme, status):
    conn = sqlite3.connect('Students.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Employees (id, name, programme, status) VALUES (?, ?, ?, ?)', (id, name, programme, status))
    conn.commit()
    conn.close()
    
def remove_students(id):
    conn = sqlite3.connect('Students.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Students WHERE id = ?', (id,))
    conn.commit()
    conn.close()
        
def update_students(id, new_name, new_role, new_gender, new_status):
    conn = sqlite3.connect('Students.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE Students SET name = ?, role = ?, gender = ?, status= ? WHERE id = ?',(
new_name, new_role, new_ gender, new_status(id,))
    conn.commit()
    conn.close()
def id_exists(id):
    conn = sqlite3.connect('Students.db')
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM Employees WHERE id = ?', (id,))
    conn.commit()
    conn.close()
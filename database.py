import sqlite3
from datetime import datetime
import os

DATABASE = 'database.db'

def init_database():
    conn = sqlite3.connect(DATABASE)
    conn.execute('''
        CREATE TABLE IF NOT EXISTS todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            done BOOLEAN DEFAULT 0,
            priority INTEGER DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def get_all_todos():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cursor = conn.execute('SELECT * FROM todos ORDER BY created_at DESC')
    todos = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return todos

def add_todo(task, priority=1):
    conn = sqlite3.connect(DATABASE)
    conn.execute('INSERT INTO todos (task, priority) VALUES (?, ?)', (task, priority))
    conn.commit()
    conn.close()

def toggle_todo(todo_id):
    conn = sqlite3.connect(DATABASE)
    conn.execute('UPDATE todos SET done = NOT done WHERE id = ?', (todo_id,))
    conn.commit()
    conn.close()

def delete_todo(todo_id):
    conn = sqlite3.connect(DATABASE)
    conn.execute('DELETE FROM todos WHERE id = ?', (todo_id,))
    conn.commit()
    conn.close()

def update_todo(todo_id, new_task):
    conn = sqlite3.connect(DATABASE)
    conn.execute('UPDATE todos SET task = ? WHERE id = ?', (new_task, todo_id))
    conn.commit()
    conn.close()

def get_todo_by_id(todo_id):
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cursor = conn.execute('SELECT * FROM todos WHERE id = ?', (todo_id,))
    todo = cursor.fetchone()
    conn.close()
    return dict(todo) if todo else None

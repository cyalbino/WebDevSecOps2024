
from flask import Flask, request
import sqlite3

app = Flask(__name__)
conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        password TEXT NOT NULL
    )
''')

@app.route('/')
def index():
    return 'Welcome to the insecure SQL injection app!'

@app.route('/search')
def search():
    query = request.args.get('query', '')
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE name = '{query}'")
    results = cursor.fetchall()
    conn.close()
    return str(results)

if __name__ == '__main__':
    app.run(debug=True)
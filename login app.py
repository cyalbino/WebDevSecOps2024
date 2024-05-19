from flask import *
import sqlite3

app = Flask(__name__)

connection = sqlite3.connect("example.db")
cursor = connection.cursor()

# cursor.execute("CREATE TABLE IF NOT EXISTS users (name text, age integer, password text)")
# cursor.execute("INSERT INTO users (name, age, password) VALUES ('elo', 20, 'password')")
# connection.commit()

@app.route('/login', methods = ["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        conn = sqlite3.connect("example.db")
        cursor = conn.cursor()
        sql = "SELECT * FROM users where name = ? AND password = ?"
        execute_sql = cursor.execute(sql,(username,password))
        #sql = cursor.execute(f"SELECT * FROM users WHERE name = '{username}' AND password = '{password}'")
        data = execute_sql.fetchall()
        print(data)
        if (data):
            return "Login Success"
        else:
            return "Login Failed"
        
@app.route('/greet', methods = ["GET","POST"])
def greet():
    if request.method == "GET":
        return render_template("greet.html")
    elif request.method == "POST":
        name = request.form.get("name")
        return render_template("greet.html", name=name)
        #return "Hello {name}" // jinja has methods of sanitation already however for normal html files, needs sanitation

if __name__ == "__main__":
    app.run(debug=True,port=3001)
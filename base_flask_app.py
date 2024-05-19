from flask import Flask, request, render_template

app = Flask(__name__) 

@app.route('/login', methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "admin123":
            return render_template("success.html", current_username = username) # first arg is the html file, 

    return render_template("login.html")

@app.route('/register')
def register():
    return "Welcome to registration page."

@app.route('/')
def index():
    return "Hello this is the root directory."

@app.route('/greet', methods = ["GET", "POST"])
def greet():
    if request.method == "GET":
        return render_template("greet.html")
    elif request.method == "POST":
        name = request.form.get("name")
        return render_template("greet.html", name = name)

if __name__ == '__main__':
    app.run(debug=True,port=3000)
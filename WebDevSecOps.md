# Web Development and Security Operations 
## I. What is web developmnet?
- Client-side
- Server-side
  - How to handle a request, and how to respond to it

## II. What is security operations?
- Ensuring that web applications are secured
- Preventing and catching common vulnerabilities
  - SQL injection
  - Cross-site scripting

## III. What is Flask?
- Python Web Framework
  - microweb framework
- Advantages:
  - lightweight
  - for easier development of web servers
  - bare minimum
- 4 Lines of Code Web Server

### IV. What is HTTP?
- HyperText Transfer Protocol (HTTP)
- Client-Server Model
- Request-Respond Messages
- Hypertext Transfer

### V. Web Dev with Python Flask
#### How a web server works?
#### A. Registering routes in Flask
```python
@app.route('/') #Add route here
def index():
    return "This is the root directory." #Content

@app.route('/register')
def register():
    return "Welcome to registration page."
```

#### B. Handling Requests in Flask
- request.args (query parameters)
  ```python
  #127.0.0.1:8000/greet?name=win 
  @app.route('/greet')
  def greet():
    print(request.args)
    name = request.args.get("name")
    return "Hello " + name
  ```
  - Problem: Only applicable to publicly available data, not applicable for sensitive data
  - Get method for getting data
- request.forms (form data)

  Login.html
  ```html
  <form method = "post">
    <label>Username</label>
    <input type="text" name="username" placeholder="Enter username" id="">
    <label>Password</label>
    <input type="password" name="password" placeholder="Enter password" id="">
    <button type="submit">Submit</button>
  </form>
  ```

  Using render_template from Flask to return Login.html and use POST method
  ```python
  @app.route('/login', methods = ["GET", "POST"])
  def login():
    if request.method == "GET":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "admin123":
            return "Login Success"
        
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "admin123":
            return "Login Success"

    return render_template("login.html")
  ```
  - Solution: Applicable for sensitive data
  - Post method for inserting data
  - For flask to use render_template, html files must be placed in template folder
- request methods (GET, POST, etc)
#### C. Introduction to Jinja 2
- Templating engine for Flask
- Advantages of using templates
  ```python
  return render_template("success.html", current_username = username)
  #current_username is the jinja variable which can be used inside the success.html
  ```
#### D. Structured Query Language
- sqlite3 is a python database library
  ```python
  connection = sqlite3.connect("example.db")
  cursor = connection.cursor()

  cursor.execute("CREATE TABLE IF NOT EXISTS users (name text, age integer, password text)")
  cursor.execute("INSERT INTO users (name, age, password) VALUES ('elo', 20, 'password')")
  connection.commit()
  ```

#### E. Security Vulnerabilities
- SQL injection 
  ```python
  sql = cursor.execute(f"SELECT * FROM users WHERE name = '{username}' AND password = '{password}'")
  # '{password}' -> ' ' OR 1 = '1 ' then the password will always be TRUE
  ```
  - No sanitation of input validation
  - Example of SQL Injection attacks
  - Solution: Do not trust user input
  - Injecting own SQL code 
  - Prevention Techniques 
    - input validation
    - parameterized queries
- Cross-site Scripting (XSS)
  - Types of XSS
    1. Reflected
    2. Stored
    3. DOM Based
  - Examples of XSS Attacks
  - Inserting own code in HTML
  - Prevention Techniques
    - Input Validation
    - Parameterized queries
- Cross-site Request Forgery (CSRF)
  - Gets your user info and hijacks your account
  - Prevention Techniques
    - CSRF Tokens - unique identifier that shows this form is valid
    - Samesite Cookies
- Password Hashing
  - hash is used for integrity purposes
  - rainbow table attack 
    - predetermined common passwords with hash equivalence
    - hash is one way, always constant
  - salt and pepper 
    - random string or random code as prefix or suffix attached to hash equivalence of password 
  - Examples of hashing alorithms
    1. Bcrypt
    2. SHA256 Hash Generator
    3. Argon2
- Security Best Practices
    1. Input Validation
    2. Output Encoding
    3. Keeping software up-to-date


from flask import Flask, render_template, request, redirect, session, url_for
import pymysql

app = Flask(__name__)

# Database configuration
db = pymysql.connect(
    host='ca4_db',  # This is the name of the database container as defined in the Docker Compose file
    user='member3',
    password='mlops123',
    database='CA4',
    cursorclass=pymysql.cursors.DictCursor
)

@app.route('/')
def home():
    return redirect(url_for('signup'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']  # Get the password from the form
        cursor = db.cursor()
        sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
        cursor.execute(sql, (username, password))
        db.commit()
        cursor.close()
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']  # Get the password from the form
        cursor = db.cursor()
        sql = "SELECT username, password FROM users WHERE username = %s"
        cursor.execute(sql, (username,))
        user = cursor.fetchone()
        if user and password == user['password']:
            session['username'] = user['username']
            return redirect(url_for('welcome'))
    return render_template('login.html')

@app.route('/welcome')
def welcome():
    if 'username' in session:
        return render_template('welcome.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

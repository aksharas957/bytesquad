from flask import Flask, render_template,request, jsonify,render_template_string

import mysql.connector, json


app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# MySQL configuration
db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'bytesquad',
    'database': 'bytesquad'
}

# Create a MySQL connection
def get_db_connection():
    return mysql.connector.connect(**db_config)


@app.route('/show')
def show_users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)  # dictionary=True gives dicts instead of tuples
    cursor.execute("SELECT * FROM members")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return render_template('table.html',data=users)

if __name__ == '__main__':
    app.run(debug=True)


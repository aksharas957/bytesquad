from flask import Flask, render_template,request, jsonify,render_template_string

import mysql.connector, json

import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# MySQL configuration
# db_config = {
#     'host': '127.0.0.1',
#     'user': 'root',
#     'password': 'bytesquad',
#     'database': 'bytesquad'
# }

# # Create a MySQL connection
# def get_db_connection():
#     return mysql.connector.connect(**db_config)


# @app.route('/show')
# def show_users():
#     conn = get_db_connection()
#     cursor = conn.cursor(dictionary=True)  # dictionary=True gives dicts instead of tuples
#     cursor.execute("SELECT * FROM members")
#     users = cursor.fetchall()
#     cursor.close()
#     conn.close()
    
#     return render_template('table.html',data=users)

# if __name__ == '__main__':
#     app.run(debug=True)


# Replace with your actual Neon credentials
DB_URL ='postgresql://neondb_owner:npg_PGBFmEw0D8xV@ep-damp-cherry-aegep02p-pooler.c-2.us-east-2.aws.neon.tech/bytesquad-website?sslmode=require&channel_binding=require'


def get_db_connection():
    conn = psycopg2.connect(DB_URL)
    return conn

@app.route('/data')
def fetch_data():
    conn = None
    results = None
    description = []
    
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute('SELECT * FROM members LIMIT 10;')
        users = cur.fetchall()
        description = [desc[0] for desc in cur.description]
        cur.close()


        return render_template('table.html',column_names=description, results=users)
    except Exception as e:
        return jsonify({"error": str(e)})
    finally:
        if conn is not None:
            
            conn.close()

if __name__ == '__main__':
    app.run(debug=True)


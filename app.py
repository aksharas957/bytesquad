from flask import Flask, render_template,request, jsonify,render_template_string

import mysql.connector, json

import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


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

        cur.execute('SELECT * FROM members order by id LIMIT 10;')
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


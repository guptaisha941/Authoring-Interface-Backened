import pymysql
from app import app
from author import app
from config import mysql
from flask import jsonify
from flask import flash, request
from werkzeug.security import generate_password_hash, check_password_hash

cursor = None
conn = mysql.connect()
cursor = conn.cursor(pymysql.cursors.DictCursor)
conn = mysql.connect()
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS discourse (discourse_id int NOT NULL AUTO_INCREMENT, author_id int, no_sentences int, domain varchar(255), create_date datetime default now(), other_attributes VARCHAR(255),PRIMARY KEY (discourse_id),FOREIGN KEY (author_id) REFERENCES author(author_id))")
conn.commit()
cursor.close() 
conn.close() 

@app.route('/discourse/create', methods = ['POST'])
def create_discourse():
    try:
        con = None
        cursor = None
        _json = request.json
        _author_id = _json['author_id']
        _no_sentences = _json['no_sentences']
        _domain = _json['domain']
        _other_attributes = _json['other_attributes']
        if _author_id and _no_sentences and _domain and _other_attributes and request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)		
            sqlQuery = "INSERT INTO discourse(author_id, no_sentences, domain, other_attributes) VALUES(%s, %s, %s, %s)"
            bindData = (_author_id, _no_sentences,_domain, _other_attributes)            
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('discourse added successfully!')
            respone.status_code = 200
            return respone
        else:
            return showMessage()
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close() 

@app.route('/discourse')
def discourse():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT discourse_id, author_id, no_sentences, domain,create_date, other_attributes FROM discourse")
        disRows = cursor.fetchall()
        respone = jsonify(disRows)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()  

@app.route('/discourse/<int:discourse_id>')
def dis_details(discourse_id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT discourse_id , author_id, no_sentences, domain, create_date,other_attributes FROM discourse WHERE discourse_id =%s", discourse_id)
        disRow = cursor.fetchone()
        respone = jsonify(disRow)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close() 

@app.route('/discourse/update', methods=['PUT'])
def update_discourse():
    conn = None
    cursor = None
    try:
        _json = request.json
        _discourse_id = _json['discourse_id']
        _author_id = _json['author_id']
        _no_sentences = _json['no_sentences']
        _domain = _json['domain']
        # _create_date = _json['create_date']
        _other_attributes = _json['other_attributes']
        if _author_id and _no_sentences and _domain and _other_attributes and request.method == 'PUT':
            sql = "UPDATE discourse SET author_id=%s, no_sentences=%s, domain=%s, other_attributes=%s WHERE discourse_id=%s"
            data = (_author_id, _no_sentences, _domain, _other_attributes, _discourse_id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('discourse updated successfully!')
            resp.status_code = 200
            return resp
        else:
            return showMessage()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/discourse/delete/<int:discourse_id>', methods=['DELETE'])
def delete_discourse(discourse_id):
	conn = None
	cursor = None
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM discourse WHERE discourse_id=%s", (discourse_id,))
		conn.commit()
		resp = jsonify('discourse deleted successfully!')
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

@app.errorhandler(404)
def showMessage(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone
    
import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request
from werkzeug.security import generate_password_hash, check_password_hash

cursor = None
conn = mysql.connect()
cursor = conn.cursor(pymysql.cursors.DictCursor)
conn = mysql.connect()
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS author (author_id int AUTO_INCREMENT , author_name varchar(255), email varchar(255), password varchar(16), reviewer_role varchar(255), PRIMARY KEY(author_id))")
conn.commit()
cursor.close() 
conn.close() 


@app.route('/author/create', methods = ['POST'])
def create_auth():
    try:
        con = None
        cursor = None
        _json = request.json
        _author_name = _json['author_name']
        _email = _json['email']
        _password = _json['password']
        _reviewer_role = _json['reviewer_role']
        if _author_name and _email and _password and _reviewer_role and request.method == 'POST':
            _hashed_password = generate_password_hash(_password)
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)		
            sqlQuery = "INSERT INTO author(author_name, email, password, reviewer_role) VALUES(%s, %s, %s, %s)"
            bindData = (_author_name, _email,_password, _reviewer_role)            
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('author added successfully!')
            respone.status_code = 200
            return respone
        else:
            return showMessage()
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close() 

@app.route('/authors')
def author():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT author_id, author_name, email, password, reviewer_role FROM author")
        authRows = cursor.fetchall()
        respone = jsonify(authRows)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()  

@app.route('/author/<int:author_id>')
def auth_details(author_id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT author_id , author_name, email, password, reviewer_role FROM author WHERE author_id =%s", author_id)
        authRow = cursor.fetchone()
        respone = jsonify(authRow)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close() 

@app.route('/author/update', methods=['PUT'])
def update_author():
    conn = None
    cursor = None
    try:
        _json = request.json
        _author_id = _json['author_id']
        _author_name = _json['author_name']
        _email = _json['email']
        _password = _json['password']
        _reviewer_role = _json['reviewer_role']
        if _author_name and _email and _password and _reviewer_role and request.method == 'PUT':
            sql = "UPDATE author SET author_name=%s, email=%s, password=%s, reviewer_role=%s WHERE author_id=%s"
            data = (_author_name, _email, _password, _reviewer_role, _author_id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('author updated successfully!')
            resp.status_code = 200
            return resp
        else:
            return showMessage()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/author/delete/<int:author_id>', methods=['DELETE'])
def delete_author(author_id):
	conn = None
	cursor = None
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM author WHERE author_id=%s", (author_id,))
		conn.commit()
		resp = jsonify('author deleted successfully!')
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
    

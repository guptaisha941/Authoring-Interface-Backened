import pymysql
import json
from app import app
from author import app
from discourse import app
from config import mysql
from flask import jsonify
from flask import flash, request

cursor = None
conn = mysql.connect()
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS usr (author_id int,  discourse_id int, sentence_id int ,USR_ID int NOT NULL AUTO_INCREMENT, orignal_USR_json json,final_USR json,create_date datetime default now(),USR_status varchar(255),FOREIGN KEY (sentence_id) REFERENCES discourse (discourse_id) ,FOREIGN KEY (discourse_id) REFERENCES discourse(discourse_id),FOREIGN KEY (author_id) REFERENCES author(author_id), PRIMARY KEY (USR_ID))")
conn.commit()
cursor.close()
conn.close()

@app.route('/USR/create', methods = ['POST'])
def create_USR():
    try:
        con = None
        cursor = None
        _json = request.json
        _author_id = _json['author_id']
        _discourse_id = _json['discourse_id']
        _sentence_id = _json['sentence_id']
        _orignal_USR_json = _json['orignal_USR_json']
        _final_USR = _json['final_USR']
        _USR_status = _json['USR_status']
        if _author_id and _discourse_id and _sentence_id and _orignal_USR_json and _final_USR and _USR_status and request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)		
            sqlQuery = "INSERT INTO usr(author_id, discourse_id, sentence_id, orignal_USR_json, final_USR, USR_status) VALUES(%s, %s, %s, %s, %s, %s)"
            bindData = (_author_id, _discourse_id, _sentence_id, _orignal_USR_json, _final_USR, _USR_status)            
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('USR added successfully!')
            respone.status_code = 200
            return respone
        else:
            return showMessage()
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close() 
    
@app.route('/USR')
def USR():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT author_id, discourse_id, sentence_id, USR_ID, orignal_USR_json, final_USR, create_date, USR_status FROM usr")
        usrRows = cursor.fetchall()
        respone = jsonify(usrRows)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()  

@app.route('/USR/<int:USR_ID>')
def usr_details(USR_ID):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT author_id, discourse_id, sentence_id, USR_ID, orignal_USR_json, final_USR, create_date, USR_status FROM usr WHERE USR_ID =%s", USR_ID)
        usrRow = cursor.fetchone()
        respone = jsonify(usrRow)
        respone.status_code = 200
        return respone
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

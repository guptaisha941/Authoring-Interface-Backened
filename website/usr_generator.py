import pymysql
import json
from app import app
from author import app
from discourse import app
from usr import app
from config import mysql
from flask import jsonify
from flask import flash, request

cursor = None
conn = mysql.connect()
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS usr_generator (wx_sentence varchar(255),  usr json)")
conn.commit()
cursor.close()
conn.close()


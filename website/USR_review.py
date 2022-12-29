# import json
# import pymysql
# import requests
# from app import app
# from author import app
# from discourse import app
# from USR import app
# from config import mysql
# from flask import jsonify
# from flask import flash, request

# cursor = None
# conn = mysql.connect()
# cursor = conn.cursor()
# cursor.execute("CREATE TABLE IF NOT EXISTS USR_review (USR_id int,  reviewer_id int, review_status varchar(255) , review_date datetime default now(),change_note vrchar(255), FOREIGN KEY (USR_id) REFERENCES usr (USR_id) ,FOREIGN KEY (discourse_id) REFERENCES discourse(discourse_id))")

# conn.commit()
# cursor.close()
# conn.close()
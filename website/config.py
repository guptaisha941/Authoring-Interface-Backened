from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Ishagu@1'
app.config['MYSQL_DATABASE_DB'] = 'reviewsystem'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


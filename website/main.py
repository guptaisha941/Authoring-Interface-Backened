from app import app
from author import app
from discourse import app
from usr import app
from admin import app
import base64
import requests

if __name__ == "__main__":
    app.run()

# alter table discourse change sentences sentences varchar(1000)
# character set utf8mb4 collate utf8mb4_unicode_ci;
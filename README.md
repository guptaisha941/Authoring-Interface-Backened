# Authoring Interface Backened
## Setup & Installation
Make sure you have the latest version of Python installed.


```bash
git clone <repo-url>
```

```bash
pip install -r requirements.txt
```

## Running The Website

```bash
python main.py
```

## Viewing The API'S

### Author

 GET  - `http://127.0.0.1:5000/authors`
 
 GET  - `http://127.0.0.1:5000/author/<author_id>`
 
 POST - `http://127.0.0.1:5000/author/create`
 
 PUT  - `http://127.0.0.1:5000/author/update`
 
 DELETE - `http://127.0.0.1:5000/author/delete/<author_id>`
 
 ### Discourse

 GET  - `http://127.0.0.1:5000/discourse`
 
 GET  - `http://127.0.0.1:5000/discourse/<discourse_id>`
 
 POST - `http://127.0.0.1:5000/discourse/create`
 
 PUT  - `http://127.0.0.1:5000/discourse/update`
 
 DELETE - `http://127.0.0.1:5000/discourse/delete/<discourse_id>`

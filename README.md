# REST API ( FLASK )

## Requirements
```
pip install Flask
pip install SQLAlchemy==1.3.3
pip install Flask-RESTful==0.3.7
pip install Flask-JWT==0.3.2
```

## Run the App
```
cd flask_restFull/
python3 app.py
```

## Description
This is Flask REST project coded in python version 3.6

## Endpoints
  1. http://127.0.0.1:5000/register
  2. http://127.0.0.1:5000/auth
  3. http://127.0.0.1:5000/stores
  4. http://127.0.0.1:5000/items
  5. http://127.0.0.1:5000/item/item_name
  6. http://127.0.0.1:5000/store/store_id
  
## Live view 
open postman collection json file 
  1. https://flask-store-rex.herokuapp.com/register | POST
  2. https://flask-store-rex.herokuapp.com/auth | POST
  3. https://flask-store-rex.herokuapp.com/stores | GET
  4. https://flask-store-rex.herokuapp.com/items  | GET
  5. https://flask-store-rex.herokuapp.com/items/item_name  | POST, PUT
  6. https://flask-store-rex.herokuapp.com/store/store_id | POST


## Implementation
This is implemented using Flask and it is a store REST API

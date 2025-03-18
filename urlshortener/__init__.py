from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '3d6f45a5fc12445dbac2f59c3b6c7cb1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@mysqldb:3306/urlshortener'
db = SQLAlchemy(app)

from urlshortener import routes,models

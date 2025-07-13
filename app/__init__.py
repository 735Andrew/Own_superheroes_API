from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_URL


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL

db = SQLAlchemy(app)


from app import routes, models

with app.app_context():
    db.create_all()

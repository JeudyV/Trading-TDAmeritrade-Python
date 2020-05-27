from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

print("Flask!")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234@localhost:3306/td_acces_token_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
migrate = Migrate(app, db)
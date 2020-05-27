from sqlalchemy import Column, Integer, String
import sqlalchemy
from datetime import datetime

from flask_app import app, db

class token(db.Model):
    __table_args__ = {'extend_existing': True} 
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    acces_token = db.Column(db.Integer, nullable=False)
    created_at = sqlalchemy.Column(sqlalchemy.DateTime, default=lambda: datetime.utcnow())
    updated_at = sqlalchemy.Column(sqlalchemy.DateTime, default=lambda: datetime.utcnow(), onupdate=lambda: datetime.utcnow())

class data_indicator(db.Model): 
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    indicator = db.Column(db.String(50), nullable=False)
    exchange = db.Column(db.String(50), nullable=False)
    symbol = db.Column(db.String(50), nullable=False)
    interval = db.Column(db.String(50), nullable=False)
    period = db.Column(db.Integer, nullable=False)
    value = db.Column(db.Integer, nullable=False)
    created_at = sqlalchemy.Column(sqlalchemy.DateTime, default=lambda: datetime.utcnow())
    
#app.run(debug=True)
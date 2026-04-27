from flask_sqlalchemy import SQLAlchemy
from datetime import date

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    UserID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    FirstName = db.Column(db.String(50), nullable=False)
    LastName = db.Column(db.String(50), nullable=False)
    Email = db.Column(db.String(100), nullable=False, unique=True)
    JoinDate = db.Column(db.Date, default=date.today)
    RecordStatus_Meta = db.Column(db.String(50), default='Active_System')
    orders = db.relationship('Order', backref='user', lazy=True)

class Vendor(db.Model):
    __tablename__ = 'vendors'
    VendorID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    VendorName = db.Column(db.String(100), nullable=False)
    CuisineType = db.Column(db.String(50), nullable=False)
    AddedBy_Meta = db.Column(db.String(50), default='Admin_01')
    orders = db.relationship('Order', backref='vendor', lazy=True)

class Order(db.Model):
    __tablename__ = 'orders'
    OrderID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    UserID = db.Column(db.Integer, db.ForeignKey('users.UserID'), nullable=False)
    VendorID = db.Column(db.Integer, db.ForeignKey('vendors.VendorID'), nullable=False)
    OrderDate = db.Column(db.Date, default=date.today)
    DeliveryDate = db.Column(db.Date, nullable=True)
    SubTotal = db.Column(db.Float, nullable=False)
    TotalWithTax = db.Column(db.Float)
    LastModified_Meta = db.Column(db.String(50), default='System_Auto')
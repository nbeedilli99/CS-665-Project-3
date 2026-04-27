-- CS665 Project 3 - Final SQL Schema (3rd Normal Form)
-- Application: Local Food & Bakery Delivery App

DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS vendors;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    UserID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) NOT NULL UNIQUE,
    JoinDate DATE DEFAULT CURRENT_DATE,
    RecordStatus_Meta VARCHAR(50) DEFAULT 'Active_System'
);

CREATE TABLE vendors (
    VendorID INTEGER PRIMARY KEY AUTOINCREMENT,
    VendorName VARCHAR(100) NOT NULL,
    CuisineType VARCHAR(50) NOT NULL,
    AddedBy_Meta VARCHAR(50) DEFAULT 'Admin_01'
);

CREATE TABLE orders (
    OrderID INTEGER PRIMARY KEY AUTOINCREMENT,
    UserID INTEGER NOT NULL,
    VendorID INTEGER NOT NULL,
    OrderDate DATE DEFAULT CURRENT_DATE,
    DeliveryDate DATE,
    SubTotal DECIMAL(10,2) NOT NULL,
    TotalWithTax DECIMAL(10,2),
    LastModified_Meta VARCHAR(50) DEFAULT 'System_Auto',
    FOREIGN KEY (UserID) REFERENCES users(UserID),
    FOREIGN KEY (VendorID) REFERENCES vendors(VendorID)
);
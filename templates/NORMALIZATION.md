# Normalization Report
## CS665 Project 3 — Local Food & Bakery Delivery App

---

## 1. Original Functional Dependencies

### Users Table
- UserID → FirstName, LastName, Email, JoinDate, RecordStatus_Meta
- Email → UserID (Email is unique)

### Vendors Table
- VendorID → VendorName, CuisineType, AddedBy_Meta

### Orders Table
- OrderID → UserID, VendorID, OrderDate, DeliveryDate, SubTotal, TotalWithTax, LastModified_Meta
- OrderID → UserID (FK reference to Users)
- OrderID → VendorID (FK reference to Vendors)

---

## 2. Anomaly Identification

### Potential Update Anomaly
If a vendor changes their name, it only needs to be updated in the Vendors table.
Because VendorName is not stored in Orders (only VendorID), there is no risk
of inconsistency across multiple rows.

### Potential Insertion Anomaly
A vendor can be inserted into the Vendors table independently without needing
an order to exist first. Similarly, users can be added without orders.

### Potential Deletion Anomaly
Deleting all orders for a user does NOT delete the user record. User and vendor
data is preserved in their own tables, avoiding deletion anomalies.

---

## 3. Normal Form Analysis

### First Normal Form (1NF) ✅
- All columns contain atomic values (no lists or repeating groups)
- Each table has a defined primary key
- No duplicate rows exist

### Second Normal Form (2NF) ✅
- All tables use a single-column primary key
- No partial dependencies exist
- Every non-key attribute is fully dependent on the entire primary key

### Third Normal Form (3NF) ✅
- No transitive dependencies exist
- Example: In Orders, SubTotal does not determine UserID or VendorID
- TotalWithTax is derived from SubTotal (computed column, not a transitive dependency)
- All non-key attributes depend only on the primary key

---

## 4. Decomposition Steps

**No decomposition was required.** The original schema from Project 2 already
satisfies all requirements of 3rd Normal Form because:

1. All non-key attributes depend directly on their table's primary key
2. No non-key attribute determines another non-key attribute
3. Foreign keys (UserID, VendorID in Orders) properly reference parent tables

---

## 5. Final Relational Schema
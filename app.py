from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, User, Vendor, Order
from datetime import date
from sqlalchemy import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///food_delivery.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'cs665secretkey'

db.init_app(app)

with app.app_context():
    db.create_all()

# ---------- DASHBOARD ----------
@app.route('/')
def dashboard():
    total_users = db.session.query(func.count(User.UserID)).scalar()
    total_revenue = db.session.query(func.sum(Order.SubTotal)).scalar() or 0
    avg_order = db.session.query(func.avg(Order.SubTotal)).scalar() or 0
    total_orders = db.session.query(func.count(Order.OrderID)).scalar()
    return render_template('index.html',
        total_users=total_users,
        total_revenue=round(total_revenue, 2),
        avg_order=round(avg_order, 2),
        total_orders=total_orders)

# ---------- USERS ----------
@app.route('/users')
def users():
    all_users = User.query.all()
    return render_template('users.html', users=all_users)

@app.route('/users/add', methods=['POST'])
def add_user():
    fn = request.form.get('FirstName', '').strip()
    ln = request.form.get('LastName', '').strip()
    em = request.form.get('Email', '').strip()
    if not fn or not ln or not em:
        flash('All fields are required.', 'danger')
        return redirect(url_for('users'))
    if User.query.filter_by(Email=em).first():
        flash('Email already exists.', 'danger')
        return redirect(url_for('users'))
    new_user = User(FirstName=fn, LastName=ln, Email=em)
    db.session.add(new_user)
    db.session.commit()
    flash('User added successfully!', 'success')
    return redirect(url_for('users'))

@app.route('/users/edit/<int:id>', methods=['POST'])
def edit_user(id):
    u = User.query.get_or_404(id)
    u.FirstName = request.form.get('FirstName', '').strip()
    u.LastName = request.form.get('LastName', '').strip()
    u.Email = request.form.get('Email', '').strip()
    if not u.FirstName or not u.LastName or not u.Email:
        flash('All fields are required.', 'danger')
        return redirect(url_for('users'))
    db.session.commit()
    flash('User updated!', 'success')
    return redirect(url_for('users'))

@app.route('/users/delete/<int:id>')
def delete_user(id):
    u = User.query.get_or_404(id)
    db.session.delete(u)
    db.session.commit()
    flash('User deleted.', 'warning')
    return redirect(url_for('users'))

# ---------- VENDORS ----------
@app.route('/vendors')
def vendors():
    all_vendors = Vendor.query.all()
    return render_template('vendors.html', vendors=all_vendors)

@app.route('/vendors/add', methods=['POST'])
def add_vendor():
    name = request.form.get('VendorName', '').strip()
    cuisine = request.form.get('CuisineType', '').strip()
    if not name or not cuisine:
        flash('All fields are required.', 'danger')
        return redirect(url_for('vendors'))
    db.session.add(Vendor(VendorName=name, CuisineType=cuisine))
    db.session.commit()
    flash('Vendor added!', 'success')
    return redirect(url_for('vendors'))
 
@app.route('/vendors/delete/<int:id>')
def delete_vendor(id):
    v = Vendor.query.get_or_404 (id)
    db.session.delete(v)
    db.session.commit()
    flash('Vendor deleted.', 'warning')
    return redirect(url_for('vendors'))

# ---------- ORDERS ----------
@app.route('/orders')
def orders():
    all_orders = Order.query.all()
    all_users = User.query.all()
    all_vendors = Vendor.query.all()
    return render_template('orders.html',
        orders=all_orders, users=all_users, vendors=all_vendors)

@app.route('/orders/add', methods=['POST'])
def add_order():
    try:
        uid = int(request.form.get('UserID'))
        vid = int(request.form.get('VendorID'))
        subtotal = float(request.form.get('SubTotal'))
        if subtotal <= 0:
            flash('SubTotal must be greater than 0.', 'danger')
            return redirect(url_for('orders'))
    except (ValueError, TypeError):
        flash('Invalid input values.', 'danger')
        return redirect(url_for('orders'))
    try:
        new_order = Order(
            UserID=uid, VendorID=vid,
            SubTotal=subtotal,
            TotalWithTax=round(subtotal * 1.08, 2),
            OrderDate=date.today(),
            LastModified_Meta='System_Auto'
        )
        db.session.add(new_order)
        db.session.commit()
        flash('Order placed successfully!', 'success')
    except Exception:
        db.session.rollback()
        flash('Transaction failed. Order not saved.', 'danger')
    return redirect(url_for('orders'))

@app.route('/orders/delete/<int:id>')

def delete_order(id):
    o = Order.query.get_or_404(id)
    db.session.delete(o)
    db.session.commit()
    flash('Order deleted.', 'warning')
    return redirect(url_for('orders'))

if __name__ == '__main__':
    app.run(debug= True)
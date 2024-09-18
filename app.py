from flask import Flask, render_template, request, redirect, url_for
from models import db, Room, Employee, Customer

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hotel.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

# หน้าแรก
@app.route('/')
def index():
    return render_template('index.html')

# เส้นทางสำหรับการจัดการห้อง
@app.route('/rooms')
def manage_rooms():
    rooms = Room.query.all()  # ดึงข้อมูลห้องจากฐานข้อมูล
    return render_template('rooms.html', rooms=rooms)

# เส้นทางสำหรับการเพิ่มห้อง
@app.route('/add_room', methods=['POST'])
def add_room():
    room_name = request.form.get('room_name')
    new_room = Room(name=room_name)
    db.session.add(new_room)
    db.session.commit()
    return redirect(url_for('manage_rooms'))

# เส้นทางสำหรับการลบห้อง
@app.route('/delete_room/<int:id>', methods=['POST'])
def delete_room(id):
    room = Room.query.get(id)
    if room:
        db.session.delete(room)
        db.session.commit()
    return redirect(url_for('manage_rooms'))

# เส้นทางสำหรับการแก้ไขห้อง
@app.route('/edit_room/<int:id>', methods=['GET', 'POST'])
def edit_room(id):
    room = Room.query.get(id)
    if request.method == 'POST':
        new_name = request.form.get('room_name')
        if room:
            room.name = new_name
            db.session.commit()
        return redirect(url_for('manage_rooms'))
    return render_template('edit_room.html', room=room)

# จัดการพนักงาน
@app.route('/employees')
def manage_employees():
    employees = Employee.query.all()  # ดึงข้อมูลพนักงานจากฐานข้อมูล
    return render_template('employees.html', employees=employees)

@app.route('/add_employee', methods=['POST'])
def add_employee():
    employee_name = request.form.get('employee_name')
    new_employee = Employee(name=employee_name)
    db.session.add(new_employee)
    db.session.commit()
    return redirect(url_for('manage_employees'))
    
@app.route('/delete_employee/<int:id>', methods=['POST'])
def delete_employee(id):
    employee = Employee.query.get(id)
    if employee:
        db.session.delete(employee)
        db.session.commit()
    return redirect(url_for('manage_employees'))

@app.route('/edit_employee/<int:id>', methods=['GET', 'POST'])
def edit_employee(id):
    employee = Employee.query.get(id)
    if request.method == 'POST':
        new_name = request.form.get('employee_name')
        if employee:
            employee.name = new_name
            db.session.commit()
        return redirect(url_for('manage_employees'))
    return render_template('edit_employee.html', employee=employee)

# จัดการลูกค้า
@app.route('/customers')
def manage_customers():
    customers = Customer.query.all()  # ดึงข้อมูลลูกค้าจากฐานข้อมูล
    return render_template('customers.html', customers=customers)

@app.route('/add_customer', methods=['POST'])
def add_customer():
    customer_name = request.form.get('customer_name')
    new_customer = Customer(name=customer_name)
    db.session.add(new_customer)
    db.session.commit()
    return redirect(url_for('manage_customers'))

@app.route('/delete_customer/<int:id>', methods=['POST'])
def delete_customer(id):
    customer = Customer.query.get(id)
    if customer:
        db.session.delete(customer)
        db.session.commit()
    return redirect(url_for('manage_customers'))

@app.route('/edit_customer/<int:id>', methods=['GET', 'POST'])
def edit_customer(id):
    customer = Customer.query.get(id)
    if request.method == 'POST':
        new_name = request.form.get('customer_name')
        if customer:
            customer.name = new_name
            db.session.commit()
        return redirect(url_for('manage_customers'))
    return render_template('edit_customer.html', customer=customer)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001, threaded=True, use_reloader=False)

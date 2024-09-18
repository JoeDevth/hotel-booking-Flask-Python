from flask import Flask, render_template, request, redirect, url_for
from models import db, Room, Employee, Customer

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hotel.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_request
def create_tables():
    db.create_all()

# หน้าแรก
@app.route('/')
def index():
    return render_template('index.html')

# เส้นทางสำหรับการจัดการห้อง
@app.route('/rooms')
def manage_rooms():
    # เพิ่มรหัสเพื่อดึงข้อมูลห้องจากฐานข้อมูล
    rooms = [{'id': 1, 'name': 'Room 1'}, {'id': 2, 'name': 'Room 2'}]  # ตัวอย่างข้อมูลห้อง
    return render_template('rooms.html', rooms=rooms)

# เส้นทางสำหรับการเพิ่มห้อง
@app.route('/add_room', methods=['POST'])
def add_room():
    room_name = request.form.get('room_name')
    # เพิ่มรหัสเพื่อบันทึกห้องในฐานข้อมูล
    return redirect(url_for('manage_rooms'))

# เส้นทางสำหรับการลบห้อง
@app.route('/delete_room/<int:id>', methods=['POST'])
def delete_room(id):
    if request.method == 'POST':
        # ลบข้อมูลตาม ID
        return redirect(url_for('manage_rooms'))

# เส้นทางสำหรับการแก้ไขห้อง
@app.route('/edit_room/<int:id>', methods=['GET', 'POST'])
def edit_room(id):
    if request.method == 'POST':
        new_name = request.form.get('room_name')
        # เพิ่มรหัสเพื่ออัปเดตชื่อห้องในฐานข้อมูล
        return redirect(url_for('manage_rooms'))
    # เพิ่มรหัสเพื่อดึงข้อมูลห้องที่ต้องการแก้ไข
    room = {'id': id, 'name': 'Example Room'}  # ตัวอย่างข้อมูลห้อง
    return render_template('edit_room.html', room=room)


# จัดการพนักงาน
@app.route('/employees')
def manage_employees():
    employees = Employee.query.all()
    return render_template('employees.html', employees=employees)

@app.route('/add_employee', methods=['POST'])
def add_employee():
    employee_name = request.form['employee_name']
    new_employee = Employee(name=employee_name)
    db.session.add(new_employee)
    db.session.commit()
    return redirect(url_for('manage_employees'))

@app.route('/delete_employee/<int:id>')
def delete_employee(id):
    employee = Employee.query.get(id)
    db.session.delete(employee)
    db.session.commit()
    return redirect(url_for('manage_employees'))

@app.route('/edit_employee/<int:id>', methods=['GET', 'POST'])
def edit_employee(id):
    employee = Employee.query.get(id)
    if request.method == 'POST':
        employee.name = request.form['employee_name']
        db.session.commit()
        return redirect(url_for('manage_employees'))
    return render_template('edit_employee.html', employee=employee)

# จัดการลูกค้า
@app.route('/customers')
def manage_customers():
    customers = Customer.query.all()
    return render_template('customers.html', customers=customers)

@app.route('/add_customer', methods=['POST'])
def add_customer():
    customer_name = request.form['customer_name']
    new_customer = Customer(name=customer_name)
    db.session.add(new_customer)
    db.session.commit()
    return redirect(url_for('manage_customers'))

@app.route('/delete_customer/<int:id>')
def delete_customer(id):
    customer = Customer.query.get(id)
    db.session.delete(customer)
    db.session.commit()
    return redirect(url_for('manage_customers'))

@app.route('/edit_customer/<int:id>', methods=['GET', 'POST'])
def edit_customer(id):
    customer = Customer.query.get(id)
    if request.method == 'POST':
        customer.name = request.form['customer_name']
        db.session.commit()
        return redirect(url_for('manage_customers'))
    return render_template('edit_customer.html', customer=customer)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001, threaded=True , use_reloader=False)

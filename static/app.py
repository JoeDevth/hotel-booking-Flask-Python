from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Mock Data
rooms = []
employees = []
customers = []

# หน้าแรก
@app.route('/')
def index():
    return render_template('index.html')

# จัดการห้องพัก
@app.route('/rooms')
def manage_rooms():
    return render_template('rooms.html', rooms=rooms)

@app.route('/add_room', methods=['POST'])
def add_room():
    room_name = request.form['room_name']
    rooms.append(room_name)
    return redirect(url_for('manage_rooms'))

@app.route('/delete_room/<int:index>')
def delete_room(index):
    rooms.pop(index)
    return redirect(url_for('manage_rooms'))

# จัดการพนักงาน
@app.route('/employees')
def manage_employees():
    return render_template('employees.html', employees=employees)

@app.route('/add_employee', methods=['POST'])
def add_employee():
    employee_name = request.form['employee_name']
    employees.append(employee_name)
    return redirect(url_for('manage_employees'))

@app.route('/delete_employee/<int:index>')
def delete_employee(index):
    employees.pop(index)
    return redirect(url_for('manage_employees'))

# จัดการลูกค้า
@app.route('/customers')
def manage_customers():
    return render_template('customers.html', customers=customers)

@app.route('/add_customer', methods=['POST'])
def add_customer():
    customer_name = request.form['customer_name']
    customers.append(customer_name)
    return redirect(url_for('manage_customers'))

@app.route('/delete_customer/<int:index>')
def delete_customer(index):
    customers.pop(index)
    return redirect(url_for('manage_customers'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001, threaded=True , use_reloader=False)

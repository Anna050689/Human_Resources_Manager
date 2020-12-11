from app import app
from app import db
from models import Department, Employee
from flask import render_template, request, flash, redirect, url_for, jsonify, g
from sqlalchemy.sql import func, and_
from datetime import datetime


@app.route('/')
def index():
    """
    This function responds to request for / ,
    forms the query result as a list of departments with such parameters
    as id, name, manager, phone, average salary, count of employees.
    The query result is passed as an argument to render_template function.

    :return: the rendered template 'index.html'
    """
    departments = db.session.query(
        Department.id, Department.name, Department.manager, Department.phone,
        func.round(func.avg(Employee.salary), 2).label('average_salary'), \
        func.count(Employee.id).label('count_of_employees')).select_from(Department).join(Employee,
                                                                                          isouter=True).group_by(
        Department.id)
    return render_template('index.html', departments=departments)


@app.route('/employees', methods = ['GET'])
def view_employees():
    """
    This function responds to request for /employees ,
    forms the query result as a list of employees.
    The query result is passed as an argument to
    render_template function.

    :return: the rendered template 'view_employees.html'
    """
    employees = db.session.query(Employee)
    return render_template('view_employees.html', employees=employees)


@app.route('/employees/filter', methods=['POST'])
def view_employees_filter():
    """
    This function responds to request for /employees/filter ,
    forms the query result as a list of employees filtered by the birth date.
    The query result is passed as an argument to render_template function.

    :return: the rendered template 'view_employees.html'
    """
    if request.method == 'POST':
        birth_date = request.form.get('birth_date', '')
        if birth_date != '':
            employees = db.session.query(Employee).filter(Employee.birth_date == birth_date).all()
        else:
            employees = db.session.query(Employee)
        return render_template('view_employees.html', employees=employees)


@app.route('/employees/filter_by_period', methods=['POST'])
def view_employees_filter_by_period():
    """
    This function responds to request for /employees/filter_by_period ,
    forms the query result as a list of employees who were born in a fixed period.
    The query result is passed as an argument to render_template function.

    :return: the rendered template 'view_employees.html'
    """
    if request.method == 'POST':
        born_from = request.form.get('born_from') or '1900-01-01'
        born_to = request.form.get('born_to') or '2100-01-01'
        employees = db.session.query(Employee).filter(and_(func.date(Employee.birth_date) >= born_from), \
                                                      func.date(Employee.birth_date) <= born_to).order_by(
            Employee.birth_date).all()
        return render_template('view_employees.html', employees=employees)


@app.route('/employee', methods=['POST'])
def add_employee():
    """
    This function responds to request for /employee ,
    adds to the database the record of the new employee.

    :return: the result of redirect function
    """
    session = db.session

    try:
        department_name = request.form['department_name']
        department = get_department_by_name(session, department_name)
        employee = extract_employee_data(request.form, department)
        session.add(employee)
        session.commit()

        flash("The record of the employee was inserted successfully")
    except TypeError:
        session.rollback()
        flash("The employee's department is absent. The record of this employee wasn't inserted.")
    finally:
        session.close()
        return redirect(url_for('view_employees'))


def get_department_by_name(session, name):
    """
    Get Department entity by given name
    :param session: data base session
    :param name: department name
    :return: Department entity
    """
    department = session.query(Department).filter(Department.name == name).first()
    if department is not None:
        return department
    else:
        raise TypeError(f"Department with name {name} was not found")


def extract_employee_data(form, department):
    """
    Extract data from HTTP form by field name

    :param form: HTTP Form (dictionary)
    :param department: reference to particular Department entity
    :return: Employee entity
    """
    first_name = form['first_name']
    patronymic = form['patronymic']
    last_name = form['last_name']
    age = form['age']
    birth_date = form['birth_date']
    phone = form['phone']
    position = form['position']
    experience = form['experience']
    salary = form['salary']

    return Employee(first_name, patronymic, last_name, age, birth_date,
                    phone, position, experience, department.id, salary)


# @app.route('/update/employee', methods=['GET', 'POST'])
# def update_employee():
#     """
#     This function responds to request for /update/employee ,
#     updates the record of the employee in the database.
#
#     :return: the result of the redirect function
#     """
#
#     if request.method == 'POST':
#         updated_data = Employee.query.get(request.form.get('id'))
#
#         try:
#             updated_data.first_name = request.form['first_name']
#             updated_data.patronymic = request.form['patronymic']
#             updated_data.last_name = request.form['last_name']
#             updated_data.age = request.form['age']
#             updated_data.birth_date = request.form['birth_date']
#             updated_data.phone = request.form['phone']
#             updated_data.position = request.form['position']
#             updated_data.experience = request.form['experience']
#             updated_data.salary = request.form['salary']
#             department_name = request.form['department_name']
#             updated_data.department_id = \
#             db.session.query(Department.id).filter(Department.name == department_name).first()[0]
#         except TypeError:
#             updated_data.department_id = None
#             flash("The employee's department is absent. The record's field of the department is empty.")
#
#         db.session.commit()
#         flash("The record of the employee was updated successfully")
#
#         return redirect(url_for('view_employees'))
#     



@app.route('/delete/employee/<id>', methods=['GET', 'POST'])
def delete(id):
    """
    This function responds to request for /delete/employee/<id>
    with one matching employee from employees and removes
    the record of the employee in the database.

    :param id: id of the employee

    :return: the result of redirect function
    """
    employee = Employee.query.get(id)
    db.session.delete(employee)
    db.session.commit()
    flash("The record of the employee was deleted successfully")

    return redirect(url_for('view_employees'))


@app.route('/insert/department', methods=['POST'])
def insert_department():
    """
    This function responds to request for /insert/department ,
    adds the record of new department to the database.

    :return: the result of redirect function
    """

    if request.method == 'POST':
        name = request.form['name']
        manager = request.form['manager']
        phone = request.form['phone']

        department = Department(name, manager, phone)
        db.session.add(department)
        db.session.commit()

        flash("The record of the department was inserted successfully")

        return redirect(url_for('index'))


@app.route('/update/department', methods=['GET', 'POST'])
def update_department():
    """
    This function responds to request for /update/department ,
    updates the record of the department in the database.

    :return: the result of the redirect function
    """
    if request.method == 'POST':
        updated_data = Department.query.get(request.form.get('id'))

        updated_data.name = request.form['name']
        updated_data.manager = request.form['manager']
        updated_data.phone = request.form['phone']
        updated_data.created_on = datetime.now()

        db.session.commit()
        flash("The record of the employee was updated successfully")

        return redirect(url_for('index'))


@app.route('/delete/department/<id>', methods=['GET', 'POST'])
def delete_department(id):
    """
    This function responds to request for /delete/department/<id>
    with one matching department from departments and removes
    the record of the department in the database.

    :param id: id of the department
    :return: the result of redirect function
    """
    department = Department.query.get(id)
    db.session.delete(department)
    db.session.commit()

    flash("The record of the department was deleted successfully")

    return redirect(url_for('index'))


@app.route('/search/employee', methods=['POST'])
def search_employee():
    """
    This function responds to request for /search/employee ,
    forms the query result as a list of employees filtered
    by the last name.
    The query result is passed as an argument to render_template
    function.

    :return: the rendered template('view_employees.html')
    """
    if request.method == 'POST':
        last_name = request.form.get('last_name', '')
        if last_name != '':
            employees = db.session.query(Employee).filter(Employee.last_name == last_name).all()
            return render_template('view_employees.html', employees=employees)
        else:
            employees = db.session.query(Employee).all()
            return render_template('view_employees.html', employees=employees)

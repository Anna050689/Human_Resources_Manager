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
    session = db.session
    departments = select_departments()
    session.close()
    return render_template('index.html', departments=departments)


def select_departments():
    """
    Select departments as a list of departments
    with such parameters as id, name, manager,
    phone, average salary, count of employees.
    :return: the list of departments
    """
    session = db.session
    departments = session.query(Department.id, Department.name, Department.manager, \
                                Department.phone,func.round(func.avg(Employee.salary), 2).label('average_salary'), \
                                func.count(Employee.id).label('count_of_employees')) \
                         .select_from(Department).join(Employee,isouter=True) \
                         .group_by(Department.id)
    session.close()
    return departments


@app.route('/employees', methods=['GET'])
def view_employees():
    """
    This function responds to request for /employees ,
    forms the query result as a list of employees.
    The query result is passed as an argument to
    render_template function.

    :return: the rendered template 'view_employees.html'
    """
    session = db.session
    employees = select_employees()
    session.close()
    return render_template('view_employees.html', employees=employees)

def select_employees():
    """
    Select employees as a list of employees with such parameters
    as id, first_name, patronymic, last_name, age, birth_date,
    phone, position, experience, department_name, salary.
    :return: the list of departments
    """
    session = db.session
    employees = session.query(Employee.id, Employee.first_name, Employee.patronymic, Employee.last_name, \
                              Employee.age, Employee.birth_date, Employee.phone, Employee.position, \
                              Employee.experience, Department.name.label('department_name'), Employee.salary) \
                        .select_from(Employee).join(Department, isouter=True).all()
    session.close()
    return employees



@app.route('/employees/filter', methods=['POST'])
def view_employees_filter():
    """
    This function responds to request for /employees/filter ,
    forms the query result as a list of employees filtered by the birth date.
    The query result is passed as an argument to render_template function.

    :return: the rendered template 'view_employees.html'
    """
    if request.method == 'POST':
        session = db.session
        birth_date = request.form.get('birth_date', '')
        if birth_date != '':
            employees = select_employees_by_filter(birth_date)
        else:
            employees = select_employees()
        session.close()
        return render_template('view_employees.html', employees=employees)

def select_employees_by_filter(birth_date):
    """
    Select employees who were born on a certain birth date.
    :param birth_date: the birth date of the employee
    :return: the list of employees
    """
    session = db.session
    employees = session.query(Employee.id, Employee.first_name, Employee.patronymic, Employee.last_name, \
                              Employee.age, Employee.birth_date, Employee.phone, Employee.position, \
                              Employee.experience, Employee.salary, Department.name.label('department_name')) \
                        .select_from(Employee).join(Department) \
                        .filter(Employee.birth_date == birth_date).order_by(Employee.birth_date).all()
    session.close()
    return employees


@app.route('/employees/filter_by_period', methods=['POST'])
def view_employees_filter_by_period():
    """
    This function responds to request for /employees/filter_by_period ,
    forms the query result as a list of employees who were born in a fixed period.
    The query result is passed as an argument to render_template function.

    :return: the rendered template 'view_employees.html'
    """
    session = db.session

    born_from = request.form.get('born_from') or '1900-01-01'
    born_to = request.form.get('born_to') or '2100-01-01'

    employees = select_employee_by_period(born_to, born_from)
    session.close()
    return render_template('view_employees.html', employees=employees)

def select_employee_by_period(born_to, born_from):
    """
    Select employees who were born in a fixed period.
    :param born_to: the start date of a fixed period.
    :param born_from: the end date of a fixed period.
    :return: the list of employees
    """
    session = db.session
    employees = session.query(Employee.first_name, Employee.patronymic, Employee.last_name, Employee.birth_date, \
                Employee.age, Employee.phone, Employee.position, Employee.experience, Employee.salary,
                Department.name.label('department_name')) \
                .select_from(Employee).join(Department,isouter=True).filter(and_(func.date(Employee.birth_date) >= born_from), \
                func.date(Employee.birth_date) <= born_to).order_by(Employee.birth_date).all()
    session.close()
    return employees


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
    Extract data from HTTP form

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


@app.route('/update/employee', methods=['GET', 'POST'])
def update_employee():
    """
    This function responds to request for /update/employee ,
    updates the record of the employee in the database.

    :return: the result of the redirect function
    """
    session = db.session()
    if request.method == 'POST':
        department_name = request.form['department_name']
        updated_data = Employee.query.get(request.form.get('id'))

        try:
            updated_data.first_name = request.form['first_name']
            updated_data.patronymic = request.form['patronymic']
            updated_data.last_name = request.form['last_name']
            updated_data.age = request.form['age']
            updated_data.birth_date = request.form['birth_date']
            updated_data.phone = request.form['phone']
            updated_data.position = request.form['position']
            updated_data.experience = request.form['experience']
            updated_data.salary = request.form['salary']
            updated_data.department_name = session.query(Department.name) \
                                                  .select_from(Employee) \
                                                  .join(Department) \
                                                  .filter(Department.id == Employee.department_id)
            updated_data.department_id = session.query(Department.id) \
                                                .filter(Department.name == department_name).first()[0]
        except TypeError:
            updated_data.department_id = None
            flash("The employee's department is absent. The record's field of the department is empty.")

        session.commit()
        session.close()
        flash("The record of the employee was updated successfully")

        return redirect(url_for('view_employees'))


@app.route('/employee/<id>', methods=['GET', 'POST'])
def delete_employee(id):
    """
    This function responds to request for /employee/<id>
    with one matching employee from employees and removes
    the record of the employee in the database.

    :param id: id of the employee

    :return: the result of redirect function
    """
    session = db.session()

    employee = extract_employee_by_id(id)
    session.delete(employee)
    session.commit()
    session.close()
    flash("The record of the employee was deleted successfully")

    return redirect(url_for('view_employees'))


def extract_employee_by_id(id):
    """
    Extract data of employee from the data base by id
    :param id: id of Employee entity
    :return: Employee entity
    """
    employee = Employee.query.get(id)
    return employee


@app.route('/department', methods=['POST'])
def add_department():
    """
    This function responds to request for /department ,
    adds the record of new department to the database.

    :return: the result of redirect function
    """
    session = db.session
    department = extract_department_data()
    session.add(department)
    session.commit()

    flash("The record of the department was inserted successfully")

    return redirect(url_for('index'))


def extract_department_data():
    """
    Extract data from HTTP form

    :return: Department entity
    """
    name = request.form['name']
    manager = request.form['manager']
    phone = request.form['phone']

    department = Department(name, manager, phone)
    return department


@app.route('/update/department', methods=['GET', 'POST'])
def update_department():
    """
    This function responds to request for /update/department ,
    updates the record of the department in the database.

    :return: the result of the redirect function
    """
    session = db.session

    if request.method == 'POST':
        updated_data = Department.query.get(request.form.get('id'))

        updated_data.name = request.form['name']
        updated_data.manager = request.form['manager']
        updated_data.phone = request.form['phone']
        updated_data.created_on = datetime.now()

        session.commit()
        session.close()
        flash("The record of the employee was updated successfully")

        return redirect(url_for('index'))


@app.route('/department/<id>', methods=['GET', 'POST'])
def delete_department(id):
    """
    This function responds to request for /department/<id>
    with one matching department from departments and removes
    the record of the department in the database.

    :param id: id of the employee

    :return: the result of redirect function
    """
    session = db.session()

    department = extract_department_by_id(id)
    session.delete(department)
    session.commit()

    flash("The record of the department was deleted successfully")

    return redirect(url_for('index'))


def extract_department_by_id(id):
    """
    Extract data of department from the data base by id
    :param id: id of Department entity
    :return: Department entity
    """
    department = Department.query.get(id)
    return department


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
    session = db.session

    last_name = extract_last_name()
    if last_name != '':
        employees = select_employee_by_last_name(last_name)
    else:
        employees = select_employees()
    session.close()
    return render_template('view_employees.html', employees=employees)

def select_employee_by_last_name(last_name):
    session = db.session
    employees = session.query(Employee.id, Employee.first_name, Employee.patronymic, Employee.last_name, \
                              Employee.age, Employee.birth_date, Employee.phone, Employee.position, \
                              Employee.experience, Employee.salary, Department.name.label('department_name')) \
                        .select_from(Employee).join(Department) \
                        .filter(Employee.last_name == last_name).order_by(Employee.birth_date).all()
    session.close()
    return employees


def extract_last_name():
    """
    Extract last_name from HTTP Form
    :return: str(last_name)
    """
    last_name = request.form.get('last_name', '')
    return last_name

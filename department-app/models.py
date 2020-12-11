from app import db
from datetime import datetime


class Department(db.Model):
    """Create a scheme for the table "Department" in the database."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    manager = db.Column(db.String(20))
    phone = db.Column(db.String(20))
    created_on = db.Column(db.DateTime, default=datetime.now())


    def __init__(self, name, manager, phone):
        """
        This function initializes the instance of class Department.

        :param self, name, manager, phone:
        department's name, manager's fullname, department's phone
        :return the instance of class Department
        """
        self.name = name
        self.manager = manager
        self.phone = phone

class Employee(db.Model):
    """Create a scheme for the table "Employee" in the database."""
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    patronymic = db.Column(db.String(20))
    last_name = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    birth_date = db.Column(db.Date)
    phone = db.Column(db.String(20))
    position = db.Column(db.String(20))
    experience = db.Column(db.Integer)
    department_id = db.Column('department_id', db.Integer, db.ForeignKey('department.id'))
    salary = db.Column(db.Numeric)
    department = db.relationship('Department', backref="employee")

    def __init__(self, first_name, patronymic, last_name, age,
                 birth_date, phone, position, experience, department_id, salary):
        """
        This function initializes the instance of class Department.

        :param self, first_name, patronymic, last_name, age, birth_date,
        phone, position, experience, department_id, salary:

        employee's first name, employee's patronymic, employee's last name,
        employee's age, employee's birth date, employee's phone,
        employee's position, employee's experience, id of employee's department,
        employee's salary

        :return the instance of class Employee
        """
        self.first_name = first_name
        self.patronymic = patronymic
        self.last_name = last_name
        self.age = age
        self.birth_date = birth_date
        self.phone = phone
        self.position = position
        self.experience = experience
        self.department_id = department_id
        self.salary = salary

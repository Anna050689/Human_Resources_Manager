import unittest
from sqlalchemy.sql import func
from datetime import date

from models import Department, Employee
from app import db, app



class TestModels(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:BeHappy01112017@localhost/human_resources_department_test'
        app.config['TESTING'] = True
        db.create_all()
        app.testing = True
        self.client = app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_department(self):
        department = Department('IT', 'Ivanov I.I', '+38(093)1548-093')
        db.session.add(department)
        db.session.commit()
        department = Department.query.get(1)
        self.assertEqual(department.id, 1)
        self.assertEqual(department.name, 'IT')
        self.assertEqual(department.manager, 'Ivanov I.I')
        self.assertEqual(department.phone, '+38(093)1548-093')

        assert department in db.session

    def test_create_employee(self):

        employee = Employee('Anna', 'Olekseevna', 'Ivanova', 22, '1998-01-01',
                            '+38(099)1548123', 'trainee', 2, 1, 10000)
        department = Department('IT', 'Ivanov I.I', '+38(093)1548-093')
        db.session.add(department)
        db.session.add(employee)
        db.session.commit()
        department = Department.query.get(1)
        self.assertEqual(department.id, 1)
        self.assertEqual(department.name, 'IT')
        self.assertEqual(department.manager, 'Ivanov I.I')
        self.assertEqual(department.phone, '+38(093)1548-093')
        self.assertEqual(employee.first_name, 'Anna')
        self.assertEqual(employee.patronymic, 'Olekseevna')
        self.assertEqual(employee.last_name, 'Ivanova')
        self.assertEqual(employee.age, 22)
        self.assertEqual(employee.birth_date, date(1998, 1, 1))
        self.assertEqual(employee.phone, '+38(099)1548123')
        self.assertEqual(employee.position, 'trainee')
        self.assertEqual(employee.experience, 2)
        self.assertEqual(employee.department_id, 1)
        self.assertEqual(employee.salary, 10000)

        assert department in db.session
        assert employee in db.session

    def test_index(self):
        response = self.client.get('/')
        department = Department('IT', 'Ivanov I.I', '+38(093)1548-093')
        employee_1 = Employee('Anna', 'Olekseevna', 'Ivanova', 22, '1998-01-01',
                            '+38(099)1548123', 'trainee', 2, 1, 10000)
        employee_2 = Employee('Inna', 'Igorevna', 'Leonova', 22, '1998-01-01',
                            '+38(099)1548123', 'trainee', 2, 1, 11000)
        db.session.add(department)
        db.session.add(employee_1)
        db.session.add(employee_2)
        db.session.commit()
        departments = db.session.query(
            Department.id, Department.name, Department.manager, Department.phone,
            func.round(func.avg(Employee.salary), 2).label('average_salary'), \
            func.count(Employee.id).label('count_of_employees')).select_from(Department). \
            join(Employee, isouter=True).group_by(Department.id)
        self.assertEqual(departments[0].id, 1)
        self.assertEqual(departments[0].name, 'IT')
        self.assertEqual(departments[0].manager, 'Ivanov I.I')
        self.assertEqual(departments[0].phone, '+38(093)1548-093')
        self.assertEqual(departments[0].average_salary, 10500.00)
        self.assertEqual(departments[0].count_of_employees, 2)



    def test_view_employees(self):
        response = self.client.get('/employees')
        self.assertTrue(response.status_code, 200)
        department = Department('IT', 'Ivanov I.I', '+38(093)1548-093')
        employee_1 = Employee('Anna', 'Olekseevna', 'Ivanova', 22, '1998-01-01',
                              '+38(099)1548123', 'trainee', 2, 1, 10000)
        db.session.add(department)
        db.session.add(employee_1)
        db.session.commit()
        employees = db.session.query(Employee.id, Employee.first_name,
                                  Employee.patronymic, Employee.last_name,
                                  Employee.age, Employee.birth_date,
                                  Employee.phone, Employee.position,
                                  Employee.experience, Employee.salary,
                                  Department.name.label('department_name')) \
            .select_from(Employee) \
            .join(Department, isouter=True).all()
        self.assertEqual(employees[0].id, 1)
        self.assertEqual(employees[0].first_name, 'Anna')
        self.assertEqual(employees[0].patronymic, 'Olekseevna')
        self.assertEqual(employees[0].last_name, 'Ivanova')
        self.assertEqual(employees[0].age, 22)
        self.assertEqual(employees[0].birth_date, date(1998, 1, 1))
        self.assertEqual(employees[0].position, 'trainee')
        self.assertEqual(employees[0].experience, 2)
        self.assertEqual(employees[0].department_name, 'IT')
        self.assertEqual(employees[0].salary, 10000)



if __name__ == '__main__':
    unittest.main()




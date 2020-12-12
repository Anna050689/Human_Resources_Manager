import unittest
from models import Department, Employee
from app import db
from datetime import date

SQLALCHEMY_DATABASE_URI = "sqlite://test.db"
TESTING = True

class TestModels(unittest.TestCase):
    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_department(self):
        department = Department('IT', 'Ivanov I.I', '+38(093)1548-093')
        db.session.add(department)
        db.session.commit()
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


if __name__ == '__main__':
    unittest.main()



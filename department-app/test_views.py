import unittest
from sqlalchemy.sql import func
from models import Department, Employee
from app import app, db
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class TestViews(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
        app.config['TESTING'] = True
        db.create_all()
        # employee_1 = Employee('Anna', 'Olekseevna', 'Ivanova', 22, '1998-01-01',
        #                     '+38(099)1548123', 'trainee', 2, 1, 10000)
        # employee_2 = Employee('Olga', 'Olekseevna', 'Popova', 22, '1998-01-01',
        #                     '+38(099)1548123', 'trainee', 2, 1, 11000)
        # department = Department('IT', 'Ivanov I.I', '+38(093)1548-093')
        # db.session.add(department)
        # db.session.add([employee_1, employee_2])
        db.session.commit()
        app.testing = True
        self.client = app.test_client()


    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_index(self):
        response = self.client.get('/')
        self.assertTrue(response.status_code, 200)
        # departments = db.session.query(
        #     Department.id, Department.name, Department.manager, Department.phone,
        #     func.round(func.avg(Employee.salary), 2).label('average_salary'), \
        #     func.count(Employee.id).label('count_of_employees')).select_from(Department). \
        #     join(Employee, isouter=True).group_by(Department.id)
        # self.assertEqual(departments[0][0], 1)
        # self.assertEqual(departments[0][1], 'IT')
        # self.assertEqual(departments[0][2], 'Ivanov I.I')
        # self.assertEqual(departments[0][3], '+38(093)1548-093')
        # self.assertEqual(departments[0][4], 10500)
    def test_view_employees(self):
        response = self.client.get('/employees')
        self.assertTrue(response.status_code, 200)










if __name__ == '__main__':
    unittest.main()
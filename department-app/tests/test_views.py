from test_base import BaseTestCase
from .models import Department, Employee
from flask import url_for

class ViewsTests(BaseTestCase):
    def test_insert_employee(self):
        Employee.create(first_name='Anna', patronymic='Aleksandrovna', last_name='Ivanova', age=34,
                        birth_date='1986-01-01', phone='973687', experience=2, department_id=7,
                        salary=10000)
        employee = {'first_name': 'Anna', 'patronymic': 'Aleksandrovna', 'last_name': 'Ivanova', 'age':34,
                'birth_date': '1986-01-01', 'phone': '973687', 'experience': 2, 'department_id': 7,
                'salary':10000}
        response = self.client.post(url_for('insert_employee'), data=employee)
        self.assert_redirects(response, url_for('view_employees'))
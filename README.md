# Manager of Human Resources Department

## Vision

**«Manager of Human Resources Department»** is a web-application which allows the manager of 
Human Resources Department to record and analyze the information about every employee of 
the company and every department as a group of employees.

The application should provide:

* Storing the information of every employee and the summary information of every department as
a group of employees;
* Display the list of departments;
* Updating the information of each department (adding, editing, and removing);
* Display the total list of employees;
* Updating the information about the employee (adding, editing, and removing);
* Select the list of employees who have the same birth date;
* Select the list of employees who were born in the fixed period between dates;

### Prerequisites

1. Windows or Unix based OS
2. Pre-installed Python 3.6 or higher
3. Pre-installed MySql
4. Pre-installed Git
5. Pre-installed pip

### How to run this application?

1. Create the directory for this application (for example, directory is called *"department-app"*:
```bash
mkdir department-app
```
2. Clone this repo: 
```bash
git clone git@gitlab.com:Anna050689/final_project.git
```
3. Set the virtual environments
```bash
python -m venv /path/to/new/virtual/environment
. venv/bin/activate
```
4. Install dependencies with pip: 
```bash
pip install -r requirements.txt
```
5. Create database in MySql and set the correct parameter **SQLALCHEMY_DATABASE_URI** in *config.py* file:<br>
```python
SQLALCHEMY_DATABASE_URI= 'mysql+mysqlconnector://root:password@localhost/name_of_database'
```
5. Make sure to populate the database by opening a Python shell from within the app and running:
```bash
from app import db
from models import Department, Employee
db.create_all()
```
6. Run the app:
```bash
export FLASK_APP='main'
export FLASK_ENV="development"
flask run
```





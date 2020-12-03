# Manager of Human Resources Department

## Vision

**«Manager of Human Resources Department»** is a web-application which allows the manager of 
Human Resources Department to record and analyze the information about every employee of 
the company and every department as a group of employees.

The application should provide:

* Storing the information of every employee and the summary information of every department as
a group of employees;
* Display the list of departments;
* Displays the actual information about departments according to the fixed date;
* Updating the information of each department;
* Display the total list of employees;
* Display the list of employees of every department;
* Updating the information about the employee (adding, editing, and removing);
* Select the list of employees who have the same birth date;
* Select the list of employees who were born in the fixed period between dates;

## 1. Departments

### 1.1 Display the list of departments

The mode is designed to view the list of departments. According to every department 
there is displayed information about the average salary, the count of employees for 
a certain period of time.

*Main scenario*:

* User selects item "Departments" in the sidebar (in the left upper corner);
* Application displays the list of departments.

![The list of departments](images/list_of_departments.png)

* *Name* - unique name of the department;
* *Manager* - full name of the manager of the department;
* *Phone* - phone number of the department;
* *Count* of employees - total count of employees of the department;
* *Average salary* - the average salary of employees of the department;
* *Actions* - here the user can get access in order to edit the 
information about the department or to view the information about the
department.

***Filtering by date:***
* In order to view the actual information about departments according to the 
certain period, the user sets the date filter and presses the refresh button( 
to the right of the date entry field);
* The application displays the actual information about departments according 
to the fixed date.

*Restrictions*:
* Start date of the period should be less than end date of the period;
* If start date and end date are blank, application displays the actual information 
according to the current date;
* If start date or end date is blank, application displays the error;

### 1.2 Edit the information about the department

*Main scenario*:

* User clicks the left icon in the column "Actions" of the department's row;
* Application displays the form to edit the data of the department;
* User enters updated data and presses "Save" button;
* If any data is entered incorrectly, an incorrect message is displayed;
* If entered data is valid, then the updated information will be added to the database;
* If updated information was successfully added, the user will see the updated information
in *The list of departments*.

*Cancel operation scenario*:

* User clicks the left icon in the column "Actions" of the department's row;
* Application displays the form to edit the data of the department;
* User enters updated data and presses "Cancel" button;
* Updated data didn't save in database;
* The user will see the previous information in *The list of departments*;
* If the user selects the menu item "Departments", "Employees" in the sidebar (to the 
left of the editing form), the data won't be saved in the database, and the corresponding form
with updated data will be opened.

![editing form](images/editing_form.png)

In the editing form the user can update the data of the department according to fixed period:
* *Name* - unique name of the department;
* *Manager* - full name of the manager of the department;
* *Phone* - phone number of the department;

### 1.3 View the information about the department.

*Main scenario*:

* User clicks the right icon in the column "Actions" of the department's row;
* Application displays the information of the department according to the fixed period 
in the Departments list;
* In order to return to the the page of *The list of departments* the user presses the button
"Departments" (in the sidebar to the left of the information page).

![view form](images/view_form.png)

In the view form the user can read the data of the department according to fixed period:
* *Name* - unique name of the department;
* *Manager* - full name of the manager of the department;
* *Phone* - phone number of the department;
* *Count* of employees - total count of employees of the department;
* *Average salary* - the average salary of employees of the department;

In order to view the list of selected department user presses the button "Employees" in the the bottom
of the view form.

## 2. Employees

### 2.1. Display the list of employees

The mode is designed to view and edit data about employees.

*Main scenario:*
* User selects item "Employees" in the sidebar (in the left upper corner);
* Application displays the list of employees.

![total list of employees](images/total_list_of_employees.png)

The total list of employees includes the following columns:
* *First Name* - employee's first name;
* *Patronymic* - employees's patronymic;
* *Last Name* - employee's last name;
* *Age* - employee's age;
* *Birth Date* - employee's birth date;
* *Phone* - employee's phone;
* *Position* - employee's position;
* *Experience* - employee's experience;
* *Department* - employee's department;
* *Salary* - employee's salary;
* *Actions* - here the user can get access in order to edit the 
information about the employee or to remove the record about the
employee.

***Filtering by birth date*:

* In order to view the list of employees who has the same birth date, the user enters
the birth date in the corresponding date field "Birth date" and presses the button "Search";

* Application displays the list of employees who have the same birth date;

![the list of employees who has the same birth date](images/list_filtering_by_birthdate.png)

* In order to view the list of employees who were born in the certain period, the user sets the 
date filter and presses the button "Search";

* Application displays the list of employees who were born in the certain period; 

![the list of employees who were born in the certain period](images/list_filtering_by_period.png)

*Restrictions:*

* If date field "Birth date" is blank, application displays the error;
* In the date entry field start date of the period should be less than end date 
of the period;
* If start date or end date is blank, application displays the error;

### 2.2 Edit the information about the employee

*Main scenario*:

* User clicks the left icon in the column "Actions" of the employee's row;
* Application displays the form to edit the data of the employee;
* User enters updated data and presses "Save" button;
* If any data is entered incorrectly, an incorrect message is displayed;
* If entered data is valid, then the updated information will be added to the database;
* If updated information was successfully added, the user will see the updated information in 
"Total list of employees".

*Cancel operation scenario*:

* User clicks the left icon in the column "Actions" of the employee's row;
* Application displays the form to edit the data of the employee;
* User enters updated data and presses "Cancel" button;
* Updated data didn't save in database;
* The user will see the previous information of this employee in *Total list of departments*;
* If the user selects the menu item "Departments", "Employees" in the sidebar(to the 
left of the editing form), the data won't be saved in the database, and the corresponding form
with updated data will be opened.

![editing form of employee](images/editing_form_of_employee.png)

In the editing form the user can update the data of the employee:
* *First Name* - employee's first name;
* *Patronymic* - employees's patronymic;
* *Last Name* - employee's last name;
* *Age* - employee's age;
* *Birth Date* - employee's birth date;
* *Phone* - employee's phone;
* *Position* - employee's position;
* *Experience* - employee's experience;
* *Department* - employee's department;
* *Salary* - employee's salary;

### 2.3 Remove the record of the employee.

*Main scenario:*

* User clicks the right icon in the column "Actions" of the employee's row;
* Application displays confirmation message "Please confirm removing the record";
* The user presses button "Yes" and confirms the removal of the employee;
* Record is deleted from database;
* If employee's record is successfully deleted, then total list of employees without 
deleted records is displaying.

*Cancel operation scenario:*
* User clicks the right icon in the column "Actions" of the employee's row;
* Application displays confirmation message "Please confirm removing the record";
* User press “Cancel” button;
* The total list of employees without changes is displaying.

![deleting the redord of the employee](images/deleting_the_record.png)

### 2.4 View the information about the employee

*Main scenario*:
* User enters the last name, patronymic and first name of the employee in the search field (in 
the right upper corner) and presses Enter;
* Application displays the record of the employee;
* If any data is entered incorrectly, an incorrect message is displayed;

![record_of_the_employee](images/record_of_the_employee.png)

### 2.5 Add the record of the employee

*Main scenario*:
* User presses the button "Employees";
* In the page "Total list of employees" user presses the button "Add employee";
* Application displays the blank form of the employee;
* User enters the data in text fields and presses the button "Save";

![add the employee](images/add_the_employee.png)

*Cancel operation scenario*:

* User presses the button "Employees";
* In the page "Total list of employees" user presses the button "Add employee";
* Application displays the blank form of the employee;
* User enters the data in text fields and presses the button "Cancel";
* Added data didn't save in database;
* The user will see the previous list of employees in *Total list of employees*;
* If the user selects the menu item "Departments", "Employees" in the sidebar (to the 
left of the editing form), the data won't be saved in the database, and the corresponding form
with added data will be opened.










































# Employee management microservice

## Overview
The Employee management microservice provides APIs for managing employee data, including creation, retrieval, updating, and deletion of employee records.

APIs offered:
- **Create Employee**: `POST /employee`
- **Get All Employees**: `GET /employees` (*Extra functionality added*)
- **Get Employee by ID**: `GET /employee/<employee_id>`
- **Delete Employee by ID**: `DELETE /employee/<employee_id>` 
- **Update Employee by ID**: `PUT /employee/<employee_id>`

## Getting Started Guide
To start using the Employee management microservice APIs, follow these steps:

1. **Clone this repository**:
```
 git clone https://github.com/ShreyaCtrl/Hirademy-Backend.git
```
   
2. **Create a virtual environment**:
   - Install `virtualenv` using pip:
   ```
    pip install virtualenv
    ```
    - Create a virtual environment:
    - On Windows:
    ```
    python -m venv env
    ```
    - On macOS and Linux:
    ```
    python3 -m venv env
    ```
    - Activate the virtual environment:
    - On Windows:
    ```
    .\env\Scripts\activate
    ```
    - On macOS and Linux:
    ```
    source env/bin/activate
    ```
3. **Install the dependencies**:
   ```
    pip install -r requirements.txt
   ```
4. **Run the server**:
   ```
   python app.py
   ```


## API Documentation
The Employee management microservice APIs are documented below:

## Note:
- **Employee ID** is a unique identifier for each employee record. It is generated automatically when a new employee record is created.
- **Employee data** includes the following fields:
  - `employee_name`: Name of the employee
  - `employee_email`: Email address of the employee
  - `employee_dept`: Department in which the employee works
  - `employee_role`: Job description of the employee in the department
  - `employee_salary`: Salary of the employee
  - `employee_dob`: Date on which the employee joined the company
  - `employee_phone`: Flag indicating whether the employee is active or not
  - `employee_city`: City in which the employee resides
  - `employee_country`: Country in which the employee resides
- **Request body** is a JSON object containing the employee data fields.
- Make sure to add your own MongoDB connection string in the `.env` file and do remember to not make it public.

## 
Feel free to customize the Employee management microservice as per your requirements. If you have any questions or need help, please reach out to us, any changes or suggestions are welcome. 

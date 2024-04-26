# Employee management microservice

## 📑Overview
The Employee management microservice provides APIs for managing employee data, including creation, retrieval, updating, and deletion of employee records.

APIs offered:
- **Create Employee**: `POST /employee`
- **Get All Employees**: `GET /employees` (*Extra functionality added*)
- **Get Employee by ID**: `GET /employee/<employee_id>`
- **Delete Employee by ID**: `DELETE /employee/<employee_id>` 
- **Update Employee by ID**: `PUT /employee/<employee_id>`

## 🔖 Getting Started Guide
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

## 👀 Note:
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

Certainly! Here's a template for creating a README file that includes detailed steps on how to run your application and how to use the Postman Collection that you exported:

## ⚙️ Technologies Used
- Python 3.x
- MongoDB
- Postman (for testing the APIs)

## 🤔 How to Use Postman Collection
To test the Employee management microservice APIs using Postman, follow these steps:
Certainly! Here are detailed instructions on how to use the Postman Collection for testing your APIs:

### Importing Postman Collection

1. **Download the Postman Collection JSON file**:
   - Go to your GitHub repository where you have uploaded the Postman Collection JSON file.
   - Click on the file to view its contents.
   - Click on the "Raw" button to view the raw JSON data.
   - Right-click and select "Save As" to download the JSON file to your local machine.

2. **Open Postman**:
   - Launch the Postman application on your computer.

3. **Import the Collection**:
   - In Postman, click on the "Import" button located in the top left corner of the window.

4. **Choose File**:
   - Select the downloaded JSON file (Postman Collection) from your local machine.

5. **Import Settings**:
   - Choose the "Import File" option if prompted.
   - Postman will automatically import the collection with all its requests and folders.

### Setting Environment Variables

1. **Open Manage Environments**:
   - In Postman, click on the gear icon in the top right corner to open the "Manage Environments" window.

2. **Create New Environment**:
   - Click on the "Add" button to create a new environment.
   - Enter a name for the environment (e.g., "Development", "Production", etc.).

3. **Add Environment Variables**:
   - Add the necessary variables required for your API requests. Common variables include:
     - `base_url`: The base URL of your API (e.g., `http://localhost:5000`).
     - `api_key`: If your API requires an API key for authentication.
     - Other custom variables specific to your API endpoints. (*Note: Not required in this case*)

4. **Save Environment**:
   - Click on "Add" to save the environment with the defined variables.

### Executing Requests

1. **Select Request**:
   - From the imported Postman Collection, navigate to the specific request you want to execute.

2. **Set Environment**:
   - In the top right corner of Postman, select the desired environment from the dropdown menu (e.g., "Development", "Production", etc.).
   - This ensures that the requests use the environment variables you defined.

3. **Execute Request**:
   - Click on the "Send" button next to the request to execute it.
   - Postman will send the request to the specified API endpoint using the configured environment variables.

4. **View Response**:
   - Once the request is executed, Postman will display the response received from the API.
   - You can view the response body, headers, status code, and other details in the Postman interface.

By following these steps, you can import the Postman Collection, set up environment variables, and execute requests to test your APIs effectively using Postman. Adjust the variables and requests as needed based on your API endpoints and testing requirements.

### Importing Postman Collection
1. Download the Postman Collection JSON file from the GitHub repository.

2. Open Postman and click on the "Import" button.

3. Choose the downloaded JSON file and import it into Postman.

### Setting Environment Variables
1. In Postman, click on the gear icon to open the "Manage Environments" window.

2. Click on "Add" to create a new environment.

3. Enter the environment name and add the necessary variables (e.g., `base_url`, `api_key`, etc.).

4. Click on "Save" to save the environment.

### Executing Requests
1. Select the desired request from the imported collection.

2. Choose the appropriate environment from the dropdown (if applicable).

3. Click on "Send" to execute the request and view the response.

---

Feel free to customize the Employee management microservice as per your requirements. If you have any questions or need help, please reach out to us, any changes or suggestions are welcome. 😁

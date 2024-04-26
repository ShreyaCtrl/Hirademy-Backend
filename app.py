from flask import Flask, request, jsonify, Response
import json
from pymongo import MongoClient
from bson.objectid import ObjectId
from dotenv import load_dotenv
import os

load_dotenv()
try:
    MONGO_URL = os.environ['MONGODB_URL']
    client = MongoClient(
        MONGO_URL,
        serverSelectionTimeoutMS=5000
    )
    # print(client.server_info())
    db = client.company
    # for db_name in client.list_database_names():
    #     print(db_name)
    # db = client.company
    client.server_info()
except Exception as e:
    print(e)

app = Flask(__name__)

@app.route('/')

@app.route('/employee', methods=['POST'])
def create_employee():
    try:
        employee = {
            'employee_name': request.form['name'],
            'employee_email': request.form['email'],
            'employee_phone': request.form['phone'],
            'employee_salary': request.form['salary'],
            'employee_dob': request.form['dob'],
            'employee_dept': request.form['dept'],
            'employee_city': request.form['city'],
            'employee_country': request.form['country']
        }
        # employee = {
        #     # 'employee_id': 1,
        #     'name': 'John Doe',
        #     'email': 'abs@gmail.com',
        #     'phone': 1234567890
        # }
        collection = db.employee
        print(collection)
        dbResponse = collection.insert_one(employee)
        # print(dbResponse.inserted_id)
        # for attr in dir(dbResponse):
        #     print(attr)
        return Response(
            response=json.dumps({
                'message': 'Employee created',
                'id': str(dbResponse.inserted_id),
                'status': 200,
                'statusText': 'OK',
                'mime-type': 'application/json'
            }),
            status=200,
            mimetype='application/json'
        )
        # return jsonify({
        #     'message': 'Employee created',
        #     'id': str(dbResponse.inserted_id),
        #     'status': 200,
        #     'statusText': 'OK',
        #     'mime-type': 'application/json'
        # })
    except Exception as e:
        print(e)
        return Response(
            response=json.dumps({
                'message': 'Employee not created',
                'error': str(e),
                'status': 500,
                'statusText': 'Internal Server Error',
                'mime-type': 'application/json'
            }),
            status=500,
            mimetype='application/json'
        )
        # return jsonify({
        #     'message': 'Employee not created',
        #     'error': str(e),
        #     'status': 500,
        #     'statusText': 'Internal Server Error',
        #     'mime-type': 'application/json'
        # })
    # return 'Employee created'

@app.route('/employees', methods=['GET'])
def get_all_employees():
    try:
        collection = db.employee
        print(collection)
        employees = list(collection.find({}, {'_id': 0}))  # Exclude _id field from response
        return jsonify(employees)
    except Exception as e:
        return Response(
            response=json.dumps({
                'message': 'Failed to fetch employees',
                'error': str(e),
                'status': 500,
                'statusText': 'Internal Server Error',
                'mime-type': 'application/json'
            }),
            status=500,
            mimetype='application/json'
        )

@app.route('/employee/<employee_id>', methods=['GET'])
def get_employee(employee_id):
    try:
        collection = db.employee
        print(employee_id)
        employee = collection.find_one({'_id': ObjectId(employee_id)})
        if employee:
            employee['_id'] = str(employee['_id'])
            return jsonify(employee)
        else:
            return Response(
                response=json.dumps({
                    'message': 'Employee not found',
                    'status': 404,
                    'statusText': 'Not Found',
                    'mime-type': 'application/json'
                }),
                status=404,
                mimetype='application/json'
            )
    except Exception as e:
        return Response(
            response=json.dumps({
                'message': 'Failed to fetch employee',
                'error': str(e),
                'status': 500,
                'statusText': 'Internal Server Error',
                'mime-type': 'application/json'
            }),
            status=500,
            mimetype='application/json'
        )

@app.route('/employee/<employee_id>', methods=['DELETE'])
def delete_employee_by_id(employee_id):
    try:
        collection = db.employee
        db_response = collection.delete_one({'_id': ObjectId(employee_id)})
        if db_response.deleted_count:
            return Response(
                response=json.dumps({
                    'message': 'Employee deleted',
                    'status': 200,
                    'statusText': 'OK',
                    'mime-type': 'application/json'
                }),
                status=200,
                mimetype='application/json'
            )
        else:
            return Response(
                response=json.dumps({
                    'message': 'Employee not found',
                    'status': 404,
                    'statusText': 'Not Found',
                    'mime-type': 'application/json'
                }),
                status=404,
                mimetype='application/json'
            )
    except Exception as e:
        return Response(
            response=json.dumps({
                'message': 'Failed to delete employee',
                'error': str(e),
                'status': 500,
                'statusText': 'Internal Server Error',
                'mime-type': 'application/json'
            }),
            status=500,
            mimetype='application/json'
        )

@app.route('/employee/<employee_id>', methods=['PUT'])
def update_employee(employee_id):
    try:
        collection = db.employee
        update_data = request.json
        db_response = collection.update_one({'_id': ObjectId(employee_id)}, {'$set': update_data})
        if db_response.modified_count:
            return Response(
                response=json.dumps({
                    'message': 'Employee updated',
                    'status': 200,
                    'statusText': 'OK',
                    'mime-type': 'application/json'
                }),
                status=200,
                mimetype='application/json'
            )
        else:
            return Response(
                response=json.dumps({
                    'message': 'Employee not found',
                    'status': 404,
                    'statusText': 'Not Found',
                    'mime-type': 'application/json'
                }),
                status=404,
                mimetype='application/json'
            )
    except Exception as e:
        return Response(
            response=json.dumps({
                'message': 'Failed to update employee',
                'error': str(e),
                'status': 500,
                'statusText': 'Internal Server Error',
                'mime-type': 'application/json'
            }),
            status=500,
            mimetype='application/json'
        )

if __name__ == '__main__':
    app.run(debug=True)
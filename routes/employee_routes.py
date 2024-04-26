from flask import Blueprint, request, jsonify, Response, current_app
from models.employee import Employee
import json

employee_bp = Blueprint('employee', __name__)

@employee_bp.route('/employee', methods=['POST'])
def create_employee():
    try:
        employee_data = request.json
        employee = Employee()
        employee_id = employee.create_employee(employee_data)
        return jsonify({
            'message': 'Employee created',
            'id': employee_id,
            'status': 200,
            'statusText': 'OK',
            'mime-type': 'application/json'
        })
    except Exception as e:
        return jsonify({
            'message': 'Employee not created',
            'error': str(e),
            'status': 500,
            'statusText': 'Internal Server Error',
            'mime-type': 'application/json'
        }), 500

@employee_bp.route('/employees', methods=['GET'])
def get_all_employees():
    try:
        employee = Employee()
        employees = employee.get_all_employees()
        return jsonify(employees)
    except Exception as e:
        return jsonify({
            'message': 'Failed to fetch employees',
            'error': str(e),
            'status': 500,
            'statusText': 'Internal Server Error',
            'mime-type': 'application/json'
        }), 500

@employee_bp.route('/employee/<employee_id>', methods=['GET'])
def get_employee_by_id(employee_id):
    try:
        employee = Employee()
        fetched_employee = employee.get_employee_by_id(employee_id)
        if fetched_employee:
            fetched_employee['_id'] = str(fetched_employee['_id'])
            return jsonify(fetched_employee)
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

@employee_bp.route('/employee/<employee_id>', methods=['DELETE'])
def delete_employee_by_id(employee_id):
    try:
        employee = Employee()
        deleted_count = employee.delete_employee(employee_id)
        if deleted_count:
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

@employee_bp.route('/employee/<employee_id>', methods=['PUT'])
def update_employee_by_id(employee_id):
    try:
        update_data = request.json
        employee = Employee()
        modified_count = employee.update_employee(employee_id, update_data)
        if modified_count:
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
# Add other routes (GET, PUT, DELETE) for employee operations similarly

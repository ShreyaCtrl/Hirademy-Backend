from pymongo import MongoClient
from bson.objectid import ObjectId
from flask import current_app

class Employee:
    def __init__(self):
        try:
            self.db = MongoClient(
                current_app.config['MONGO_URL'],
                serverSelectionTimeoutMS=5000
            ).company.employee
            self.db.server_info()
        except Exception as e:
            print(e)
        self.db = MongoClient(current_app.config['MONGO_URL']).company.employee

    def create_employee(self, employee_data):
        db_response = self.db.insert_one(employee_data)
        return str(db_response.inserted_id)

    def get_all_employees(self):
        employees = list(self.db.find({}, {'_id': 0}))
        return employees

    def get_employee_by_id(self, employee_id):
        employee = self.db.find_one({'_id': ObjectId(employee_id)})
        return employee

    def update_employee(self, employee_id, update_data):
        db_response = self.db.update_one({'_id': ObjectId(employee_id)}, {'$set': update_data})
        return db_response.modified_count

    def delete_employee(self, employee_id):
        db_response = self.db.delete_one({'_id': ObjectId(employee_id)})
        return db_response.deleted_count

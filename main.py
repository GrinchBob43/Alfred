import json
from flask import Flask, jsonify, request

app = Flask(__name__)

employees = [ { 'id': 1, 'name': 'Walt' }, { 'id': 2, 'name': 'Tomas' }, { 'id': 3, 'name': 'Remy' }]

@app.route('/employees', methods=['POST'])
def create_employee():
 global nextEmployeeId
 employee = json.loads(request.data)
 if not employee_is_valid(employee):
   return jsonify({ 'error': 'Invalid employee properties.' }), 400

 employee['id'] = nextEmployeeId
 nextEmployeeId += 1
 employees.append(employee)

 return '', 201, { 'location': f'/employees/{employee["id"]}' }

@app.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id: int):
 employee = get_employee(id)
 if employee is None:
   return jsonify({ 'error': 'Employee does not exist.' }), 404

 updated_employee = json.loads(request.data)
 if not employee_is_valid(updated_employee):
   return jsonify({ 'error': 'Invalid employee properties.' }), 400

 employee.update(updated_employee)

 return jsonify(employee)

@app.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id: int):
 global employees
 employee = get_employee(id)
 if employee is None:
   return jsonify({ 'error': 'Employee does not exist.' }), 404

 employees = [e for e in employees if e['id'] != id]
 return jsonify(employee), 200


@app.route('/employees', methods=['GET'])
def get_employees():
 return jsonify(employees)

 if __name__ == '__main__':
   app.run(port=5000)

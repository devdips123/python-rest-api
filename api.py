import flask
from flask import Flask, request, jsonify, make_response
import customer
import json

app = Flask(__name__)

@app.route('/all', methods=['GET'])
def getAll():
    return jsonify(customer.getAll())

@app.route('/create', methods=['POST'])
def create():
    payload = json.loads(request.data)
    print(f"Input object: {payload}")
    status = customer.create(payload)
    if status:
        returnCode = 201
    else:
        returnCode = 400

    response = make_response()
    response.data = json.dumps([{"msg": str(status)}])
    response.status_code = returnCode
    response.headers.add("username", "Debasish Sahoo")
    return response

@app.route('/delete/<int:id>', methods=['DELETE'])
def deleteById(id):
    status = customer.deleteById(id)
    if status:
        returnCode = 200
    else:
        returnCode = 400
    return jsonify([{"msg": str(status)}]), returnCode

@app.route('/get/<int:id>', methods=['GET'])
def getById(id):
    status = customer.getById(id)
    if status:
        returnCode = 200
    else:
        returnCode = 400
    return jsonify([{"msg": str(status)}]), returnCode

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
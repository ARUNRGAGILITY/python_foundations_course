# Python Flask

# pip install Flask

from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulating a database with a dictionary
data_store = {}
next_id = 1

@app.route('/create', methods=['POST'])
def create():
    global next_id
    data = request.json
    data_store[next_id] = data
    next_id += 1
    return jsonify(id=next_id - 1), 201

@app.route('/read/<int:id>', methods=['GET'])
def read(id):
    data = data_store.get(id)
    if data:
        return jsonify(data), 200
    else:
        return jsonify(message="Item not found"), 404

@app.route('/update/<int:id>', methods=['PUT'])
def update(id):
    if id in data_store:
        data = request.json
        data_store[id] = data
        return jsonify(id=id), 200
    else:
        return jsonify(message="Item not found"), 404

@app.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    if id in data_store:
        del data_store[id]
        return jsonify(message="Item deleted"), 200
    else:
        return jsonify(message="Item not found"), 404

if __name__ == '__main__':
    app.run(debug=True)

# CRUD Operation
# Create: POST request to add a new item
curl -X POST http://127.0.0.1:5000/create -H "Content-Type: application/json" -d '{"name": "John Doe", "age": 30}'

# Read: GET request to retrieve an item by its ID (assuming ID 1)
curl -X GET http://127.0.0.1:5000/read/1

# Update: PUT request to update an existing item by its ID (assuming ID 1)
curl -X PUT http://127.0.0.1:5000/update/1 -H "Content-Type: application/json" -d '{"name": "Jane Doe", "age": 32}'

# Delete: DELETE request to delete an item by its ID (assuming ID 1)
curl -X DELETE http://127.0.0.1:5000/delete/1

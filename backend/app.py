import os
from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Fetch the MongoDB URL from the environment variables
MONGO_URL = os.getenv('MONGO_URL')

# Connect to MongoDB
client = MongoClient(MONGO_URL)
db = client['myappdb']  # The database name

@app.route('/')
def home():
    db.test.insert_one({"message": "Hello, MongoDB!"})
    
    # Fetch the document from the test collection
    message = db.test.find_one({"message": "Hello, MongoDB!"})
    
    return jsonify(message=message['message'])

@app.route('/api/data')
def get_data():
    # Return some dummy data
    return jsonify(data={"key": "value", "number": 123})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

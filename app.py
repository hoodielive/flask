from flask import Flask, jsonify

app = Flask(__name__)

# POST - used to receive data
# GET - used to send data back only

app.run(port=5000)

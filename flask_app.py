from flask import Flask, request, jsonify
from flask_cors import CORS
import database
import bot

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/credential/create', methods=['POST'])
def create():
    data = request.get_json()
    email = data["email"]
    password = data["password"]
    connection = database.openConnection()
    status = database.create(connection, email, password)
    database.closeConnection(connection)
    if(status):
        return "success"
    else:
        return "failed" 

@app.route('/get_emails', methods=['GET'])
def getEmails():
    connection = database.openConnection()
    emails = database.getEmails(connection)
    database.closeConnection(connection)
    return jsonify({ 'emails' : emails })

@app.route('/start_bot', methods=['POST'])
def start_bot():
    data = request.get_json()
    email = data['email']
    country = data['country']
    connection = database.openConnection()
    password = database.getPassword(connection, email)
    print(password)
    database.closeConnection(connection)
    response = bot.run(email, password, country)
    print(response)
    return "success"

if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=80)
    app.run(host='0.0.0.0', port=80)
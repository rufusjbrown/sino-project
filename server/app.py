from flask import Flask, jsonify, request
from flask_cors import CORS
import os
from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "users.db"))

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)

# enable CORS
CORS(app)

class User(db.Model):
    name = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=False, primary_key=False)

    # def __repr__(self):
    #     return "<Name: {}>".format(self.name)

@app.route("/api/submit", methods=["POST"])
def home():
    if request.method == 'POST':
        name = request.get_json()['name']
        email = request.get_json()['email']
        user = User(name = name, email = email)
        db.session.add(user)
        db.session.commit()
        print(user, email)
    return "My flask app"

@app.route("/api/getUsers", methods=["GET"])
def getUsers():
    if request.method == 'GET':
        userList = []
        users = User.query.all()
        for user in users:
            userList.append({'name': user.name, 'email': user.email})
        return jsonify(userList)
  
if __name__ == "__main__":
    app.run(debug=True)
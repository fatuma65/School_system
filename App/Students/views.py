# from App.Students import student_bp
import json
from flask import request, jsonify, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
from App.Students.models import Student
import uuid
from App.auths.database import select_a_student
import jwt
import datetime
from flask import current_app as app

student_bp = Blueprint('student_bp', __name__)
# sign up endpoint for students
students = []

@student_bp.route('/student', methods=['GET'])
def get_students():
    return jsonify(students)

# creating a new student
@student_bp.route('/student', methods=['POST'])
def create_student():

    data = json.loads(request.data)
    first_name = data.get("first_name")
    last_name = data.get("last_name")
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")
    student_id = str(uuid.uuid4())

    if not first_name:
        return {"error" : "first name is required"}, 401
    if len(first_name) < 3:
        return {"error" : "first name is invalid"}, 401
    if not last_name:
        return {"error" : "first name is required"}, 401
    if len(last_name) < 3:
        return {"error" : "last name is invalid"}, 401
    if not username:
        return {"error" : "first name is required"}, 401
    if not email:
        return {"error" : "first name is required"}, 401
    

    new_student = {
        "student_id": student_id,
        "first_name": first_name,
        "last_name": last_name,
        "username": username,
        "email": email
        
    }

    students.append(new_student)
    
    student_password = generate_password_hash(password)
    user = Student(student_id, first_name, last_name, username, email, student_password)
    user.insert_student()

    response = {}
    response["data"] = new_student
    response["message"] = "student added successsfully"

    return response, 200

# login endpoint for students
@student_bp.route('/stud', methods=['POST'])
def login():
    student_info = request.data 
    login_info = json.loads(student_info)
    username = login_info["username"]
    password = login_info["password"]

    if not username or not password:
        return {"error" : "username and password is required"}
    
    student_data = select_a_student()
    if student_data[3] == username and check_password_hash(student_data[4], password):
        token = jwt.encode({"user": username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=2)}, app.config['SECRET_KEY'], algorithm='HS256')
        return jsonify({"message": "You are now logged in", "token" : token}), 200
    return jsonify({"error": "Wrong username and password"}), 400
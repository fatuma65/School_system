from flask import Blueprint, request, jsonify
import jwt
from werkzeug.security import generate_password_hash, check_password_hash
import psycopg2
import json
from App.Teachers.model import Teacher
import uuid
import jwt
import datetime
from App.auths.database import select_a_teacher
from flask import current_app as app
from App.helpers import protected_route
# from App.Teachers import teachers_bp


teachers_bp = Blueprint('teachers', __name__)

def get_connection():
    conn = psycopg2.connect(
        host = 'localhost',
        database = 'school',
        user = 'postgres',
        password = '123456789',
        port = '5432'
    )
    return conn

teacher_s = []

@teachers_bp.route('/teachers', methods=['GET'])
def get_teacher():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM teacher')
    cur.close()
    conn.close()

    return jsonify(teacher_s)

# Register teachers
@teachers_bp.route('/teachers/register', methods=['POST'])
@protected_route
def register_teacher(current_user):
    print(current_user)

    data = request.data
    data = json.loads(data)
    teacher_id = str(uuid.uuid4())
    first_name = data["first_name"]
    last_name = data["last_name"]
    username = data["username"]
    email = data["email"]
    role = "teacher"
    password = str(data["password"])

    current_user_role = current_user.get('role')

    if current_user_role != 'administrator':
        return {'error': 'You are not allowed to perform this action'}, 403

    if not first_name:
        return {"error": "first name is required"}, 401
    if not len(first_name):
        return {"error": "first name is invalid"}, 401

    if not last_name:
        return {"error": "first name is required"}, 401
    if not len(last_name):
        return {"error": "first name is required"}, 401
    if not username:
        return {"error": "first name is required"}, 401
    if not email:
        return {"error": "first name is required"}, 401
    if not password:
        return {"error": "first name is required"}, 401

    new_teacher = {
        "teacher_id": str(uuid.uuid4()),
        "first_name": first_name,
        "last_name": last_name,
        "username" : username,
        "email": email,
        "role": role,
    }

    teacher_s.append(new_teacher)

    user_password = generate_password_hash(password)
    user = Teacher( teacher_id, first_name, last_name, username, email, user_password)
    user.insert_teacher()

    response = {}
    response['data'] = new_teacher
    response["message"] = "Teacher added successfully"

    return response, 200

# login endpoint for teacher
@teachers_bp.route('/teachers/login', methods=['POST'])
def login():
    teacher_login = request.data
    login_teacher = json.loads(teacher_login)
    username = login_teacher["username"]
    password = login_teacher["password"]

    # if not username or password:
    #     return jsonify({"error":"user information is not found"}), 404
   
    teacher_data = select_a_teacher(username)

    if not teacher_data:
        return {"error": "Username or password is incorrrect"}, 400
    print(teacher_data)

    if teacher_data[3] == username  and check_password_hash(teacher_data[6], password):
        teacher_id = teacher_data[0]
        email = teacher_data[4]
        role = teacher_data[5]
        print("these conditions are matching")

        token = jwt.encode({"user": { 'username' : username, 'id' : teacher_id, 'email' : email, 'role': role }, 'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=2)}, app.config['SECRET_KEY'], algorithm='HS256')
        return jsonify({"message" : "You are now logged in", "token" : token}), 200
    return jsonify({"error" : "Wrong username or password"}), 400

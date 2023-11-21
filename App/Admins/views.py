from flask import request, jsonify,  Blueprint
import json
from werkzeug.security import generate_password_hash, check_password_hash
# from App.Admins import admin_bp
import psycopg2
from App.Admins.models import Admin
from App.auths.database import select_an_admin
import jwt
import datetime
from flask import current_app as app

# from App.auths.check import check_admin

admin_bp = Blueprint('admin_bp', __name__)
# signup endpoint for admins

def get_connection():
    conn = psycopg2.connect(
        host = 'localhost',
        database = 'school',
        user = 'postgres',
        password = '123456789',
        port = '5432'
    )
    return conn   

admin = []

@admin_bp.route('/admin', methods=['GET'])
def get_admin():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM adminss")
    cur.close()
    conn.close()

    return jsonify(admin)

# creating new administrators 
@admin_bp.route('/admin', methods=['POST'])
def create_admin():

    data = request.data
    data = json.loads(data)
    first_name = data["first_name"]
    last_name = data["last_name"]
    username = data["username"]
    email = data["email"]
    password = str(data["password"])

    # if check_admin() == True:
    #     return jsonify({"error": "Access Denied, please login in as Admin"}), 400
    if not first_name:
        return {"error" : "first name is required"}, 401
    if not last_name:
        return {"error" : "last name is required"}, 401
    if not username:
        return {"error" : "username is required"}, 401
    if not email:
        return {"error" : "email is required"}, 401

    new_admin = {
        "first_name": first_name,
        "last_name": last_name,
        "username" : username,
        "email": email
    }

    admin.append(new_admin)

    user_password = generate_password_hash(password)
    user = Admin(first_name, last_name, username, email, user_password)
    # for same in admin:
    #     if same["username"] == username:
    #         return jsonify({"error" : "username already exists"}),400
        
    user.insert_admin()

    response = {}
    response["message"] = "Administrator created sucessfully"
    response["data"] = new_admin

    return  response, 200

# login endpoint for administrators
@admin_bp.route('/log', methods=['POST'])
def login():
    user_info = request.data
    login_info = json.loads(user_info)
    username = login_info["username"]
    password = login_info["password"]

    if not username or not password:
        return {"error": "username and password is required"}, 401
    
    user_data = select_an_admin()
    if user_data[3] == username and check_password_hash(user_data[4], password):
        token = jwt.encode({'username': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=2)}, app.config['SECRET_KEY'], algorithm='HS256')
        return jsonify({"message" : "you are logged in", "token" : token}), 200
    return jsonify({"error" : "wrong username and password"}), 400
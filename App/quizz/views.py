from flask import Blueprint, request
import psycopg2
import json
from App.quizz.model import Quizz
import uuid
from flask import current_app as app
from App.helpers import protected_route

quizz_bp = Blueprint('quizz', __name__)

def get_connection():
    conn = psycopg2.connect(
        host = 'localhost',
        database = 'school',
        user = 'postgres',
        password = '123456789',
        port = '5432'
    )
    return conn

@quizz_bp.route('/quizz', methods=['POST'])
@protected_route
def create_quizz(current_user):

    current_user_role = current_user.get('role')

    if current_user_role != 'teacher':
        return {"error" : "you are not allowed to perform this action"}, 403

    data = request.data
    create_data = json.loads(data)
    question = create_data["question"]
    created_by = current_user.get("id"),
    quizz_id  =  str(uuid.uuid4())

    quizz_n = Quizz(quizz_id, created_by[0], question)
    quizz_n.insert_quizz()

    response = {}
    response["message"] = "quizz created successfully"

    return response, 201
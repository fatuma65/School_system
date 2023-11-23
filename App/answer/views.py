from flask import Blueprint, request, jsonify
import psycopg2
import json
from App.answer.model import Answer
import uuid
from flask import current_app as app
from App.helpers import protected_route

answer_bp = Blueprint('answer', __name__)

def get_connection():
    conn = psycopg2.connect(
        host = 'localhost',
        database = 'school',
        user = 'postgres',
        password = '123456789',
        port = '5432'
    )
    return conn

@answer_bp.route('/answers', methods=['POST'])
@protected_route
def create_answer(current_user):

    current_user_role = current_user.get('role')

    if current_user_role != 'student':
        return {"error" : "you are not allowed to perform this action"}, 403

    data = request.data
    create_data = json.loads(data)
    answer = create_data["answer"]
    answered_by = current_user.get("id"),
    ans_id  =  str(uuid.uuid4())

    answer_n = Answer(ans_id, answered_by[0], answer)
    answer_n.insert_answer()

    response = {}
    response["message"] = "answer created successfully"

    return response, 201
from flask import Blueprint, request
import psycopg2
import json
from App.questions.model import  Question
import uuid
from flask import current_app as app
from App.helpers import protected_route

questions_bp = Blueprint('questions', __name__)

def get_connection():
    conn = psycopg2.connect(
        host = 'localhost',
        database = 'school',
        user = 'postgres',
        password = '123456789',
        port = '5432'
    )
    return conn


@questions_bp.route('/questions', methods=['POST'])
@protected_route
def create_question(current_user):

    current_user_role = current_user.get('role')

    if current_user_role != 'teacher':
        return {"error" : "you are not allowed to perform this action"}, 403

    data = request.data
    create_data = json.loads(data)
    question = create_data["question"]
    created_by = current_user.get("id"),
    quest_id  =  str(uuid.uuid4())

    question_n = Question(quest_id, created_by[0], question)
    question_n.insert_question()

    response = {}
    response["message"] = "question created successfully"

    return response, 201
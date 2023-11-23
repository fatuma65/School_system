from flask import Blueprint, request
import psycopg2
import json
from App.grade.model import Grade
import uuid
from flask import current_app as app
from App.helpers import protected_route

grade_bp = Blueprint('grade', __name__)

def get_connection():
    conn = psycopg2.connect(
        host = 'localhost',
        database = 'school',
        user = 'postgres',
        password = '123456789',
        port = '5432'
    )
    return conn

@grade_bp.route('/grades', methods=['POST'])
@protected_route
def grade_studnets(current_user):

    current_user_role = current_user.get('role')

    if current_user_role != 'teacher':
        return {"error" : "you are not allowed to perform this action"}, 403
    
    data = request.data
    grade_data = json.loads(data)
    grade_id = str(uuid.uuid4())
    graded_by = current_user.get("id")
    question_id = grade_data["question_id"]
    score = grade_data["score"]

    grade = Grade(grade_id, graded_by, question_id, score)
    grade.insert_grade()

    response = {"message": "Grading added"}

    return response, 200
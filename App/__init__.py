from flask import Flask
from App.Admins.views import admin_bp
from App.Students.views import student_bp
from App.Teachers.views import teachers_bp
from App.questions.views import questions_bp
from App.answer.views import answer_bp
from App.quizz.views import quizz_bp
from App.grade.views import grade_bp
from App.auths import auth_bp
from instance.config import app_config

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    # register blueprints
    app.register_blueprint(admin_bp)
    app.register_blueprint(student_bp)
    app.register_blueprint(teachers_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(questions_bp)
    app.register_blueprint(answer_bp)
    app.register_blueprint(quizz_bp)
    app.register_blueprint(grade_bp)

    return app
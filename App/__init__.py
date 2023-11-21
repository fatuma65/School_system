from flask import Flask
from App.Admins.views import admin_bp
from App.Students.views import student_bp
from App.Teachers.views import teachers_bp
from App.auths import auth_bp
from instance import inst_bp
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
    app.register_blueprint(inst_bp)

    return app
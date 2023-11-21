from instance import inst_bp

class BaseConfig:
    ENVIRONMENT = 'development'
    # FLASK_APP = '__init__'
    DEBUG = False
    SECRET_KEY = 'cathyfatuma@123'
    DATABASE_URL = 'postgres://postgres:123456789@localhost:5432/school'

class Development(BaseConfig):
    DEBUG = True
    ...

app_config = {
    "Development": Development
}
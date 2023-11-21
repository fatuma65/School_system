from flask import current_app as app
import jwt
from functools import wraps
from flask import jsonify, request


def protected_route(f):
    @wraps
    def decorated(*args, **kwargs):
        token = None
        if 'token' in request.headers:
            token = request.headers['token']
        if not token:
            return jsonify({"message" : "token is missing"}), 401
        try:
            data = jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])
            current_user = data['user']
        except:
            return jsonify({"error" : "Token is invalid"}), 401
        return f(current_user, *args, **kwargs)
    return decorated
from flask import request, jsonify
from flask_jwt_extended import create_access_token, JWTManager

jwt = JWTManager()


def create_token(users, json):
    username = json.get("user", None)
    password = json.get("password", None)
    # Consulta la base de datos por el nombre de usuario y la contraseña
    user = users.find_one({'user': username, "password": password})
    if user is None:
        return jsonify({"msg": "Bad username or password"}), 401
    else:
        access_token = create_access_token(identity=user['user'])

    return jsonify({"token": access_token, "user_id": user['user']})

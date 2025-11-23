from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token
from flask import jsonify
from models.user import User
from models import db

bcrypt = Bcrypt()

def register_user(data):
    username = data.get("username")
    password = data.get("password")

    if User.query.filter_by(username=username).first():
        return jsonify({"error": "Username already exists"}), 400

    hashed = bcrypt.generate_password_hash(password).decode("utf-8")

    user = User(username=username, password=hashed)
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "Registered successfully"}), 201


def login_user(data):
    username = data.get("username")
    password = data.get("password")

    user = User.query.filter_by(username=username).first()

    if not user or not bcrypt.check_password_hash(user.password, password):
        return jsonify({"error": "Invalid credentials"}), 401

    token = create_access_token(identity=user.id)

    return jsonify({"token": token}), 200

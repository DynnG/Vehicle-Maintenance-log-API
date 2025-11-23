from flask import Blueprint, request, jsonify
from services.auth_service import register_user, login_user

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    return register_user(request.json)

@auth_bp.route("/login", methods=["POST"])
def login():
    auth_header = request.headers.get("Authorization")
    if auth_header:
        return jsonify({
            "warning": "A token is already present. Please delete it before logging in to another account."
        }), 400
    
    return login_user(request.json)

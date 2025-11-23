from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.maintenance_log import MaintenanceLog
from models import db

log_bp = Blueprint("logs", __name__)

# CREATE
@log_bp.route("/", methods=["POST"])
@jwt_required()
def create_log():
    user_id = get_jwt_identity()
    data = request.json

    if not user_id:
        return jsonify({"error": "Unauthorized access"}), 403

    log = MaintenanceLog(
        service_type=data.get("service_type"),
        description=data.get("description"),
        user_id=user_id
    )

    db.session.add(log)
    db.session.commit()

    return jsonify({"message": "Log created"}), 201


# READ (only user logs)
@log_bp.route("/", methods=["GET"])
@jwt_required()
def get_logs():
    user_id = get_jwt_identity()
    if not user_id:
        return jsonify({"error": "Unauthorized access"}), 403

    logs = MaintenanceLog.query.filter_by(user_id=user_id).all()

    return jsonify([
        {"id": l.id, "service_type": l.service_type, "description": l.description}
        for l in logs
    ]), 200


# UPDATE
@log_bp.route("/<int:log_id>", methods=["PUT"])
@jwt_required()
def update_log(log_id):
    user_id = get_jwt_identity()
    log = MaintenanceLog.query.get_or_404(log_id)

    if log.user_id != user_id:
        return jsonify({"error": "Unauthorized access"}), 403

    data = request.json
    log.service_type = data.get("service_type", log.service_type)
    log.description = data.get("description", log.description)

    db.session.commit()
    return jsonify({"message": "Log updated"}), 200


# DELETE
@log_bp.route("/<int:log_id>", methods=["DELETE"])
@jwt_required()
def delete_log(log_id):
    user_id = get_jwt_identity()
    log = MaintenanceLog.query.get_or_404(log_id)

    if log.user_id != user_id:
        return jsonify({"error": "Unauthorized access"}), 403

    db.session.delete(log)
    db.session.commit()

    return jsonify({"message": "Log deleted"}), 200

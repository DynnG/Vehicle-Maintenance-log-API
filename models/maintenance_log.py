from . import db

class MaintenanceLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_type = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(300))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

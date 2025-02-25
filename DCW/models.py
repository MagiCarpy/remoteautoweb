from DCW import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    # image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), unique=True, nullable=False)

class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    deviceName = db.Column(db.String(20), nullable=False)
    status = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'Device(name={self.deviceName}, status={self.status})'

    def toggleDevice(self, state):
        self.status = state
        db.session.commit()
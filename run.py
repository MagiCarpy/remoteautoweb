from DCW import app, db
from DCW.models import Devices

if __name__ == "__main__":
    with app.app_context():
        # db.drop_all()
        # db.create_all()
        # db.session.add(Devices(deviceName="light", status=0))
        # db.session.commit()
        # Devices.query.all()[0].status = 1
        # db.session.delete(Devices.query.all()[1])
        # db.session.commit()
        app.run(debug=True)

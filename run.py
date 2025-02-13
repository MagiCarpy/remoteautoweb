from DCW import app, db
from DCW.models import Device

if __name__ == "__main__":
    with app.app_context():
        # db.drop_all()
        # db.create_all()
        # db.session.add(Device(deviceName="light", status=0))
        # db.session.commit()
        # Device.query.all()[0].status = 1
        # db.session.delete(Device.query.all()[1])
        # db.session.commit()
        app.run(debug=True)

from DCW.models import Devices
from flask_restful import Resource, fields, marshal_with
from DCW import api

devicesFields = {
    'id':fields.Integer,
    'deviceName':fields.String,
    'status':fields.Integer,
}

class DevicesAPI(Resource):
    @marshal_with(devicesFields)
    def get(self):
        devices = Devices.query.all()
        return devices
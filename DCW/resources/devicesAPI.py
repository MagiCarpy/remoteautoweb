from DCW.models import Device
from flask_restful import Resource, fields, marshal_with
from DCW import api
import json

devicesFields = {
    'id':fields.Integer,
    'deviceName':fields.String,
    'status':fields.Integer,
}

class DevicesAPI(Resource):
    @marshal_with(devicesFields)
    def get(self):
        devices = Device.query.all()
        return devices


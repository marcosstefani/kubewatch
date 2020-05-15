from flask_restful import Resource

from service.service import ServiceService

class ServiceController(Resource):
    def get(self):
        return ServiceService.all()

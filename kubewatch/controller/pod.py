from flask_restful import Resource

from service.pod import PodService

class PodController(Resource):
    def get(self):
        return PodService.all()

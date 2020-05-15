from flask_restful import Resource

from service.kubernetes import KubernetesService

class KubernetesController(Resource):
    def get(self):
        return KubernetesService.all()

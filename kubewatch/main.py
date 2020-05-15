from flask import Flask
from flask_restful import Resource, Api

from service.kubernetes import KubernetesService
from controller.service import ServiceController

app = Flask(__name__)
api = Api(app)

class Kubernetes(Resource):
    def get(self):
        return KubernetesService.all()

api.add_resource(Kubernetes, '/')
api.add_resource(ServiceController, '/services/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

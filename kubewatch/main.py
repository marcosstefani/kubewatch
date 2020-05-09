from flask import Flask
from flask_restful import Resource, Api

from model.pod import Pod
from service.pod import PodService
from service.service import ServiceService

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return ServiceService.getAll()

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
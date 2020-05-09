from flask import Flask
from flask_restful import Resource, Api

from service.pod import PodService
from service.service import ServiceService
from service.persistent_volume import PersistentVolumeService
from service.persistent_volume_claim import PersistentVolumeClaimService

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return PersistentVolumeClaimService.getAll()

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
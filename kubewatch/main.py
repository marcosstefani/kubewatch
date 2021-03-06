from flask import Flask
from flask_restful import Api

from controller.kubernetes import KubernetesController
from controller.pod import PodController
from controller.service import ServiceController
from controller.persistent_volume import PersistentVolumeController
from controller.persistent_volume_claim import PersistentVolumeClaimController
from controller.replica_set import ReplicaSetController

from service.util import host, port

app = Flask(__name__)
api = Api(app)

api.add_resource(KubernetesController, '/')
api.add_resource(PodController, '/pod/')
api.add_resource(ServiceController, '/service/')
api.add_resource(PersistentVolumeController, '/persistent_volume/')
api.add_resource(PersistentVolumeClaimController, '/persistent_volume_claim/')
api.add_resource(ReplicaSetController, '/replica_set/')

if __name__ == '__main__':
    app.run(debug=True, host=host(), port=port())

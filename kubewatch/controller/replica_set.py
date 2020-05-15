from flask_restful import Resource

from service.replica_set import ReplicaSetService

class ReplicaSetController(Resource):
    def get(self):
        return ReplicaSetService.all()

from flask_restful import Resource

from service.persistent_volume_claim import PersistentVolumeClaimService

class PersistentVolumeClaimController(Resource):
    def get(self):
        return PersistentVolumeClaimService.all()

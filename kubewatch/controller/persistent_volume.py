from flask_restful import Resource

from service.persistent_volume import PersistentVolumeService

class PersistentVolumeController(Resource):
    def get(self):
        return PersistentVolumeService.all()

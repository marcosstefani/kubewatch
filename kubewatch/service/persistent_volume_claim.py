import subprocess

from model.persistent_volume_claim import PersistentVolumeClaim
from model.kubernetes import get_information, Element

class PersistentVolumeClaimService:
    @classmethod
    def getAll(cls):
        values = get_information(Element.PERSISTENT_VOLUME_CLAIM)
        print (values)
        pvcs = []
        for value in values:
            pvc = PersistentVolumeClaim(value[0], value[1], value[2], value[3], value[4], value[5], value[6], value[7])
            pvcs.append(pvc.json())
        return pvcs

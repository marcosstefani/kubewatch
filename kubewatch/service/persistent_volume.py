import subprocess

from model.persistent_volume import PersistentVolume
from model.kubernetes import get_information, Element

class PersistentVolumeService:
    @classmethod
    def all(cls):
        values = get_information(Element.PERSISTENT_VOLUME)
        print (values)
        pvs = []
        for value in values:
            if not (len(value) == 10 and len(pvs) == 7): # sometimes the col REASON is blank, then ignore this col
                pv = PersistentVolume(value[0], value[1], value[2], value[3], value[4], value[5], value[6], value[7], value[8])
                pvs.append(pv.json())
        return pvs

import subprocess
from enum import Enum

from model.model import Model

class Kubernetes(Model):
    def __init__(self, pods, services, persistent_volumes, persistent_volume_claims, replica_sets):
        self.pods = pods
        self.services = services
        self.persistent_volumes = persistent_volumes
        self.persistent_volume_claims = persistent_volume_claims
        self.replica_sets = replica_sets

class Element(Enum):
    POD = 'pods'
    SERVICE = 'services'
    PERSISTENT_VOLUME = 'pv'
    PERSISTENT_VOLUME_CLAIM = 'pvc'
    REPLICA_SET = 'rs'

def get_information(element):
    value = subprocess.Popen("kubectl get {el} -o wide".format(el=element.value), stdout=subprocess.PIPE, shell=True)
    (output, err) = value.communicate()
    output = output.decode("utf-8").split('\n')[:-1]

    result = []
    if (len(output) <= 1):
        print ("Not found: {el}".format(el=element))
        return result
    del output[0]

    for l in output:
        text = ' '.join(l.split())
        values = text.split(' ')
        result.append(values)
    return result

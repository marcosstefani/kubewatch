import subprocess
from enum import Enum

class Kubernetes:
    initialized = False

class Element(Enum):
    POD = 'pods'
    SERVICE = 'services'
    PERSISTENT_VOLUME = 'pv'
    PERSISTENT_VOLUME_CLAIM = 'pvc'
    REPLICA_SET = 'replicaset'

def get_information(element):
    value = subprocess.Popen("kubectl get {el} -o wide".format(el=element.value), stdout=subprocess.PIPE, shell=True)
    (output, err) = value.communicate()
    output = output.decode("utf-8").split('\n')[:-1]

    result = []
    if (len(output) <= 1):
        print ("Não encontrei pods")
        return result
    del output[0]

    for l in output:
        text = ' '.join(l.split())
        values = text.split(' ')
        result.append(values)
    return result

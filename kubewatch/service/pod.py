import subprocess

from model.pod import Pod
from model.kubernetes import get_information, Element

class PodService:
    @classmethod
    def all(cls):
        values = get_information(Element.POD)
        print (values)
        pods = []
        for value in values:
            pod = Pod(value[0], value[1], value[2], value[3], value[4], value[5], value[6], value[7], value[8])
            pods.append(pod.json())
        return pods

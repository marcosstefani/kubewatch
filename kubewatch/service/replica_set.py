import subprocess

from model.replica_set import ReplicaSet
from model.kubernetes import get_information, Element

class ReplicaSetService:
    @classmethod
    def all(cls):
        values = get_information(Element.REPLICA_SET)
        print (values)
        replicasets = []
        for value in values:
            rs = ReplicaSet(value[0], value[1], value[2], value[3], value[4], value[5], value[6], value[7])
            replicasets.append(rs.json())
        return replicasets

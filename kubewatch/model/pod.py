from model.model import Model
from service.util import nullIfNone

class Pod(Model):
    def __init__(self, name, ready, status, restarts, age, ip, node, nominated_nodes, readiness_gates):
        self.name = name
        self.ready = ready
        self.status = status
        self.restarts = restarts
        self.age = age
        self.ip = ip
        self.node = nullIfNone(node)
        self.nominated_nodes = nullIfNone(nominated_nodes)
        self.readiness_gates = nullIfNone(readiness_gates)

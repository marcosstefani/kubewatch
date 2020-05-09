from model.model import Model
from service.util import treat_null

class Pod(Model):
    def __init__(self, name, ready, status, restarts, age, ip, node, nominated_nodes, readiness_gates):
        self.name = name
        self.ready = ready
        self.status = status
        self.restarts = restarts
        self.age = age
        self.ip = ip
        self.node = treat_null(node)
        self.nominated_nodes = treat_null(nominated_nodes)
        self.readiness_gates = treat_null(readiness_gates)

from model.model import Model

class Pod(Model):
    def __init__(self, name, ready, status, restarts, age, ip, node):
        self.name = name
        self.ready = ready
        self.status = status
        self.restarts = restarts
        self.age = age
        self.ip = ip
        self.node = node
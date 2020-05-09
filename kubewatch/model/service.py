from model.model import Model
from service.util import treat_null

class Service(Model):
    def __init__(self, name, type, cluester_ip, external_ip, ports, age, selector):
        self.name = name
        self.type = type
        self.cluester_ip = cluester_ip
        self.external_ip = treat_null(external_ip)
        self.ports = treat_null(ports)
        self.age = age
        self.selector = treat_null(selector)

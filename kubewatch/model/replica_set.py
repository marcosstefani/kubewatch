from model.model import Model
from service.util import treat_null

class ReplicaSet(Model):
    def __init__(self, name, desired, current, ready, age, containers, images, selector):
        self.name = name
        self.desired = treat_null(desired)
        self.current = treat_null(current)
        self.ready = treat_null(ready)
        self.age = treat_null(age)
        self.containers = treat_null(containers)
        self.images = treat_null(images)
        self.selector = treat_null(selector)

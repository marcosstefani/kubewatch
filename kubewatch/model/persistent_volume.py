from model.model import Model
from service.util import treat_null

class PersistentVolume(Model):
    def __init__(self, name, capacity, access_modes, reclaim_policy, status, claim, storage_class, age, volume_mode):
        self.name = name
        self.capacity = treat_null(capacity)
        self.access_modes = treat_null(access_modes)
        self.reclaim_policy = treat_null(reclaim_policy)
        self.status = treat_null(status)
        self.claim = treat_null(claim)
        self.storage_class = treat_null(storage_class)
        self.age = treat_null(age)
        self.volume_mode = treat_null(volume_mode)

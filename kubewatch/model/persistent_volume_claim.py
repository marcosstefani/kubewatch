from model.model import Model
from service.util import treat_null

class PersistentVolumeClaim(Model):
    def __init__(self, name, status, volume, capacity, access_modes, storage_class, age, volume_mode):
        self.name = name
        self.status = treat_null(status)
        self.volume = treat_null(volume)
        self.capacity = treat_null(capacity)
        self.access_modes = treat_null(access_modes)
        self.storage_class = treat_null(storage_class)
        self.age = treat_null(age)
        self.volume_mode = treat_null(volume_mode)

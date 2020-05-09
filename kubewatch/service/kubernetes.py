from model.kubernetes import Kubernetes

from .pod import PodService
from .service import ServiceService
from .persistent_volume import PersistentVolumeService
from .persistent_volume_claim import PersistentVolumeClaimService
from .replica_set import ReplicaSetService

class KubernetesService:
    @classmethod
    def all(cls):
        pods = PodService.all()
        services = ServiceService.all()
        pvs = PersistentVolumeService.all()
        pvcs = PersistentVolumeClaimService.all()
        replica_sets = ReplicaSetService.all()
        
        return Kubernetes(pods, services, pvs, pvcs, replica_sets).json()

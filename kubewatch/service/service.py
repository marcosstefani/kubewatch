import subprocess

from model.service import Service
from model.kubernetes import get_information, Element

class ServiceService:
    @classmethod
    def getAll(cls):
        values = get_information(Element.SERVICE)
        print (values)
        services = []
        for value in values:
            service = Service(value[0], value[1], value[2], value[3], value[4], value[5], value[6])
            services.append(service.json())
        return services
import json
import subprocess
from enum import Enum

class Model:
    def json(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4))

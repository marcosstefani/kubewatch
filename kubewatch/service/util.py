import os
from enum import Enum

class Environment(Enum):
    HOST = '0.0.0.0'
    PORT = '5000'

def treat_null(value):
    if value in ['<none>', '', None]:
        return None
    return value

def environment(env):
    try:
        return os.environ[env.name]
    except KeyError as e:
        print('Environment {name} not found'.format(name=env.name))
    return env.value

def host():
    return environment(Environment.HOST)

def port():
    return environment(Environment.PORT)

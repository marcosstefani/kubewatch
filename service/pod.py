import subprocess

from model.pod import Pod

class PodService:
    @classmethod
    def getAll(cls):
        value = subprocess.Popen("kubectl get pods -o wide", stdout=subprocess.PIPE, shell=True)
        (output, err) = value.communicate()
        output = output.decode("utf-8").split('\n')[:-1]
        
        pods = []
        if (len(output) <= 1):
            print ("Não encontrei pods")
            return pods
        del output[0]
        
        for l in output:
            text = ' '.join(l.split())
            values = text.split(' ')
            pod = Pod(values[0], values[1], values[2], values[3], values[4], values[5], values[6])
            pods.append(pod.json())
        return pods

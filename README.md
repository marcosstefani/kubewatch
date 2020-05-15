# kubewatch
Library to listen to the kubernetes

Docker Hub: https://hub.docker.com/orgs/pykubewatch

The idea of this project is that we have a docker machine that runs a flask application that will manage a minikube that will be on the docker machine where the machine with the flask will be.

Initially we developed the get function that will bring all the pods, services, pvs, pvcs and replicasets of a pre-installed minikube machine. I will create several Issues to evolve progressively until we have a machine that:

- Start up and create a minikube inside the Docker the first time
- Initialize main of the kubewatch project and place it on the desired port
- Bring the list of all elements (pods, services, pvs, pvcs, etc ...). *This is already in the project, you may need to improve it.*
- Search for yaml generated by the flask application from the content of the minikube of the docker machine
- Add and remove new elements (pods, services, pvs, pvcs, etc ...) via the flask API
- And in the end, maybe have a visual interface using the flask templates

## APIs already created:
- Get All Information: `GET /`
- Get All Pods: `GET /pod`
- Get All Services: `GET /service`
- Get All PV: `GET /persistent_volume`
- Get All PVC: `GET /persistent_volume_claim`
- Get All Replica Sets: `GET /replica_set`

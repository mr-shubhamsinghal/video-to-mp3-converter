# list of commands

- docker build .
- docker image ls
- docker login
- docker tag ab9fa9d9a021 haasamj/auth:latest
- docker push haasamj/auth:latest
- curl -v https://registry-1.docker.io/v2/

- minikube
- kubectl apply -f ./


# To rebuild docker image

- docker build -t haasamj/auth:latest . -> at auth directory

# To redeploy pods

- kubectl get pods
- kubectl delete pod auth-7798fd788d-67fbx
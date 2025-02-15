# Useful commands


- docker build .

# To map your localhost to some hostname.

- vim /etc/hosts

# Minikube addons list

- Minikube addons list
- minikube start
- k9s
- minikube addons enable ingress
- kubectl scale deployment --replicas=0 gateway
- kubectl scale deployment --replicas=1 auth converter gateway -> for multiple services

- kubectl exec -it gateway-7566868bb6-whpkj -- /bin/sh
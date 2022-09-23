This helm chart is for installing an nginx container with custom configuration. 

I have configured nginx with a config map, which is routing traffic from 

-  hostname/google to google.html
-  hostname/fb to fb.html

Usage.

- Bring up a minikube cluster.
- clone the repo and cd to this directory
- run helm install command

```
helm upgrade --install nginx-app .
```

- find the node port which the service is exposes.

```
kubectl get svc
```
- access from browser
- try /google and /fb paths



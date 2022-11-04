
# Prerequisites
You must have the following installed to work with Kubernetes on your local machine:
- some type of hyperviser/virtual machine (e.g. Hyper-V for Windows)
- Docker
- kubectl
- minikube


# Directory Description
The directory contains the code needed to create 2 "chatting" pods (server and client) and deploy them onto a Kubernetes cluster. The client (i.e. pod 1) sends "Hello, world!" to the server (i.e. pod 2), which will send "I got it, Roger" back to the client.


# Kubernetes Deployment
The server pod - client pod communication code and the deployment code are already written for you. You will need to execute the following steps in your command line to deploy the 2 pods to a local kubernetes cluster. I used WSL2 on Windows as my command line tool.


## step 0: directory set up (technically optional for this task)
Since the current base code does not require additional requirements, it still work even without setting up a virtual environment and installing dependencies in requirements.txt (it's an empty file). However, if you prefer to set them up for good practice or if you do add additional dependencies, please set them up:

Create virutal environment
```
virtualenv -p /usr/bin/python3 venv
```
Activate venv
```
source venv/bin/activate
```
Install dependencies
```
python3 -m pip install -r requirements.txt
```


## step 1: build server and client as Docker images 
Build the server container
```
# cd into the server director
cd /server

# build image and tag it as "chat-server"
docker build -t chat-server .
```
Build the client container
```
# cd into the client director
cd /client

# build image and tag it as "chat-client"
docker build -t clat-client .
```

You can run the "$ docker images" command to double check if the containers have been successfully created.


## step 2: deploy to Kubernetes 
Create the server and client deployments using yaml files
```
# cd back into base directory
cd ..

# server deployment
kubectl apply -f server/server-deployment.yaml

# client deployment
kubectl apply -f client/client-deployment.yaml
```
Create the service that allows the server and client to communicate
```
kubectl apply -f server/server-service.yaml
```

If everything has been successful, your 2 pods should be communicating now!


## Reading messages printed by the pods

You can see the messages being printed out by the server pod by running
```
kubectl logs -f deployment.apps/server-deployment
```

You can see the messages being printed out by the client pod by running
```
kubectl logs -f deployment.apps/client-deployment
```
tip: run them on 2 different windows to observe both pods simultaneously!
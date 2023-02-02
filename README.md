# Docker-K8s-WebApp
Sample (and simple) web application that uses flask and redis.  The web application is dockerized and uploaded to DockerHub. [Link here](https://hub.docker.com/repository/docker/rv0lt/flaskrediswebapp/general)
Also, an implementation for a kubernetes cluster of the web app is provided.

There are 3 folders in the project:

**files**
Contains the original files for the web application, as well as the Dockerfile to build the image. You can build the image with:

    docker build -t flaskrediswebapp .

**docker**
In this folder is the docker compose file that created two containers, one with the flask application created (pulling it from docker hub) and other container with redis. The connection to redis is secured with a password.
To run the containers, simply run

    docker compose up -d
    
The web application should, then, be available through localhost:5000

To stop the containers:

    docker compose down

**kubernetes**
Finally, in this folder we have the files to run the same two images inside a Kubernetes cluster. 
All the resources and objects can be created by the kustomization file provided. So that, simply by running 

    kubectl apply -k ./      

We will be able to set up the web application. 

If the cloud provided being used provides load balancing we could see the address to see the web by typing:

    kubectl get services -n webapp

Finally, to clean the cluster, stop it with

    kubectl delete -k ./


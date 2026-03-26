"""
Q:: helm
A:: Helm is a package manager for Kub (like pip). But instead of installing code, 
    Helm installs entire applications on Kubernetes. Helm repository is a collection 
    of charts. Each chart is a collection of software which might be deployed on Kub.


Q:: kubectl
A:: kubectl is a tool which is installed in local machine and enables on access to controller 
    node via http API.


Q:: scheduler
A:: sceduler is a part of controller which decides how to allocate pods on each node.


Q:: kubelet
A:: kubelet is present on each (even controller) node. Is responsible for checking health of container.


Q:: manifest
A:: A manifest is just a declarative config file (usually .yaml) where you describe the desired state 
    of your system: what should run, how many copies, how it’s exposed, what resources it gets.


Q:: pod .yaml
A:: When we specify pods we specify: name, namespace, volumes
    Container level:: container port, image, requests/limits, probes(readiness/liveness), volume mounts   


Q:: ResourseQuota
A:: ResourseQuota is attached to namespace and specifies limits and requirements. 
    Defines what’s allowed in total for a namespace.    


Q:: Probes
A:: Probe uses the handle + port of docker to check their status. Probes talk to kubelet. 
    kubelet talks to controller, then controller can kill node or remove from service.


Q:: Configmaps vs Secrets
A:: 


Q:: labels vs namespaces::
A:: Namespaces influence the way pods are operating. They apply resource restrictions/permissions 
    while labels are just tags which group objects together. Used in filtering over pods while 
    resoursequotas can be attached to namespaces.


Q:: Deployment
A:: Deployments create replicaset, replicaset makes pods.


Q:: Configmap vs Secrets
A:: ConfigMap: Stores non-sensitive config
        - environment variables
        - config files
    Secrets:: Same as ConfigMap but for sensitive data (could be encrypted)
        - passwords
        - API keys


Q:: Volume vs volume mount
A:: Volume is actual memory while volumeMount is an access of docker to this mem. 
    Volume has name and volumemount has name (same) + path.
"""
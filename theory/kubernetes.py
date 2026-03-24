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
"""
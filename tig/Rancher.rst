


First setup a master aka management server:
role: controller, etcd
# 2.x # sudo docker run -d --restart=unless-stopped -p 80:80 -p 443:443 rancher/rancher

# 1.x # sudo docker run -d --restart=always -p 8080:8080 rancher/server


Next setup worker kubernetes node
probably rke - rancher kubernetes engine
role: worker

rke config
which generate a cluster.yml

hmm... kubernetes will fail to activate if swap is on :(
soln: --fail-swap-on=false

ref: https://hackernoon.com/deploying-kubernetes-on-premise-with-rke-and-deploying-openfaas-on-it-part-1-69a35ddfa507




FYI
---

* rancher/rancher is rancher 2.x - support k8s, better user mapping, but problem not solved yet.
* rancher/server  is rancher 1.x (does not use k8s scheduler, only support their own (internal) scheduler)
* rancher will run prometheus for server health monitoring




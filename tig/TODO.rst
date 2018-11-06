
grafana plugin install don't work on bofh.
likely cuz docker container can't go out to internet
cuz of the way how i disabled docker from doing iptables, and used ufw to selectively block port access.

so, may still need to add some ufw or routing things for bofh at least, maybe more general in recipe.


~~~~


tin6150/satools 
fat docker for troubleshoooting.  not likely checked into dockerhub yet.
may want to find a different place to host the file, and have not figured out all the tags vs dockerhub upload yet.


~~~~

Learn:
how to make docker container listen only for specific list of IP.
not sure if want the container network to have iptables itself to selectively allow for inbound connection for specific ip.
only i would use it anyway, would likely not need in production or host behind network firewall.





redis container for test by Hiroshi/ALS
***************************************

docker-compose up


But should limit IP that can submit request.

seems like best to use 
DOCKER-USER iptable chain

docker-compose up/down will only change whether the port is LISTEN or not, 
it will leave the DOCKER-USER chain intact

https://docs.docker.com/network/iptables/

.. code:: bash 

	Use 1 of, cannot be repeated:
	sudo iptables -I DOCKER-USER -m iprange -i enp1s0 ! --src-range 192.168.28.1-192.168.28.140 -j DROP
	sudo iptables -I DOCKER-USER -m iprange -i eno1   ! --src-range 131.243.75.1-131.243.86.255 -j DROP
	sudo iptables -I DOCKER-USER -i eno1  ! -s 131.243.86/24   -j DROP

The above updated iptables.  ufw largely dont see the changes, but iptables -nvL reports them.
Predicatably, `ufw reload` does not change any of the manual iptables cmd.

`ufw reset` will delete all ufw rules, but the iptables cmd still remain.

These are all consistent with ufw only mangling things it put up.
But leave question on how to reset all rules.  run `iptables ??` 


changing iptable rules
----------------------

.. code:: bash 

	iptables -nvL --line-n           # show rule number, which is dynamic
	sudo iptables -D DOCKER-USER  1  # delete specific rule, be careful not to delete the RETURN rule added by docker 



How to allow multiple ranges?
-----------------------------

	TBD...





redis container for test by Hiroshi/ALS
***************************************

startup
-------

export PASSWORD_FROM_ENV=myPassword
docker-compose up

Also need one time setup of iptables PREROUTE rule
to limit which IP range can hit it, see
DOCKER-USER iptables section below


testing redis
-------------

telnet localhost 6379
PING

echo PING | nc localhost 6379

(printf "PING\r\n";) | nc localhost 6379


curl -w '\n' http://127.0.0.1:6379/ping
https://stackoverflow.com/questions/33243121/abuse-curl-to-communicate-with-redis




redis-cli
---------

.. code:: bash 

	redis-cli -h redis15.localnet.org  -p 6379 ping 


redis-cli is the entry point to the docker container, 
annoyingly `-h host` has to after it, then followed by args to redis-cli :/

.. code:: bash 

	docker run --network host  --rm redis  redis-cli  -h localhost  ping
	docker run --network host  --rm redis  redis-cli  -h localhost  set name foo
	docker run --network host  --rm redis  redis-cli  -h localhost  get name
	docker run --network host  --rm redis  redis-cli  -h localhost  

	docker run -it --network host  --rm redis redis-cli -h 172.17.0.1 -p 6379 ping

	docker run -it --network host  --rm redis redis-cli -h localhost redis-cli
	ping
	incr counter
	get counter
	flushall



If need to provide password, use -a STRING 

.. code:: bash 

	docker run --network host  --rm redis  redis-cli  -h localhost  -a myPassword ping


ref: https://redis.io/topics/rediscli



DOCKER-USER iptables rule
=========================

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




https://blog.trendmicro.com/trendlabs-security-intelligence/why-running-a-privileged-container-in-docker-is-a-bad-idea/

non-root docker:
run with --userns-remap to lower the user inside the container
(same as User: clause in a docker-compose/dockerfile ?)
But this config is not less featureful, which rootless docker is.
(rootless docker is the one that miss out on cgroup (needed by docker top) , network creation, AppArmor, Checkpoint, etc).

but docker daemon still running as root
thus namesapce hacks can easily regain root priviledges.

docker-in-docker was for dev but adopted by ci, and that req lots of priviledges.


rootless docker is different.
there is no root daemon.
systemctl --user start docker
run as user.
so, there is no dependency of userns being secure?  cuz the most it can break out of is the user running the docker, no?

uid/gid remap... i have not studied how messy that is.  but we are likely only handling a handful of user for GRETA.


~~~~

https://unit42.paloaltonetworks.com/non-root-containers-kubernetes-cve-2019-11245-care/

At the same time, all the current implementations of rootless containers rely on user namespaces at their core. Not to be confused with what is referred to as non-root containers in this article, rootless containers are containers that can be run and managed by unprivileged users on the host. While Docker and other runtimes require a daemon running as root, rootless containers can be run by any user without additional capabilities.
[...]
Although user namespaces are not the focus of this article, it is worth mentioning that they do provide additional security benefits to traditional non-root containers. Without user namespaces, even if a container process runs without root, any privilege escalation vulnerability in the container could still compromise the host. For example, a malicious container process could exploit a vulnerable setuid binary to become root. This would not be possible if the root user inside the container is mapped to a non-root user on the host.
[...]
The use of containers follows the principle of least privilege by its nature, as containers usually have limited responsibilities and capabilities. By restricting containers from using root when it is not strictly needed, we can further increase their security and prevent attackers from exploiting flaws that may be found in container engines.

**>>** above was precisely my point.  design with least security needed.  Security by layers, not just perimiter security.
GRETA will need to be supported for 10-20 years.  A bit more work now may go a long way in mitigating future risks.  
Do we want people to look back and say we were naive?

Still need to dig out the user namespace issue.  Rootless docker is no panacea, but how is it worse?
maybe see https://news.ycombinator.com/item?id=20039465

Well, thousands of companies, such as ISPs offering VPS are using containers for exactly that reason. Containers use cgroups under the hood, a Linux kernel feature that limits, accounts for, and isolates the resource usage (CPU, memory, disk I/O, network, etc.) of a collection of processes. As long as there aren't any bugs in the kernel related to cgroups, security is provided.

The problem with docker isn't at the kernel level, it's the userspace tooling. It's pretty insecure by default. For example it creates bridged networks as the default network interface and actively encourages (by design) developers to run code as root (since creating non-root users then becomes a manual RUN command). Then you have vulnerabilities in the user space tools to contend with in addition to the same concerns about sharing a kernel that crop up when discussing security and containerisation. That said, there are some stuff it does right from a security standpoint but generally speaking docker is a tool you need to harden rather than something that comes hardened.

An excellent talk from Red Hat's Dan Walsh: https://www.youtube.com/watch?v=a9lE9Urr6AQ




hmm...
double check on this:
https://www.alibabacloud.com/blog/container-security-a-look-at-rootless-containers_595153

**>>** rootless docker doesn't use userNS ?
**>>** and rootless docker can't create veth.  maybe not using DOCKER_USER PREFILTER in iptables, 
       but it seems that standard ufw can now block container listen by ip without doing a special iptable raw command with DOCKER_USER, which could be a plus.
Although unprivileged users can create network namespaces in user namespaces and perform operations like iptables rule management and tcpdump, they cannot create veth pairs across the host and containers, which means containers do not have Internet connection

rootless docker can listen to traffic.
it is like normal unix program.
docker run -it -p 8008:8008 tin6150/r4eta 
then run iperf3 server on port 8008
other machine can connect.
**^ tin zink ^**>  iperf3 -c localhost -t 30 -i 1 -p 8008 
[  4]   0.00-30.00  sec  56.5 GBytes  16.2 Gbits/sec    4             sender
[  4]   0.00-30.00  sec  56.5 GBytes  16.2 Gbits/sec                  receiver

**^ tin m42 ~ ^**>  iperf3 -c 192.168.28.131 -p 8008 -t 30 -i 1
  [ ID] Interval           Transfer     Bandwidth       Retr
  [  4]   0.00-30.00  sec  47.1 MBytes  13.2 Mbits/sec   51             sender
  [  4]   0.00-30.00  sec  46.4 MBytes  13.0 Mbits/sec                  receiver
# have to disable ufw on zink (192.168.28.131).
# test over wifi, and a Ethernet over AC adapter thing, so perf isn't great.


another test
redis with docker-compose.yml, listen to port 6379
redis-cli with ping work from host... functionaly does not seems diff between instance running by 
traditional docker vs rootless docker.
performance... not sure.  there seems to be some delay?

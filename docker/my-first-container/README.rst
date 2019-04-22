
Following spin nersc docker tutorial #1
https://docs.nersc.gov/services/spin/getting_started/lesson-1/

a docker container for flask application (maybe put psg as static pages in there)


~~~~
bofh is having problem building container...
so moving (really meant cp) to tin-gh/inet-dev-class/docker  



**^ tin bofh ~/docker/my-first-container/app ^**>  docker image build --tag my-first-container-app .
Sending build context to Docker daemon  3.072kB
Step 1/6 : FROM debian:latest
 ---> 2d337f242f07
Step 2/6 : RUN apt-get update --quiet -y && apt-get install --quiet -y python-flask
 ---> Running in f2905d0bff04
Err:1 http://deb.debian.org/debian stretch InRelease
  Temporary failure resolving 'deb.debian.org'
Err:2 http://security.debian.org/debian-security stretch/updates InRelease
  Temporary failure resolving 'security.debian.org'
Err:3 http://deb.debian.org/debian stretch-updates InRelease
  Temporary failure resolving 'deb.debian.org'
Reading package lists...
W: Failed to fetch http://deb.debian.org/debian/dists/stretch/InRelease  Temporary failure resolving 'deb.debian.org'
W: Failed to fetch http://security.debian.org/debian-security/dists/stretch/updates/InRelease  Temporary failure resolving 'security.debian.org'
W: Failed to fetch http://deb.debian.org/debian/dists/stretch-updates/InRelease  Temporary failure resolving 'deb.debian.org'
W: Some index files failed to download. They have been ignored, or old ones used instead.
Reading package lists...
Building dependency tree...
Reading state information...
E: Unable to locate package python-flask
The command '/bin/sh -c apt-get update --quiet -y && apt-get install --quiet -y python-flask' returned a non-zero code: 100
**^ tin bofh ~/docker/my-first-container/app ^**>  cd ..


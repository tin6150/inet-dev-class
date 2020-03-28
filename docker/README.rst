
Learning docker
===============

vi Dockerfile

docker build -t tin6150/ubuntu-test .

better examples in cmaq repo


Docker X11 GUI apps
===================


eg from https://blog.jessfraz.com/post/docker-containers-on-the-desktop/


chrome
------

docker run -it \
    --net host \ # may as well YOLO
    --cpuset-cpus 0 \ # control the cpu
    --memory 512mb \ # max memory it can use
    -v /tmp/.X11-unix:/tmp/.X11-unix \ # mount the X11 socket
    -e DISPLAY=unix$DISPLAY \ # pass the display
    -v $HOME/Downloads:/root/Downloads \ # optional, but nice
    -v $HOME/.config/google-chrome/:/data \ # if you want to save state
    --device /dev/snd \ # so we have sound
    --name chrome \
    jess/chrome


docker run -it --cpuset-cpus 0  --memory 4096mb  -v /tmp/.X11-unix:/tmp/.X11-unix  -e DISPLAY=:0 \
    -v $HOME/Downloads:/root/Downloads  -v $HOME/.config/google-chrome/:/data  
    --device /dev/snd  --name chrome  jess/chrome

tin@fed888xxx:~$ docker run -it  -v /tmp/.X11-unix:/tmp/.X11-unix  -e DISPLAY=:0     --rm  jess/chrome
Failed to move to new namespace: PID namespaces supported, Network namespace supported, but failed: errno = Operation not permitted



cathode 1995 era CRT terminal emulator
--------------------------------------

docker run -it  -v /tmp/.X11-unix:/tmp/.X11-unix  -e DISPLAY=$DISPLAY  jess/cathode
docker run -it  -v /tmp/.X11-unix:/tmp/.X11-unix  -e DISPLAY=:0        jess/cathode
# both works, just don't use unix$DISPLAY, maybe Jess meant unix was hostname...

docker build  https://raw.githubusercontent.com/jessfraz/dockerfiles/master/cathode/Dockerfile


xterm in cmaq container
-----------------------

docker run -it  -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY  --name xterm   --rm  tin6150/os4cmaq /usr/bin/xterm
# works.  used Docker version 18.09.7, build 2d0083d (ubuntu 18.04)
# note that must use source and destination in -v map.
# cannot just use -v /tmp/.X11-unix, nor -v /tmp

# probably don't need to run xhost +

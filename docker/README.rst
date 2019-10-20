
Learning docker
===============

well, kinda testing, why isn't bofh building container??!!

vi Dockerfile

docker build -t tin6150/ubuntu-test .



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


cathode 1995 era CRT terminal emulator
--------------------------------------

docker run -it  -v /tmp/.X11-unix:/tmp/.X11-unix  -e DISPLAY=unix$DISPLAY  jess/cathode

# didn't work:
No protocol specified
qt.qpa.screen: QXcbConnection: Could not connect to display unix:0.0
Could not connect to any X display.

docker build  https://raw.githubusercontent.com/jessfraz/dockerfiles/master/cathode/Dockerfile


xterm in cmaq container
-----------------------

docker run -it  -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix$DISPLAY  --name xterm   --rm  tin6150/os4cmaq

docker exec -it xterm2 -e DISPLAY=unix$DISPLAY  /usr/bin/xterm


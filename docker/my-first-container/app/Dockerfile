FROM debian:latest
#ENV http_proxy 'proxy.com'
##RUN echo "nameserver 8.8.8.8" > /etc/resolv.conf 
RUN apt-get update --quiet -y && apt-get install --quiet -y python-flask
WORKDIR /app
COPY app.py /app
ENTRYPOINT ["python"]
CMD ["app.py"]

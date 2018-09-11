

from the rhel install page

http://docs.grafana.org/installation/rpm/



The systemd service file and init.d script both use the file located at 
*> /etc/sysconfig/grafana-server <*
for environment variables used when starting the back-end. Here you can override log directory, data directory and other variables.
Logging

By default Grafana will log to 
*> /var/log/grafana <*
Database

The default configuration specifies a sqlite3 database located at 
*> /var/lib/grafana/grafana.db <* . Please backup this database before upgrades. You can also use MySQL or Postgres as the Grafana database, as detailed on the configuration page.
Configuration

The configuration file is located at 
*> /etc/grafana/grafana.ini <* . Go the Configuration page for details on all those options.




http://docs.grafana.org/installation/configuration/
---------------------------------------------------



Config file locations

    Default configuration from $WORKING_DIR/conf/defaults.ini
    Custom configuration from $WORKING_DIR/conf/custom.ini
    The custom configuration file path can be overridden using the --config parameter

    Note. If you have installed Grafana using the deb or rpm packages, then your configuration file is located at /etc/grafana/grafana.ini. This path is specified in the Grafana init.d script using --config file parameter.

Using environment variables

All options in the configuration file (listed below) can be overridden using environment variables using the syntax:

GF_<SectionName>_<KeyName>


export GF_DEFAULT_INSTANCE_NAME=my-instance
export GF_SECURITY_ADMIN_USER=true
export GF_AUTH_GOOGLE_CLIENT_SECRET=newS3cretKey





Install using docker
--------------------

http://docs.grafana.org/installation/docker/


docker run \
  -d \
  -p 3000:3000 \
  --name=grafana \
  -e "GF_SERVER_ROOT_URL=http://grafana.server.name" \
  -e "GF_SECURITY_ADMIN_PASSWORD=secret" \
  grafana/grafana



Setting Default value
GF_PATHS_CONFIG /etc/grafana/grafana.ini
GF_PATHS_DATA   /var/lib/grafana                # most important for persistent storage
GF_PATHS_HOME   /usr/share/grafana
GF_PATHS_LOGS   /var/log/grafana                # map this so that can see what grafana may complain about (or docker logs?).



Grafana container using bind mounts

You may want to run Grafana in Docker but use folders on your host for the database or configuration. When doing so it becomes important to start the container with a user that is able to access and write to the folder you map into the container.

mkdir data # creates a folder for your data
ID=$(id -u) # saves your user id in the ID variable

# starts grafana with your user id and using the data folder
docker run -d --user $ID --volume "$PWD/data:/var/lib/grafana" -p 3000:3000 grafana/grafana:5.1.0



Reading secrets from files (support for Docker Secrets)

    Only available in Grafana v5.2+.

It’s possible to supply Grafana with configuration through files. This works well with Docker Secrets as the secrets by default gets mapped into /run/secrets/<name of secret> of the container.

You can do this with any of the configuration options in conf/grafana.ini by setting GF_<SectionName>_<KeyName>__FILE to the path of the file holding the secret.

Let’s say you want to set the admin password this way.

    Admin password secret: /run/secrets/admin_password
    Environment variable: GF_SECURITY_ADMIN_PASSWORD__FILE=/run/secrets/admin_password



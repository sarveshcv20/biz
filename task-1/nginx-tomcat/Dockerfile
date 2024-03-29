# Using customised base-image which contains required dependencies (dockerfile available under base-image folder)
# Pulls customised base-image from dockerhub
FROM sarveshanand94/sarvesh-repo:sarvesh-final-base

# Creating tomcat dir
RUN mkdir /opt/tomcat/

# Making current work dir
WORKDIR /opt/tomcat

#Downloading tomcat tar, extracting contents and installing Nginx from nginx repo
RUN curl -O https://archive.apache.org/dist/tomcat/tomcat-8/v8.5.40/bin/apache-tomcat-8.5.40.tar.gz \
    && tar xvfz apache*.tar.gz \
    && mv apache-tomcat-8.5.40/* /opt/tomcat/. \
    && yum -y localinstall http://nginx.org/packages/centos/7/x86_64/RPMS/nginx-1.16.0-1.el7.ngx.x86_64.rpm

#Copying server.xml (tomcat port is changed to 8500)
ADD server.xml /opt/tomcat/conf/ 

# Copying nginx config (added reverse proxy config with access & err logging enabled )
ADD nginx.conf /etc/nginx/ 

# Copying supervisor config (contains startup commands for processes)
ADD supervisor.conf /etc/supervisor.conf

# Exposing nginx port 80 to connect from host
EXPOSE 80

# Command to run at boot up of container (supervisor controls multi-process startup)
CMD ["supervisord", "-c", "/etc/supervisor.conf"]

# Docker build command 
# docker build -t image_name .
# Docker run command boots the container and binds container port with host port
# docker run -it -d --name container_name -p 80:80 container_image_id
# Connect at 127.0.0.1:80

#Using customised base-image which contains required dependencies
FROM sarveshanand94/sarvesh-repo:sarvesh-final-base

# Creating tomcat dir
RUN mkdir /opt/tomcat/

# Making current dir
WORKDIR /opt/tomcat

#Downloading tomcat tar, extracting contents and installing Nginx
RUN curl -O https://archive.apache.org/dist/tomcat/tomcat-8/v8.5.40/bin/apache-tomcat-8.5.40.tar.gz \
    && tar xvfz apache*.tar.gz \
    && mv apache-tomcat-8.5.40/* /opt/tomcat/. \
    && yum -y localinstall http://nginx.org/packages/centos/7/x86_64/RPMS/nginx-1.16.0-1.el7.ngx.x86_64.rpm

#Copying server.xml,nginx.conf and supervisor config
ADD server.xml /opt/tomcat/conf/ 
ADD nginx.conf /etc/nginx/ 
ADD supervisor.conf /etc/supervisor.conf

# Exposing nginx port 80 to connect from host
EXPOSE 80

# Command to run at boot up of container
CMD ["supervisord", "-c", "/etc/supervisor.conf"]


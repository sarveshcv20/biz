# Using official centos7 image as base
FROM centos:7

# Installing base packages  
RUN yum install -y wget tar gcc \
    && yum -y install epel-release \
    && yum install -y https://centos7.iuscommunity.org/ius-release.rpm \
    && yum install -y python36u python36u-libs python36u-devel python36u-pip \
    && yum install -y openldap-devel \
    && yum install -y supervisor \
    && yum -y install java \
    && java -version

FROM artifactory.core.rcsops.com/devops-centos6-brooklyn

ENV http_proxy=10.131.236.9:3128 https_proxy=10.131.236.9:3128 LANG=en_US.UTF-8

MAINTAINER vijay.maddukuri@virtustream.com

RUN yum_install curl epel-release java-1.8.0-openjdk-devel libxslt tar rpm-build \
git perl-Git \
&& yum clean all

RUN echo "export JAVA_HOME=/usr/lib/jvm/java-1.8.0" >> /home/jenkins/.bashrc

RUN yum install unzip && curl -O https://artifactory.core.rcsops.com/artifactory/ext-release-local/org/apache/maven/apache-maven/3.3.9/apache-maven-3.3.9-bin.zip && mkdir -p /home/jenkins/tools/hudson.tasks.Maven_MavenInstallation/maven-3.3.9 && unzip apache-maven-3.3.9-bin.zip -d /home/jenkins/tools/hudson.tasks.Maven_MavenInstallation/maven-3.3.9

RUN echo "export M2_HOME=/home/jenkins/tools/hudson.tasks.Maven_MavenInstallation/maven-3.3.9/apache-maven-3.3.9" >> /home/jenkins/.bashrc
RUN echo "export M2=$M2_HOME/bin" >> /home/jenkins/.bashrc

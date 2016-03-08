# keychain

[![Build Status](https://travis-ci.org/robertdebock/keychain.svg?branch=master)](https://travis-ci.org/robertdebock/keychain)

This repository contains a SPEC file for [KeyChain](http://www.funtoo.org/Keychain) for [CentOS 7](https://www.centos.org/), [Red Hat 7](http://www.redhat.com/) or [Fedora](https://getfedora.org/).

[Travis-CI](https://travis-ci.org/robertdebock/keychain.el7) is being used to build, test and publish the RPM.

To use these packages, run:

    rpm -Uvh https://s3-eu-west-1.amazonaws.com/rpm-repos-el7/rpm-repos-el7-1-1.el7.noarch.rpm

followed by:

    yum install apache-tomcat

Or [have a look in the repository](http://apache-tomcat7.el7.s3-eu-west-1.amazonaws.com/index.html) and download the RPM's manually.
    
Optional extra packages are:
- apache-tomcat-manager
- apache-tomcat-ROOT
- apache-tomcat-docs
- apache-tomcat-examples
- apache-tomcat-host-manager

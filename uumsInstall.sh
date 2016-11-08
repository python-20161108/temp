#!/bin/bash

echo "Begin Installing UUMS"

#judgement mysql home directory exist.
if [ ! -d "/var/lib/mysql" ];then
   echo "Begin Installing mysql"
   zypper install mysql
   service mysqld start
   chkconfig mysqld on;else
echo "The mysql have installed"
fi

#judgement the case sensitive.
if grep -Fxq "lower_case_table_names" /etc/my.cnf;then
   sed -i '/[mysqld]/a\n lower_case_table_names=1' /etc/my.cnf
   service mysqld restart
   echo "Creating Database"
   mysql < $(date +%F)_db_mysql_backup.sql;else
echo "The UUMS database have created"
fi

if [ ! -d "/var/lib/tomcat6" ];then
   echo "Begin Installing Tomcat6"
   zypper install tomcat
   service tomcat6 start
   chkconfig tomcat6 on;else
echo "The tomcat6 have installed"
fi

if [ ! -d "/var/lib/tomcat6/webapps/ROOT" ];then
   cp /root/uums/ROOT.zip /var/lib/tomcat6/webapps
   unzip /var/lib/tomcat6/webapps/ROOT.zip;else
   rm -rf /var/lib/tomcat6/webapps/ROOT
   cp /root/uums/ROOT.zip /var/lib/tomcat6/webapps
   unzip /var/lib/tomcat6/webapps/ROOT.zip
echo "You can access the UUMS ,http://IP:8080/admin"
fi

# This puppet script Changes the OS configuration file so that it is possible to login with the holberton user and open a file without any error message.

#exec {'Change OS security configuration':
#  command => 'sed -i "s/holberton/foo/" /etc/security/limits.conf',
#  path    => '/usr/bin/env/:/bin/:/usr/bin/:/usr/sbin/'
#}

exec {'Change OS security configuration':
command => "bash -c \"sed -iE 's/^holberton hard nofile \
5/holberton hard nofile 88888/' /etc/security/limits.conf; \
sed -iE 's/^holberton soft nofile \
4/holberton soft nofile 88888/' /etc/security/limits.conf\"",
  path    => '/usr/bin:/usr/sbin:/bin'
}

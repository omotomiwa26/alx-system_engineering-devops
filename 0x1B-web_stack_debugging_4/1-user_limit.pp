# This puppet script Changes the OS configuration to allow login with the holberton user and open a file without any error message.

exec {'Change OS security configuration':
  command => 'sed -i "s/holberton/foo/" /etc/security/limits.conf',
  path    => '/usr/bin/env/:/bin/:/usr/bin/:/usr/sbin/'
}


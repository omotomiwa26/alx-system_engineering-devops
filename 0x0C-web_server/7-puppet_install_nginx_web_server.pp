# This Puppet manifest configures Nginx with a custom 404 page and a "301 Moved permanently" redirection rule.

# Install Nginx package
package { 'nginx':
  ensure => 'installed',
}

# Creating custom index page
file { '/var/www/html/index.html':
  ensure  => 'file',
  content => 'Hello World!\n',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0644',
}

# Define Nginx server block for the default configuration
file { '/etc/nginx/sites-enabled/default':
  ensure  => 'file',
  content => "server {
    listen 80;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }

    error_page 404 /404.html;
    location = /404.html {
        root /var/www/html/;
        internal;
    }
}",
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Creating custom 404 page
file { '/var/www/html/404.html':
  ensure  => 'file',
  content => "Ceci n'est pas une page\n",
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0644',
  notify  => Service['nginx'],
}

# Ensure the Nginx service is running and enabled
service { 'nginx':
  ensure => 'running',
  enable => true,
}

# This Puppet manisfest automate the task of creating a custom HTTP header response

exec { 'command':
  command  => 'apt-get update -y;
  apt-get install nginx -y;
  sudo sed -i "/listen 80 default_server;/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default;
  sudo service nginx restart',
  provider => shell,
}

# This is a puppet manifest using client SSH configuration

include stdlib

file_line { 'No Password Authentication':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
}

file_line { 'Private key identity Authentication':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/school'
}

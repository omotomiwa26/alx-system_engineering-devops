# This puppet file creates a manifest that kills a process named killme now

exec { 'pkill killmenow':
  path => '/usr/bin:/usr/sbin:/bin'
}


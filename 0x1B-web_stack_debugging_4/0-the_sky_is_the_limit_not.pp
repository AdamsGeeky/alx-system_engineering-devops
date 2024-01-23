# increase nginx traffic

exec { 'increase-traffic':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

# Restart Nginx
-> exec { 'restart-web-server':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
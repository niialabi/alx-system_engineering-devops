# change unlimit value to allow more openfiles
exec { 'inc_unlimit':
  command  => 'sed -i "s|ULIMIT=\"-n 15\"|ULIMIT=\"-n 10000\"|" /etc/default/nginx',
  provider => 'shell',
}
-> exec { 'service_restart_nginx':
  command  => 'service nginx restart',
  provider => 'shell',
}

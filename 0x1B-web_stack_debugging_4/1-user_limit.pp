# increase holberton user max open files
exec { 'up_hard_limit':
  command  => 'sed -i "s/holberton hard nofile 5/holberton hard nofile 5000/" /etc/security/limits.conf',
  provider => 'shell'
}
exec { 'up_soft_limit':
  command  => 'sed -i "s/holberton soft nofile 4/holberton soft nofile 4000/" /etc/security/limits.conf',
  provider => 'shell'
}

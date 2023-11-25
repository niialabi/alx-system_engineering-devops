# install package from pip3
package { 'werkzueg':
  ensure   => '2.1.1',
  provider => 'pip3',
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

package {'python3-pip':
  ensure => present,
}

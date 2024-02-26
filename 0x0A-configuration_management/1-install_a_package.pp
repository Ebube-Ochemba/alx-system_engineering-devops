# Using Puppet, install flask and pip3

# Python
package { 'python3':
  ensure => 'installed'
}

# PIP3
package { 'python3-pip':
  ensure => 'installed',
}

# Flask
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],
}

# Werkzeug
package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
  require  => Package['python3-pip'],
}

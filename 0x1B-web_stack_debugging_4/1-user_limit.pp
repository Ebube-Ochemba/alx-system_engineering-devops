# Puppet manifest to set open file limits for the system
# This manifest will correct the hard and soft limits for the maximum number of open files.

# Ensure the /etc/security/limits.conf file exists
file { '/etc/security/limits.conf':
  ensure => file,
  mode   => '0644',
}

# Fix the limits for the 'nofile' descriptor in /etc/security/limits.conf
exec { 'Correct file descriptor limits':
  command => 'sudo sed -i -e "s/nofile 5/nofile 2048/" -e "s/nofile 4/nofile 1024/" /etc/security/limits.conf',
  onlyif  => 'grep -qE "nofile [45]" /etc/security/limits.conf',
  path    => '/usr/bin:/bin',
  require => File['/etc/security/limits.conf'],
}

# Reload the limits to apply changes
exec { 'reload_limits':
  command     => 'ulimit -n 2048',
  refreshonly => true,
  subscribe   => Exec['Correct file descriptor limits'],
}

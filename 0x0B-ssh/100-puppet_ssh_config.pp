# A Puppet manifest that makes changes to my servers configuration file

file_line { 'Use this private key':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '  IdentityFile ~/.ssh/school',
}

file_line { 'Refuse Password Authentication':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '  PasswordAuthentication no',
}

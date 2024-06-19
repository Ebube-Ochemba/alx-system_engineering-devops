# 0-strace_is_your_friend.pp
# Puppet manifest to fix typo errors in .phpp files

# Ensure the directory exists
file { '/var/www/html':
  ensure => 'directory',
  owner  => 'www-data',
  group  => 'www-data',
  mode   => '0755',
}

# Search for .phpp and replace with .php
exec { 'fix-phpp-typo':
  command => "grep -rl 'phpp' /var/www/html/wp-settings.php | xargs sed -i 's/phpp/php/g'",
  path    => ['/bin', '/usr/bin'],
  onlyif  => "grep -rl 'phpp' /var/www/html/wp-settings.php",
}

# Notify the service to restart Apache after fixing the typo
service { 'apache2':
  ensure    => 'running',
  enable    => true,
  subscribe => Exec['fix-phpp-typo'],
}

# Reload Apache service to apply changes
exec { 'reload-apache2':
  command     => '/usr/sbin/service apache2 reload',
  path        => ['/bin', '/usr/bin', '/usr/sbin'],
  refreshonly => true,
  subscribes  => Exec['fix-phpp-typo'],
}

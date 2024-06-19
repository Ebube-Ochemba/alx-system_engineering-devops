# Puppet manifest to fix the typo error in wp-settings.php

$typo_file = '/var/www/html/wp-settings.php'

# Ensure the file is present
file { $typo_file:
  ensure => 'present',
  mode   => '0644',  # Ensure proper permissions
  owner  => 'www-data',
  group  => 'www-data',
}

# Correct the typo error using an exec resource
exec { 'correct_phpp_typo':
  command => "sed -i 's/class-wp-locale.phpp/class-wp-locale.php/g' ${typo_file}",
  path    => ['/bin', '/usr/bin'],
  onlyif  => "grep 'class-wp-locale.phpp' ${typo_file}",  # Only run if the typo exists
  require => File[$typo_file],  # Ensure the file resource is managed before executing the command
}

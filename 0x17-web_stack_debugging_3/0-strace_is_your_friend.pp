# Puppet manifest to fix the typo error in wp-settings.php


$typo_file = '/var/www/html/wp-settings.php'

# Ensure the file is present
file { $typo_file:
  ensure => 'present',
}

# Correct the typo error
exec { 'correct_phpp_typo':
  command => "sed -i 's/class-wp-locale.phpp/class-wp-locale.php/g' ${typo_file}",
  path    => ['/bin', '/usr/bin']
}
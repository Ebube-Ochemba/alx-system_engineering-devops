# Pupper manifet to install and configure nginx


# Update package repositories
exec {'update':
  command => '/usr/bin/apt-get update',
}

# Ensure Nginx service is installed
-> package { 'nginx':
  ensure => installed,
}

# Custom HTTP response header
-> file_line { 'add X-Served-By header':
  path  => '/etc/nginx/sites-available/default',
  match => '^server {',
  line  => "server {\n\tadd_header X-Served-By \"${::hostname}\";",
  multiple => false,
}

# Restart Nginx
-> exec {'restart nginx':
  command => '/usr/sbin/service nginx restart',
}

# Pupper manifet to install and configure nginx

$tag = "add_header X-Served-By ${hostname};"

# updating apt
exec { 'update':
  command  => 'sudo apt-get -y update',
  provider => shell,
}

# adds the header to the file
-> file_line { 'Add custom HTTP server':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => $tag,
}

# restarting nginx
-> exec { 'service -y nginx':
  command => '/usr/sbin/service nginx restart',
}

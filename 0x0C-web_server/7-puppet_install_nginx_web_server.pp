# A Puppet manifest that installs and configures an Nginx server to:
# 	listen on port 80.
# 	returns a page that contains the string "Hello World!",
#		when querying Nginx at its root /, using Curl,
#		with a Get request.
# 	The redirection must be a "301 Moved Permanently".

# Update Server
exec { 'apt-get-update':
  command => '/usr/bin/apt-get update',
}

# Install Nginx
package { 'nginx':
  ensure  => installed,
  require => Exec['apt-get-update'],
}

# Ensure Nginx listens to port 80
firewall { 'Allow Nginx HTTP':
  port   => 80,
  proto  => 'tcp',
  action => 'accept',
}

# Configure server to return "Hello World!" on root
file { '/var/www/html/index.nginx-debian.html':
  content => 'Hello World!',
  require => Package['nginx'],
}

# Configure Nginx "301 redirect"
exec {'redirect_me':
  command  => "/bin/sed -i '/server_name _;$/a\\ \\t\\trewrite ^/redirect_me https://youtu.be/dQw4w9WgXcQ?si=gOoTgc3trB6Ozv8c permanent;' /etc/nginx/sites-available/default",
  unless   => "/bin/grep -q 'rewrite ^/redirect_me' /etc/nginx/sites-available/default",
  require  => Package['nginx'],
  notify   => Service['nginx'],
}

# Ensure Nginx service
service { 'nginx':
    ensure  => running,
    enable  => true,
    require => Package['nginx'],
}

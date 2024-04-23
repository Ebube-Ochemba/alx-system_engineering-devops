# A Puppet manifest that installs and configures an Nginx server to:
# 	listen on port 80.
# 	returns a page that contains the string "Hello World!",
#		when querying Nginx at its root /, using Curl,
#		with a Get request.
# 	The redirection must be a "301 Moved Permanently".

# EnsureNginx is installed
package { 'nginx':
    ensure => installed,
}

# Configure Nginx "301 redirect"
file_line { 'Add redirection, 301':
    ensure => 'present',
    path   => '/etc/nginx/sites-available/default',
    after  => 'listen 80 default_server;',
    line   => 'rewrite ^/redirect_me https://youtu.be/dQw4w9WgXcQ?si=gOoTgc3trB6Ozv8c permanent;',
}

# Configure server to return "Hello World!" on root
file { '/var/www/html/index.nginx-debian.html':
    content => 'Hello World!',
}

# Ensure Nginx service
service { 'nginx':
    ensure  => running,
    require => Package['nginx'],
}

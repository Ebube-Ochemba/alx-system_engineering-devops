# Pupper manifet to install and configure nginx


# Ensure Nginx package is installed
package { 'nginx':
    ensure => installed,
    require => Exec['update server'], # Ensure update server exec runs first
}

# Custom HTTP response header
file_line { 'add X-Served-By header':
    path    => '/etc/nginx/sites-available/default',
    line    => '    add_header X-Served-By $HOSTNAME;',
    after   => 'listen 80 default_server;',
    notify  => Service['nginx'], # Restart Nginx when the file is modified
}

# Ensure Nginx service is running and enabled
service { 'nginx':
    ensure  => running,
    enable  => true,
    require => Package['nginx'], # Ensure Nginx package is installed before starting the service
}

# Update package repositories
exec { 'update server':
    command  => 'apt -y update',
    path     => ['/bin', '/usr/bin/'],
    refreshonly => true, # Only run when triggered
}

# Pupper manifet to install and configure nginx


# Update package repositories
exec { 'update server':
  command  => 'sudo apt -y update',
  provider => shell,
}

# Install Nginx
-> exec { 'install nginx':
    command => 'sudo apt -y install nginx',
    provider => shell,
}

# Custom HTTP response header
-> exec { 'non-standard header':
    command => 'sudo sed -i "/error_page 404.*/a\ \t\tadd_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default',
    provider  => shell,
}

# Restart Nginx
-> exec { 'restart nginx':
    command => 'sudo service nginx restart',
    provider => shell,
}

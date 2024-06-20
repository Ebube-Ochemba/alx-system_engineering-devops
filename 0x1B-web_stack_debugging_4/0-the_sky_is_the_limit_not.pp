# A Puppet manifest to increase the open file limit for Nginx and restart the service to apply changes

# Increase the open file limit for Nginx from 15 to 4096 in /etc/default/nginx
exec { 'increase_ulimit_nginx':
  command   => 'sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
  provider  => shell,
  onlyif    => 'grep -q "ULIMIT=\"-n 15\"" /etc/default/nginx',
  logoutput => true,
  notify    => Exec['restart_nginx'], # Notify the restart exec resource upon change
}

# Restart the Nginx service to apply the new configuration
exec { 'restart_nginx':
  command   => 'service nginx restart',
  provider  => shell,
  refreshonly => true, # Only run this command if notified
  logoutput => true,
}

# Optimize Nginx web server configuration

# Install nginx
package { 'nginx':
  ensure   => 'installed',
}

# Congigure nginx
file { '/etc/nginx/nginx.conf':
  ensure  => file,
  content => template('nginx/nginx.conf.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Define Service for nginx
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx'],
}

# Optimize Nginx web server configuration

exec { 'change_nginx_config':
  command     => '/usr/bin/sed -i s/15/1000/ /etc/default/nginx',
  path        => ['/usr/bin'],
  refreshonly => true,
  notify      => Service['nginx'],
}

# endure nginx is running
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Exec['change_nginx_config'],
}

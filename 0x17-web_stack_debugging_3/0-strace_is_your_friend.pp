# find out why apche is returning 500 erroe and fix it
exec { 'affected_file':
  command     => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path        => ['/usr/local/bin', '/usr/bin', '/bin'],
  refreshonly => true,
}

service { 'apache2':
  ensure  => 'running',
  enable  => true,
  require => Exec['affected_file'],
}

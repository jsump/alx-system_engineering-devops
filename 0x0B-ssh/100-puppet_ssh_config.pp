# This manifest makes changes to the configuration file
file { 'etc/ssh/ssh_config':
  ensure  => file,
  content => "
    Host 100.25.31.195
       IdentityFile ~/.ssh/school
       PasswordAuthentication no
  ",
  mode    => '0600',
}

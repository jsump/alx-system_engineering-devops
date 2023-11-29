# This manifest makes changes to the configuration file
file { '/home/ubuntu/.ssh/config':
  ensure  => file,
  content => "
    Host 100.25.31.195
       IdentityFile ~/.ssh/school
       PasswordAuthentication no
  ",
  mode    => '0600',
}

# set up client SSH configuration file so that you can connect to a server without typing a password
exec { '/etc/ssh/ssh_config':
    command => ['/usr/bin/sed \'s/#   PasswordAuthentication yes/    PasswordAuthentication no/\', '/etc/ssh_config'],
}
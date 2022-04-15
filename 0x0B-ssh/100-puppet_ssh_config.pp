# set up client SSH configuration file so that you can connect to a server without typing a password
exec { "sed -i 's|#\s*PasswordAuthentication\syes|\s\s\s\sPasswordAuthentication\sno|g' /etc/ssh/ssh_config":
    path    => '/usr/bin/',
};
exec { "sed -i 's|#\s*IdentityFile\s~/.ssh/id_rsa|\s\s\s\sIdentityFile\s~/.ssh/school|g' /etc/ssh/ssh_config":
    path    => '/usr/bin/',
}
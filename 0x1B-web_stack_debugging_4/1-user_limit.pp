#bug fix user
exec { "sed -i '/holberton hard nofile 5/d' /etc/security/limits.conf":
    path => ['/bin'],
}
exec { "sed -i '/holberton soft nofile 4/d' /etc/security/limits.conf":
    path => ['/bin'],
}

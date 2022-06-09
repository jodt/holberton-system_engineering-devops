#bug fix requests on server
exec { "sed -i 's/n 15/n 4096/' /etc/default/nginx":
    path => ['/bin'],
}
exec {'sudo service nginx restart':
    path => ['/usr/bin'],
}

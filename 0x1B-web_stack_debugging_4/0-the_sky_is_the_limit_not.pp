# make even more requestsss!!

exec { 'fix--for-nginx':
  command     => '/bin/sed -i "s/15/4096/" /etc/default/nginx,
  path        => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games',
}

exec { 'nginx-restart':
  command => '/etc/init.d/nginx restart',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games',
}

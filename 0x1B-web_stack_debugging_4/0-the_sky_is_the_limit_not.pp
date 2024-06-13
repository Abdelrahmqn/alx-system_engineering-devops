# make even more requestsss!!

exec {'modify max open files limit setting':
  command => 'sed -i "s/15/3000/" /etc/default/nginx && sudo service nginx restart',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}



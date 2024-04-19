exec { 'pkill':
  path    => ['/usr/bin', '/usr/sbin', '/bin']
  command => 'pkill -9 -f killmenow',
}

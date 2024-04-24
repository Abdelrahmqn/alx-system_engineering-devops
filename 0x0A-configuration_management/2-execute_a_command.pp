# this file should kill process called killmenow.
exec { 'kill_killmenow':
  command => '/usr/bin/pkill -f killmenow',
  path    => ['/usr/bin'],
}

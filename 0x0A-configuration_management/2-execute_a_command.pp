exec { 'pkill':
  unless  => process { name => 'killmenow' },
  command => '/usr/bin/pkill -f killmenow',
}

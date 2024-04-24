# install flask from pip3 _ python
# werkuezug now is 2.0.3
exec { 'install_flask':
  command => '/usr/bin/pip3 install flask==2.1.0 ; pip3 install werkzeug==2.0.3',
  path    => ['/usr/bin'],
}

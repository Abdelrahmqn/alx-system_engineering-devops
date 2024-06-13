# give a permision for holberton


exec { 'give-soft-permisions-forholperton':
  command => "sed -i '^/"holberton soft/s/4/5000/' /etc/security/limits.conf",
  path    => ['/bin', '/usr/bin'],
}


exec { 'give-hard-permisions-forholperton':
  command => "sed -i '^/"holberton hard/s/5/5000/' /etc/security/limits.conf",
  path    => ['/bin', '/usr/bin'],
}

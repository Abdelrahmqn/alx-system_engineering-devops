#!/usr/bin/pup
# Based on requirements install

package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}

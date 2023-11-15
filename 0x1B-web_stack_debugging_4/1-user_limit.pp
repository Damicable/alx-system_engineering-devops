# Configuration to allow login with the holberton user and open
#a file without any error message.

# This increases hard limit for the user holberton 
exec { 'increase-hard-limit-holberton':
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

# This increases soft limit for the user Holberton
exec { 'increase-soft-limit-holberton':
  command => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

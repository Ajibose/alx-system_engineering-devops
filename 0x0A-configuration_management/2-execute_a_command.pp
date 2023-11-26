# Execute a command

exec { 'kill':
  command => 'pkill -TERM -f killmenow',
  path    => '/usr/bin',
}

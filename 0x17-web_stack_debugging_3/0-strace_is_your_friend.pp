#fix 500 error
exec {'fix-wdp':
command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path  => '/usr/local/bin/:/bin/'

}

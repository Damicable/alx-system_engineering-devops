#Fixng a typo error in the wp php config

exec {'searchAndReplace':
  provider => shell,
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}

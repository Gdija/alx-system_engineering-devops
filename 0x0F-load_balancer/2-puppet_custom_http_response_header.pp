#create a custom header with puppet
exec { 'http config':
  provider => shell,
  command  => 'sudo apt-get -y update && sudo apt-get -y install nginx && sudo sed -i "27i\\\tadd_header X-Served-By \$HOSTNAME;" /etc/nginx/nginx.conf && echo "Hello World!" | sudo tee /var/www/html/index.html && sudo service nginx restart',
}

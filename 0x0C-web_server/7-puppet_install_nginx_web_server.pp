# trying to use puppet file to update & install nginx in server


exec { 'install_nginx':
  command => '/usr/bin/apt-get update && /usr/bin/apt-get install -y nginx',
}

file {' /var/www/html/index.ngins-debian.html':
  content => 'Hello World!',
}

file { '/etc/nginx/sites-enabled/default':
  content => "server {
	listen 80 default_server;
	listen [::]:80 default_server;

  location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }",
}
exec { 'reload_nginx':
  command     => 'usr/bin/nginx -s reload',
  refreshonly => true,

}

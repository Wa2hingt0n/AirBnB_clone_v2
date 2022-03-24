#!/usr/bin/env bash
# This script sets up a web server for the deployment of 'web_static', a static
#  web page.

# Installing nginx
apt-get update
apt-get -y install nginx

# Creating root directories
mkdir -p /data /data/web_static /data/web_static/releases /data/web_static/shared /data/web_static/releases/test

# Creating an index.html file
touch /data/web_static/releases/test/index.html

# Adding content to the index.html file
printf %s "
<html>
    <head>
    </head>
    <body>
        <h1>My Page</h1>
        <p>This is the first paragraph.</p>
    </body>
</html>
" > /data/web_static/releases/test/index.html

# Creating a symbolic link to the /data/web_static/releases/test/ directory
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Assigning ownership of the /data forlder to the 'ubuntu' user
chown -R ubuntu:ubuntu /data/

# Updating the nginx configuration file
printf %s "
server {
    listen 80;
    listen [::]:80;

    add_header X-Served-By 1667-web-02;

    root /var/www/html;
    index index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }

    error_page 404 /404.html;
    location /404 {
        root /var/www/html;
        internal;
    }
}
" > /etc/nginx/sites-available/default

# Restarting nginx
service nginx restart

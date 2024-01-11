#!/usr/bin/env bash
# Sets up the web servers for the deployment of web_static

# Install Nginx if it not already installed
sudo apt-get update
sudo apt-get install -y nginx

# Create the folder /data/ if it doesn’t already exist
sudo mkdir -p /data/
# Create the folder /data/web_static/ if it doesn’t already exist
sudo mkdir -p /data/web_static/
# Create the folder /data/web_static/releases/ if it doesn’t already exist
sudo mkdir -p /data/web_static/releases/
# Create the folder /data/web_static/shared/ if it doesn’t already exist
sudo mkdir -p /data/web_static/shared/
# Create the folder /data/web_static/releases/test/ if it doesn’t already exist
sudo mkdir -p /data/web_static/releases/test/

# Create a fake HTML file /data/web_static/releases/test/index.html (with simple content, to test your Nginx configuration)
sudo echo "Noble Eluwah" > /data/web_static/releases/test/index.html

# Create a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group
sudo chown -R ubuntu /data
sudo chgrp -R ubuntu /data

# Update the Nginx configuration to serve the content of /data/web_static/current/
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

# Restart nginx server
sudo service nginx restart

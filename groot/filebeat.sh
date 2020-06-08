#!/bin/bash

# TODO check filebeat is installed
curl -L -O https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-7.5.0-amd64.deb
sudo dpkg -i filebeat-7.7.1-amd64.deb

# Enable and configure the system module
# TODO Modify the settings in the modules.d/system.yml file.
filebeat modules enable system

# Start Filebeat
filebeat setup
filebeat -e

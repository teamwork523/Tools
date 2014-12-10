#/bin/bash

# Alternative solution: curl -s checkip.dyndns.org|sed -e 's/.*Current IP Address: //' -e 's/<.*$//'
wget -qO- http://ipecho.net/plain ; echo

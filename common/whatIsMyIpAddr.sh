#/bin/bash

wget -qO- http://ipecho.net/plain ; echo
# Alternative solution: curl -s checkip.dyndns.org|sed -e 's/.*Current IP Address: //' -e 's/<.*$//'

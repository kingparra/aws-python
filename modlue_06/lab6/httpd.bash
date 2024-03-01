#!/usr/bin/env bash
yum install httpd -y
systemctl enable --now httpd

cat > /var/www/html/index.html << EOF
<html>
    <head>
        <title> Example Web Server</title>
    </head>
    <body>
        <div>
            <center>
                <h2>Welcome AWS $(hostname -f)</h2>
                <hr/>$(curl "http://169.254.169.254/latest/meta-data/instance-id")
            </center>
        </div>
    </body>
</html>
EOF

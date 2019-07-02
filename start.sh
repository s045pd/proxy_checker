kill -9 `ps -ef|grep "caddy"|awk '{print $2}'`
nohup caddy >> /var/log/caddy.log  &

kill -9 `ps -ef|grep "python3 server.py"|awk '{print $2}'`
nohup python3 server.py >> /var/log/tornado.log  &
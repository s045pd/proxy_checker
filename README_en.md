<h1 align="center">Proxy Anonymous Detection</h1>

<p align="center">
    <img src="https://img.shields.io/badge/language-python3-orange.svg">
    <img  src="https://img.shields.io/badge/platform-mac|lunix|window-orange.svg" target="_blank" />
    <a href="https://github.com/aoii103/proxy_checker/blob/master/LICENSE">
        <img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-yellow.svg" target="_blank" />
    </a>
</p>


This is an proxy detection tool that works with the middleware combination.

### ✨ Schematic

![./media/proxy_level.png](./media/proxy_level.png)

### Python3 Environment

download and install *`anaconda 3.5`*

```
pip install -r ./requirements.txt
pip install -U 'requests[socks]'
```

###  🚀 Enable Service

> Please change conf_dev.py to conf.py

Upload the file code to the server and modify the `IP.SERVER` parameter of `conf.py` to the external IP of the server.

```python
class IPs(Enum):
    CLIENT = "A.B.C.D"
    SERVER = "A.B.C.D"

```
And run the `bash start.sh` command to start the `Caddy` and `server` services.

### Test

Now we can access `http://\[server_ip\]/client\=B.C.D.E` through the onion browser and we can see that the returned type is `ELITE`.

![](./media/target.png)

> A total of two parameters, respectively, `client` refers to the actual IP address of the client, and `proxy` refers to the IP address of the proxy.

### Batch Test

We do batch testing by modifying the contents of the `proxy_list` in the `client.py` script. 

For example:

```
proxy_list = [("1.1.1.1",8888),("2.2.2.2",9999))]
```

## 📝 License

Copyright © 2019 [Franck Abgrall](https://github.com/aoii103).<br />
This project is [MIT](https://github.com/aoii103/proxy_checker/blob/master/LICENSE) licensed.

---


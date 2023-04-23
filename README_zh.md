# PyGateway

![](https://img.shields.io/badge/python-v3.6%2B-blue)

这是一个用 Python 语言构建的 API 网关，它包括以下功能：路由分发、负载均衡和鉴权认证。我们还将继续开发更多功能并提供快速部署方案。

## 环境配置

- python 3.6+
- Flask 2.0.3

## 使用方法

安装依赖

```shell
pip install -r requirements.txt
```

修改配置文件config.py

```python
# Port to listen on
LISTEN_PORT =  5000

# API method, optional POST, GET and MIXED. 
# Note that if you choose to MIXED, you need to manually configure
# the method when configuring the api parameters
METHOD = 'POST'

# Authentication method, optional token, token-secret,
# token-signature, token-secret-signature
AUTH_METHOD = 'token-signature'

# Authentication encryption method, optional md5, sha256
ENCRYPTION = 'sha256'

# Data transmission method, optional args, form, json. 
# We recommend using json. Note that if you choose form and json, 
# please choose the POST method when configuring the API method.
TRANSMISSION_METHOD = 'json'

# Load balancing mode, including random, cycle, random-weight, 
# cycle-weight four modes
BALANCE_MODE = 'random'
```

初始化数据库

```shell
flask db init
```

创建迁移文件

```shell
flask db migrate
```

更新数据库

```shell
flask db upgrate
```

启动服务

```shell
python manage.py
```
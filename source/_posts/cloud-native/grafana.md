---
title: Grafana + Loki + Promtail + Prometheus + Traefik - 监控服务指标以及日志告警
tags:
  - CloudNative
  - Grafana
  - Loki
  - Promtail
  - Prometheus
  - Traefik
categories:
  - cloud-native
date: 2022-07-20 15:46:39
---

# 监控服务指标以及日志告警

> 示例仓库地址: [Github](https://github.com/lingfromSh/service-monitor-example)

通过收集服务日志以及服务指标，设置相应的监控规则，监控服务响应异常，网络异常，磁盘异常等。

做到及时响应的同时，快速定位问题。


## 0. 国内防火墙问题

将PROXY传入k3s容器内，同时配置docker daemon的PROXY.可以解决大部分容器内翻墙需求。

```shell
k3d cluster create --env "HTTP_PROXY=${HOST_IP}@server:*" --env "HTTPS_PROXY=${HOST_IP}@server:*" ...
```


## 1. 编写一个简单的服务

这里使用fastapi去编写一个简单的服务，这个服务提供四个接口,分别返回200,400,404,500。

```python
# server.py

from fastapi import FastAPI
from fastapi.responses import Response

app = FastAPI()


@app.get("/200")
async def return200():
    return Response(content="OK")


@app.post("/400")
async def return400():
    return Response(content="Bad Request", status_code=400)


@app.get("/404")
async def return404():
    return Response(content="Not Found", status_code=404)


@app.get("/500")
async def return500():
    return Response(content="Internal Server Error", status_code=500)

```

## 2. 搭建Grafana

```shell
helm install grafana grafana/grafana
```

## 3. 搭建Loki

```shell
helm install loki grafana/loki
```

## 4. 搭建Promtail

```shell
helm install promtail grafana/promtail
```

## 5. 搭建prometheus

```shell
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm install prometheus prometheus-community/prometheus
```

## 6. 搭建Grafana仪表盘

![img](cloud-native/grafana/2022-08-06_14-11.png)
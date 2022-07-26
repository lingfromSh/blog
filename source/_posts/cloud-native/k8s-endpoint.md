---
title: K8S - Endpoint 
date: 2022-07-19 23:42:05
tags:
    - Kubernetes
---

# K8S Endpoint

## 作用

Endpoint用于定义服务入口，这个入口既可以是k8s内部服务，也可以是外部服务。
Endpoint一般和Service一起配套使用。

当Service通过selector绑定deployment或者statefulset时，都会自动生成一份相同名字的Endpoint。
但是当管理外部服务的时候，就需要我们自己手动创建了。

## 手动管理Endpoint的使用场景

考虑到K8S调度有状态服务的能力，以及涉及到一些特殊硬件设备的服务，一般他们都会被部署到外部独立管理，所以为了用集群的能力去管理则需要Endpoint去管理他们。

```yaml
apiVersion: v1
kind: Service
metadata:
  name: external-service
spec:
  ports:
    - name: web
      port: 80 
      targetPort: 80 # 非必须
---
apiVersion: v1
kind: Endpoint
metadata:
  name: external-service
spec:
  addresses:
    - ip: xxx.xxx.xxx.xxx
  ports:
    - name: web  # 此处必须和Service中定义的保持一致
      port: 80   # 此处必须和Service中定义的保持一致
```

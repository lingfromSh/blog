---
title: istio 从入门到入土
tags:
  - istio
  - ServiceMesh
  - CloudNative
categories:
  - cloud-native
date: 2022-07-18 01:59:14
---
# Istio 从入门到入土

## 流量管理
Istio 的流量路由规则可让您轻松控制服务之间的流量和 API 调用。Istio 简化了断路器、超时和重试等服务级别属性的配置，并可以轻松设置重要任务，例如 A/B 测试、金丝雀发布和基于百分比的流量拆分的分阶段发布。它还提供开箱即用的可靠性功能，帮助您的应用程序更灵活地应对依赖服务或网络的故障。

Istio 的流量管理模型依赖于使者 与您的服务一起部署的代理。您的网格服务发送和接收的所有流量（数据平面流量）通过 Envoy 代理，从而可以轻松地引导和控制网格周围的流量，而无需对服务进行任何更改。

如果您对本指南中描述的功能如何工作的详细信息感兴趣，可以在 [架构概述](https://istio.io/latest/docs/ops/deployment/architecture/)中找到有关 Istio 流量管理实现的更多信息。本指南的其余部分介绍了 Istio 的流量管理功能。

### 虚拟服务
最基础的路由功能单位，每个虚拟服务都会有一系列路由规则组成，istio会按顺序执行匹配这些规则来路由请求。
```yaml
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: reviews
spec:
  hosts:
  - reviews
  http:
  - match:
    - headers:
        end-user:
          exact: jason
    route:
    - destination:
        host: reviews
        subset: v2
  - route:
    - destination:
        host: reviews
        subset: v3
```

 
### 目的规则
目的地规则是在虚拟服务规则执行后，引导流量。
例如可以定义你的多个版本的服务的实际路由规则
```yaml
apiVersion: networking.istio.io/v1alpha3
kind: DestinationRule
metadata:
  name: my-destination-rule
spec:
  host: my-svc
  trafficPolicy:
    loadBalancer:
      simple: RANDOM
  subsets:
  - name: v1
    labels:
      version: v1
  - name: v2
    labels:
      version: v2
    trafficPolicy:
      loadBalancer:
        simple: ROUND_ROBIN
  - name: v3
    labels:
      version: v3
```

### 网关
管理网格中出入流量，控制何种流量可以流出以及流入。网关配置只会应用给网格边缘运行的单节点Envoy代理，而不会发送给服务负载的Envoy边车代理。提供4-7层网络控制。
通过网关配置egress规则，决定服务是否可以与外部通信，提供更高安全管控能力。

```yaml
apiVersion: networking.istio.io/v1alpha3
kind: Gateway
metadata:
  name: ext-host-gwy
spec:
  selector:
    app: my-gateway-controller
  servers:
  - port:
      number: 443
      name: https
      protocol: HTTPS
    hosts:
    - ext-host.example.com
    tls:
      mode: SIMPLE
      credentialName: ext-host-cert
```

### 服务入口
通过声明服务入口，可以像内部服务一样使用管理外部服务。
你不需要为每个外部服务做此声明，但是这样将不能使用istio特性来控制这些服务的流量。
```yaml
apiVersion: networking.istio.io/v1alpha3
kind: ServiceEntry
metadata:
  name: svc-entry
spec:
  hosts:
  - ext-svc.example.com
  ports:
  - number: 443
    name: https
    protocol: HTTPS
  location: MESH_EXTERNAL
  resolution: DNS
```

### 边车
istio默认每个envoy代理接受并转发负载所有端口上的流量。你可以使用sidecar配置来达到以下效果:
- 调优Envoy代理接受的端口和协议
- 限制Envoy可以达到的服务
```yaml
apiVersion: networking.istio.io/v1alpha3
kind: Sidecar
metadata:
  name: default
  namespace: bookinfo
spec:
  egress:
  - hosts:
    - "./*"
    - "istio-system/*"
```

### 网络故障恢复和验证
istio不仅提供了以上的流量管理能力，同样提供了动态可选的故障回复和错误注入特性。运用这些特性可以促成你的服务更加可靠。

#### 超时
```yaml
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: ratings
spec:
  hosts:
  - ratings
  http:
  - route:
    - destination:
        host: ratings
        subset: v1
    timeout: 10s
```

#### 重试
```yaml
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: ratings
spec:
  hosts:
  - ratings
  http:
  - route:
    - destination:
        host: ratings
        subset: v1
    retries:
      attempts: 3
      perTryTimeout: 2s
```

#### 熔断
```yaml
apiVersion: networking.istio.io/v1alpha3
kind: DestinationRule
metadata:
  name: reviews
spec:
  host: reviews
  subsets:
  - name: v1
    labels:
      version: v1
    trafficPolicy:
      connectionPool:
        tcp:
          maxConnections: 100

```

## 通信安全
支持TLS


## 可见性

- 属性
```
envoy_cluster_internal_upstream_rq{response_code_class="2xx",cluster_name="xds-grpc"} 7163

envoy_cluster_upstream_rq_completed{cluster_name="xds-grpc"} 7164

envoy_cluster_ssl_connection_error{cluster_name="xds-grpc"} 0

envoy_cluster_lb_subsets_removed{cluster_name="xds-grpc"} 0

envoy_cluster_internal_upstream_rq{response_code="503",cluster_name="xds-grpc"} 1
```
- 分布式跟踪
- 日志

## 拓展性
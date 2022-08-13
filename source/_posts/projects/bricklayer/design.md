---
title: BrickLayer - 搬瓦工
date: 2022-08-12 16:33:42
tags:
  - Devops
  - Bricklayer
---

# BrickLayer - 搬瓦工 设计

## 需求

- [ ] 项目管理
  - [ ] 环境管理
    - [ ] 配置管理
  - [ ] CICD管理
  - [ ] 应用监控
  - [ ] 部署报告
  - [ ] 测试报告
- [ ] 基础设施管理
  - [ ] kubernetes
  - [ ] openstack
  - [ ] baremetal
- [ ] 仓库管理
  - [ ] 代码仓库
    - [ ] gitlab
    - [ ] github
  - [ ] 镜像仓库
    - [ ] harbor
- [ ] 账户管理
  - [ ] OAUTH2
  - [ ] 多租户

## 设计

### 技术栈

1. Kubernetes - 底座
2. Rust - 编程语言
3. Tekton - CI pipeline
4. ArgoCD - CD tools
5. ArgoEvent - 事件处理
6. ArgoWorkflow - 工作流
7. Istio - 网管/流量管理
8. Nacos - 配置分发中心

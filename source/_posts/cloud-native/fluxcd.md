---
title: Gitops - ArgoCD vs FluxCD
tags:
  - Kuberetes
  - CICD
categories:
  - cloud-native
date: 2022-07-25 10:57:03
---
# ArgoCD vs FluxCD

比较ArgoCD和FluxCD之前，我们应该先了解一下Gitops

Gitops的基础思想是，将环境放入版本控制系统并通过一个自动流程确保我们的代码运行在代码仓库中描述的状态。

||ArgoCD|FluxCD|
|--|--|--|
||声明式CD工具，可弹性扩展，自带安全管理，支持SSO，多集群多租户。|最初由WeaveWorks开发，现由CNCF托管。Flux支持持续部署和渐进式部署。|
|声明方式|Git,Helm,Kustomize,Jsonnet|Git,Helm|
|安全策略|OAuth2, RBAC|RBAC|
|回滚|支持|不支持|
|同步方式|持续部署|持续部署,渐进式部署|
|通知|webhook, alertmanager, email, grafana, slack, teams, telegram, pushover, github, google chat, pushover, mattermost|alertmanager, azureeventhub, discord, generic, githubdispatch, googlechat, grafana, lark, matrix, teams, opsgenie, rocket, sentry, slack, telegram, webex, azuredevops, bitbucket, github, gitlab|
|Web界面|支持|不支持|
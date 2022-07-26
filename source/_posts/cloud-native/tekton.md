---
title: Tekton 云原生CICD流水线
date: 2022-07-18 02:07:55
tags:
    - Tekton
    - Pipeline
    - CloudNative
---
# Tekton

## 核心概念

### Step - 步骤
一个步骤代表一个容器，去执行命令并输出结果

```yaml
steps:
  - name: deploy-app
  	image: foo/base-image:2.7
	env:	
	  - name: API_KEY
	    valueFrom: 
		  secretKeyRef:
		    name: secure-properties
			key: apiKey
	script: |
	  cloud login -a $(params.api-url)
```

### Task - 任务
一个任务代表一系列步骤的集合

```yaml
apiVersion: tekton.dev/v1beta1
kind: Task
metadata:
  name: deploy-to-my-awesome-cloud
spec:
  params:
  	- name: api-url
	  default: cloud.com
  steps:
    - name: deploy-app
	  image: foo/base-image:2.7
	  env:	
	    - name: API_KEY
		  valueFrom: 
		    secretKeyRef:
			  name: secure-properties
			  key: apiKey
	  script: |
	    cloud login -a $(params.api-url)
```

### Pipeline - 流水线
一条流水线代表一系列任务的集合

```yaml
apiVersion: tekton.dev/v1beta1
kind: Pipeline
metadata:
  name: project-pipeline
spec:
  params:
    - name: api-url
	- name: cloud-region
  tasks:
    - name: clone
	  taskRef:
	    name: git-clone
    - name: build
	  taskRef:
	    name: build
	  runAfter:
	  	- clone
	- name: deploy
	  taskRef:
	    name: deploy
      runAfter:
	  	- build
```
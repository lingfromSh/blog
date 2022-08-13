---
title: 小表驱动大表
date: 2022-08-12 10:38:58
tags:
    - SQL
---

# 小表驱动大表

## 什么是小表驱动大表?

用小的数据集去驱动(匹配)大的数据集

## 为什么需要小表驱动大表

1. 小表驱动大表
```sql
select *from tb_emp_bigdata A where A.deptno in (select B.deptno from tb_dept_bigdata B)
```

2. 大表驱动小表
```sql
select * from tb_dept_bigdata A where A.deptno in(select B.deptno from tb_emp_bigdata B);
select * from tb_dept_bigdata A where A.deptno exists(select 1 from tb_emp_bigdata B where B.deptno=A.deptno);
```

小表驱动大表的主要目的是通过减少表连接创建的次数,加快查询速度.

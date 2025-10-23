---
title: "SimpleAdapter简单适配器"
date: 2025-10-22
categories: ["Android适配器"]
description: "详细介绍Android SimpleAdapter简单适配器的使用方法和参数配置，用于显示复杂布局的列表"
featureimage: "/images/simple-adapter.jpg"
featureimagecaption: "SimpleAdapter简单适配器示意图"
draft: false
---

当创建了一个列表时，列表中的每个元素的布局都是一样的
每个列表元素的名字都是一样的所以可以用Adapter来映射他们的对应关系
```kotlin
SimpleAdapter adapter = SimpleAdapter(this,data,R.layout.xxx,from,to)
```
- `this`：环境上下文
- `data`：数据源
- `R.layout.xxx`：SimpleAdapter所对应的Activity
- `from`：展示的数据的名称
- `to`：展示的数据的控件的id
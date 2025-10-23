---
title: "ArrayAdapter数组适配器"
date: 2025-10-22
tags: ["Android", "ArrayAdapter", "适配器", "ListView"]
description: "详细介绍Android ArrayAdapter数组适配器的使用方法和构造参数，用于显示单一文本的列表"
featureimage: "/images/array-adapter.jpg"
featureimagecaption: "ArrayAdapter数组适配器示意图"
draft: false
---

# 定义
数组适配器，只能用来显示单一的文本。构造方法：
```kotlin
ArrayAdapter(Context context,int resource,int textviewId,List<T>objects)
```
- context：环境上下文
- resource：要放置的view的id
- textviewId：文本需要放在布局中对应id文本控件的位置
- objects：数据源 
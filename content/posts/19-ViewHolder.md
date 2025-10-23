---
title: "ViewHolder模式优化"
date: 2025-10-22
categories: ["Android适配器"]
description: "详细介绍Android ViewHolder模式的使用方法和性能优化原理，通过复用视图提升列表性能"
featureimage: "/images/viewholder-pattern.jpg"
featureimagecaption: "ViewHolder模式示意图"
draft: false
showComments: true
---

当滑动到list中的某个元素时，会将其加载出来，而滑到别的元素后重新滑动到已经加载过得的元素时，会进行重新加载，
# 利用进入RecycleBin获取已经加载过的控件
# 使用ViewHolder进行列表优化
1. 自定义一个类，叫做ViewHolder
2. 将需要保存的视图声明为公开的属性
3. 什么适合保存？当view为null时，完成对ViewHolder的实例化工作，并为各个空间属性赋值
4. 什么时候用？什么时候都要用（性能提升是在view不为null时体现的）
5. 怎么用？当view控件为null时，完成了ViewHolder及内部空间属性初始化工作后，调用一句代码 `view.setTag(holder)`
6. 可是当view不为空时，`holder = view.getTag()`
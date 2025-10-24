---
title: "PopupWindow弹出窗口"
date: 2025-10-22
categories: ["Android development"]
description: "详细介绍Android PopupWindow弹出窗口的使用方法和动画效果设置"
featureimage: "/images/popup-window.jpg"
featureimagecaption: "PopupWindow弹出窗口示意图"
draft: false
showComments: true
---

# 定义
长按时，在长按位置弹出的气泡框
# 步骤
1. 创建PopupWindow对象实例
2. 设置背景，注册时间监听器和添加动画
3. 显示PopupWindow
4. `setOutsideTouchable(true)`设置能响应外部的点击事件
5. `setTouchable(true)`设置弹窗能响应点击事件
# 弹窗动画
1. 创建动画资源
2. 创建一个style应用动画资源
3. 对当前弹窗的动画风格设置为第二步的资源索引
## 动画类型
- alpha
- rotate
- scale
- set
- translate
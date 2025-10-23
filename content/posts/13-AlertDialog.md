---
title: "AlertDialog对话框"
date: 2025-10-22
categories: ["Android对话框"]
description: "详细介绍Android AlertDialog对话框的使用方法和自定义对话框的实现步骤"
featureimage: "/images/alert-dialog.jpg"
featureimagecaption: "AlertDialog对话框示意图"
draft: false
---

# 定义
消息提示机制，长用于向用户传递信息，提示或警告用户的行为。通用的方法有：
- `setTitle`
- `setMesssage`
- `create`
- `show`
# 实现步骤

1. 先实例化一个`AlertDialog.Builder`类型的对象其参数为环境上下文
2. 使用`builder.setTitle()`方法来设置提示消息的title
3. 使用`builder.setMessage()`方法来设置消息提示的内容
4. 使用`builder.setPositiveButton()`方法来设置单机确认时的动作
5. 使用`builder.setNegativeButton()`方法来设置点击取消时的动作
6. 使用`builder.create()`来创建Dialog对象
7. 最后使用`dialog.show()`来展示对话框
# 自定义对话框
## 步骤
1. 设置布局
2. 设置Style
3. 自定义Dialog
4. 显示
---
title: "Android开发方式"
date: 2025-10-22
tags: ["Android", "开发方式", "Java", "XML"]
description: "本文详细介绍了Android的两种开发方式：Java代码开发和XML文件开发，并推荐使用XML方式进行开发"
featureimage: "/images/android-development.jpg"
featureimagecaption: "Android开发方式对比图"
draft: false
---

# Android开发方式

Android UI的开发方式有两种：
- java代码开发
- xml文件开发

前者要创建布局对象，并定义布局内容，然后定义布局的属性（宽、高、背景等等）
再将内容设置为该布局

后者只需要添加xml标签，并且添加定义xml标签的属性即可实现页面的编写

> \[!faq\] 我们在开发过程中需要使用哪种方式开发？
> 建议使用后者开发，java代码开发的方式需要编写很多代码，包括对象创建，属性赋值，页面赋值等等等等，但是xml并不需要这么多的开发步骤，而是直接在布局文件中编写代码

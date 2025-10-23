---
title: "FrameLayout帧布局"
date: 2025-10-22
categories: ["Android布局"]
description: "详细介绍Android FrameLayout帧布局的使用方法和属性配置，包括层叠排列和layout_gravity属性"
featureimage: "/images/framelayout-control.jpg"
featureimagecaption: "FrameLayout帧布局示意图"
draft: false
---

# FrameLayout 帧布局

在该容器下，所有的控件都是从最底部开始层叠排列的

重要属性：
- `android:layout_gravity`：控制控件所在的位置
- `android:layout_gravity`：控件的前景
- `android:layout_gravity`：前景重力

```xml
<?xml version="1.0" encoding="utf-8"?>  
<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android"  
    android:layout_width="match_parent"  
    android:layout_height="match_parent">  
    <TextView        
	    android:layout_width="350dp"  
        android:layout_height="350dp"  
        android:layout_gravity="center"  
        android:background="#0000FF"/>  
    <TextView        
	    android:layout_width="330dp"  
        android:layout_height="330dp"  
        android:layout_gravity="center"  
        android:background="#9932CC"/>  
    <TextView        
	    android:layout_width="300dp"  
        android:layout_height="300dp"  
        android:layout_gravity="center"  
        android:background="#FF1493"/>  
    <TextView        
	    android:layout_width="270dp"  
        android:layout_height="270dp"  
        android:layout_gravity="center"  
        android:background="#DA70D6"/>  
    <TextView        
	    android:layout_width="240dp"  
        android:layout_height="240dp"  
        android:layout_gravity="center"  
        android:background="#00BFFF"/>  
    <TextView        
	    android:layout_width="200dp"  
        android:layout_height="200dp"  
        android:layout_gravity="center"  
        android:background="#191970"/>  
</FrameLayout>
```

最终效果为：
![[1d62d03826b12e324c72ade5639ea696_MD5.png]]

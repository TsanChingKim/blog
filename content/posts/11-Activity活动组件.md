---
title: "Activity活动组件"
date: 2025-10-22
categories: ["Android组件"]
description: "详细介绍Android Activity活动组件的概念、生命周期、启动模式、跳转方式和信息传递方法"
featureimage: "/images/activity-component.jpg"
featureimagecaption: "Activity活动组件示意图"
draft: false
---

# Activity 活动组件

## 什么是Activity

什么是activity？app中的每一个页面都是activity

Activity启动的简单流程：
Activity与Layout之间的关系

## Activity之间的跳转

在跳转触发的监听器中创建一个`Intent`并调用`startActivity()`方法将该`Intent`传入其中

Activity之间的跳转是一种栈的数据结构

### Standard
这也是系统标准的运行模式

![ea4d203a90a53056afd2d9704d45e2b3_MD5](https://raw.githubusercontent.com/TsanChingKim/picGo/main/pic/ea4d203a90a53056afd2d9704d45e2b3_MD5.png)
### SingleTop
顶部复用模式
如果顶部还有用户打开的 Activity 就不会创建新的 Activity
![4efc467113246a3a5c6406ee3ff0ec71_MD5](https://raw.githubusercontent.com/TsanChingKim/picGo/main/pic/4efc467113246a3a5c6406ee3ff0ec71_MD5.png)
### SingleTask
如果顶部没有当前用户打开的Activity则会先清除顶部的 Activity 直到找到该Activity
![7a9c1d7341c3db700ae5d829baa499b9_MD5](https://raw.githubusercontent.com/TsanChingKim/picGo/main/pic/7a9c1d7341c3db700ae5d829baa499b9_MD5.png)
### SingleInstance
将某个操作模式单独放入到一个栈中
![c66414ac7266fe9523803f4572e68202_MD5](https://raw.githubusercontent.com/TsanChingKim/picGo/main/pic/c66414ac7266fe9523803f4572e68202_MD5.png)

## Activity 启动方式

### 显式启动
使用Intent方法传入要启动的 Activity

### 隐式启动
通过Intent的action、category、data等属性来启动Activity

### startActivityForResult
可以使用requestCode进行打开的Activity的分辨

## Activity 生命周期

![3ef71fe678c5084426406babcc0c36c7_MD5](https://raw.githubusercontent.com/TsanChingKim/picGo/main/pic/3ef71fe678c5084426406babcc0c36c7_MD5.png)

### 单个Activity的生命周期

{{< mermaid >}}
---
title: 基础操作会引发的生命周期变化
---
graph TD
	subgraph 再次启动
		G(onCreate) --> H(onStart)
		H --> I(onResume)
	end
	subgraph 正常退出
		D(onPause) --> E(onStop)
		E --> F(onDestroy)
	end
	subgraph 正常进入
		 A(onCreate) --> B(onStart)
		 B --> C(onResume)
	end
{{< /mermaid >}}

### 已经处于前台的 Activity，点击主页按钮离开当前 Activity

{{< mermaid >}}
graph TD
	subgraph 回到 Activity
		C(onRestart) --> D(onStart)
		D --> E(onResume)
	end
	subgraph 单击主页按钮离开页面
		A(onPause) --> B(onStop)
	end
{{< /mermaid >}}

### Activity不可操作（如息屏、打开了其他Activity）而应用被强行杀死了

{{< mermaid >}}
graph TD
	subgraph 重新回到Activity
		C(onCreate) --> D(onStart)
		D --> E(onResume)
	end
	subgraph 不可操作并被kill
		A(onPause) --> B(onStop)
	end
{{< /mermaid >}}

>[!error] 注意
>普通对话框对生命周期没有任何影响，如果有个Activity伪装成对话框模式，那么当他启动时，之前的Activity:onPause，"对话框"消失后，回调onResume

# Activity之间信息传递
## 传递简单内容
通过putExtra来进行放入操作，通过getXXXExtra来获取内容
## 传递对象
通过putExtra来传递序列化之后的对象，通过getSerializableExtra()方法来获取对象
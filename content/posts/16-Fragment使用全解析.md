# Fragment 概念
## 概念
为了给Pad等更大的屏幕提供公开的UI支持
## Fragment VS Activity
1. Fragment 是到 Android 3.0+ 以后
2. 一个Activity可以运行多个Fragment
3. Fragment 不能脱离 Activity 而存在
4. Activity 是屏幕的主题，而Fragment 是 Activity 的一个组成元素
## Fragment 生命周期
# Fragment 加载方式
## 静态加载
1. 创建 Fragment，调用onCreate方法
2. 在xml中创建fragment后使用android:name指定fragment1的名称
## 动态加载
## 动态切换实例
# Fragment 的传值问题
## Activity --> Fragment传值
### setArgument
### 其他
## Fragment --> Activity传值
### Callback
# 定义
数组适配器，只能用来显示单一的文本。构造方法：
```kotlin
ArrayAdapter(Context context,int resource,int textviewId,List<T>objects)
```
- context：环境上下文
- resource：要放置的view的id
- textviewId：文本需要放在布局中对应id文本控件的位置
- objects：数据源 
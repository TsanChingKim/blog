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
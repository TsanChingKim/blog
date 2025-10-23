# Button 按钮控件

button注册点击时间的方法：
- 自定义内部类
- 匿名内部类
- 当前Activity去实现事件接口
- 在布局文件中添加点击事件属性

## 1.使用自定义内部类实现单机事件

```kotlin
class MainActivity : ComponentActivity() {  
    override fun onCreate(savedInstanceState: Bundle?) {  
        super.onCreate(savedInstanceState)  
        // 设置当前显示的视图的xml文件的文件名  
        setContentView(R.layout.acitivity_main)  
        // 根据控件id获取控件  
        val btn: Button = findViewById(R.id.btn1)  
        // 获取单击事件监听器对象  
        val myOnClickListener = MyOnClickListener()  
        // 设置改控件的单击事件监听器为上述获取的监听器对象  
        btn.setOnClickListener(myOnClickListener)  
    }  
    class MyOnClickListener : View.OnClickListener {  
        override fun onClick(v: View?) {  
            println("11111111111")  
        }  
    }  
}
```

## 2.使用匿名内部类实现单击事件

```kotlin
class MainActivity : ComponentActivity() {  
    override fun onCreate(savedInstanceState: Bundle?) {  
        super.onCreate(savedInstanceState)  
        // 设置当前显示的视图的xml文件的文件名  
        setContentView(R.layout.acitivity_main)  
        // 根据控件id获取控件  
        val btn: Button = findViewById(R.id.btn1)  
        // 设置改控件的单击事件监听器为匿名内部类  
        btn.setOnClickListener(object : OnClickListener {  
		    override fun onClick(v: View?) {  
		        println("这是使用匿名内部类实现的单机事件监听器")  
		    }  
		})  
    }
}
```

## 3.使用本类实现单击事件

```kotlin
class MainActivity : ComponentActivity(), OnClickListener {  
    override fun onCreate(savedInstanceState: Bundle?) {  
        super.onCreate(savedInstanceState)  
        // 设置当前显示的视图的xml文件的文件名  
        setContentView(R.layout.acitivity_main)  
        // 根据控件id获取控件  
        val btn: Button = findViewById(R.id.btn1)  
        // 获取单击事件监听器对象  
        val myOnClickListener = MyOnClickListener()  
        // 设置改控件的单击事件监听器为本类   
        btn.setOnClickListener(this)  
    }
	override fun onClick(v: View?) {  
	    Log.e("TAG","本类实现单击事件")  
	}
}
```

## 4.使用XML绑定函数作为单击事件

```xml
<Button  
    android:id="@+id/btn1"  
    android:layout_width="wrap_content"  
    android:layout_height="wrap_content"  
    android:layout_gravity="center_horizontal"  
    android:gravity="center"  
    android:layout_marginTop="30dp"  
    android:text="Register"  
    android:onClick="myOnClick"  
    />
```

```Kotlin
fun myOnClick(v: View?){  
    Log.e("TAG","这是被onClick属性绑定的单击事件")  
}
```

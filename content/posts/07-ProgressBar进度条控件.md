# ProgressBar 进度条控件

```xml
<ProgressBar  
    android:layout_width="wrap_content"  
    android:layout_height="wrap_content"/>
```

如果只是这三行代码，只会是一个旋转的加载图标

```xml
<ProgressBar  
    android:layout_width="match_parent"  
    android:layout_height="wrap_content"  
    style="?android:attr/progressBarStyleHorizontal"  
    android:progress="30"  
    android:max="100"/>
```

- `style`：设置风格
- `progress`：当前进度
- `max`：总进度

在业务中需要根据它的id获取该控件并修改其进度

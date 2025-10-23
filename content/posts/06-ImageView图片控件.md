# ImageView 图片控件

用来显示和控制图像的空间，可以对它进行放大、缩小、旋转等操作。

项目中有两个文件夹：mipmap 和 drawable
- drawable：高清图片文件夹
- mipmap：普通图片存放
一般都存放至mipmap

```xml
<ImageView  
    android:layout_width="60dp"  
    android:layout_height="60dp"  
    android:layout_gravity="center_horizontal"  
    android:gravity="center"  
    android:src="@mipmap/ic_launcher_round"  
    android:layout_marginTop="30dp"  
    />
```

- `src`：用来指定前景图片资源
	- 前景图片的特点：不管大小如何变化，图片会始终保持其原有的比例
- `background`：使用图片作为背景
	- 背景图片的特点：不管大小如何变化，图片会随着大小变化，不会维持其大小

```xml
<ImageButton
	android:layout_width="60dp"  
    android:layout_height="60dp"
    android:src="@mipmap/ic_launcher_round"/>
```

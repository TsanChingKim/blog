---
title: FrameLayout 帧布局
date: 2025-10-24
categories: ["Android"]
robots: all
summary: 详细介绍Android FrameLayout帧布局的使用方法、层叠效果和实际应用场景
featureimage: images/android/08.jpg
---

# FrameLayout 帧布局

FrameLayout 是 Android 中最简单的布局容器，所有子控件都从左上角开始层叠排列，后添加的控件会覆盖在先添加的控件之上。

## FrameLayout 基本特性

### 层叠排列
FrameLayout 中的所有子控件都从左上角（0,0）开始定位，后添加的控件会覆盖在先添加的控件之上。

### 重要属性

| 属性 | 说明 | 示例值 |
|------|------|--------|
| `android:layout_gravity` | 控制控件在容器中的位置 | `center`, `top`, `bottom` |
| `android:foreground` | 设置前景图片 | `@drawable/foreground_image` |
| `android:foregroundGravity` | 前景图片的重力 | `center`, `top`, `bottom` |

## 基本使用示例

### 层叠效果示例

```xml
<FrameLayout
    android:layout_width="match_parent"
    android:layout_height="300dp"
    android:background="#F5F5F5">
    
    <!-- 底层 - 蓝色 -->
    <TextView
        android:layout_width="350dp"
        android:layout_height="350dp"
        android:layout_gravity="center"
        android:background="#0000FF"
        android:text="底层"
        android:textColor="#FFFFFF"
        android:gravity="center" />
    
    <!-- 第二层 - 紫色 -->
    <TextView
        android:layout_width="330dp"
        android:layout_height="330dp"
        android:layout_gravity="center"
        android:background="#9932CC"
        android:text="第二层"
        android:textColor="#FFFFFF"
        android:gravity="center" />
    
    <!-- 第三层 - 粉色 -->
    <TextView
        android:layout_width="300dp"
        android:layout_height="300dp"
        android:layout_gravity="center"
        android:background="#FF1493"
        android:text="第三层"
        android:textColor="#FFFFFF"
        android:gravity="center" />
    
    <!-- 顶层 - 浅紫色 -->
    <TextView
        android:layout_width="270dp"
        android:layout_height="270dp"
        android:layout_gravity="center"
        android:background="#DA70D6"
        android:text="顶层"
        android:textColor="#FFFFFF"
        android:gravity="center" />
    
</FrameLayout>
```

## Kotlin 代码示例

### 动态创建层叠效果

```kotlin
class FrameLayoutActivity : AppCompatActivity() {
    
    private lateinit var frameLayout: FrameLayout
    private lateinit var addLayerButton: Button
    private lateinit var removeLayerButton: Button
    
    private val colors = listOf(
        "#FF5722", "#2196F3", "#4CAF50", "#FF9800", "#9C27B0", "#00BCD4"
    )
    private var layerCount = 0
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_frame_layout)
        
        initViews()
        setupClickListeners()
    }
    
    private fun initViews() {
        frameLayout = findViewById(R.id.frameLayout)
        addLayerButton = findViewById(R.id.addLayerButton)
        removeLayerButton = findViewById(R.id.removeLayerButton)
    }
    
    private fun setupClickListeners() {
        addLayerButton.setOnClickListener {
            addLayer()
        }
        
        removeLayerButton.setOnClickListener {
            removeLayer()
        }
    }
    
    private fun addLayer() {
        if (layerCount < colors.size) {
            val textView = TextView(this).apply {
                val size = 350 - (layerCount * 20)
                layoutParams = FrameLayout.LayoutParams(
                    dpToPx(size),
                    dpToPx(size)
                ).apply {
                    gravity = Gravity.CENTER
                }
                
                background = ColorDrawable(Color.parseColor(colors[layerCount]))
                text = "第 ${layerCount + 1} 层"
                setTextColor(Color.WHITE)
                gravity = Gravity.CENTER
                textSize = 16f
            }
            
            frameLayout.addView(textView)
            layerCount++
            
            Toast.makeText(this, "添加了第 $layerCount 层", Toast.LENGTH_SHORT).show()
        } else {
            Toast.makeText(this, "已达到最大层数", Toast.LENGTH_SHORT).show()
        }
    }
    
    private fun removeLayer() {
        if (layerCount > 0) {
            frameLayout.removeViewAt(frameLayout.childCount - 1)
            layerCount--
            Toast.makeText(this, "移除了第 ${layerCount + 1} 层", Toast.LENGTH_SHORT).show()
        } else {
            Toast.makeText(this, "没有可移除的层", Toast.LENGTH_SHORT).show()
        }
    }
    
    private fun dpToPx(dp: Int): Int {
        return (dp * resources.displayMetrics.density).toInt()
    }
}
```

### 图片叠加效果

```kotlin
class ImageOverlayActivity : AppCompatActivity() {
    
    private lateinit var frameLayout: FrameLayout
    private lateinit var addOverlayButton: Button
    private lateinit var clearOverlayButton: Button
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_image_overlay)
        
        initViews()
        setupClickListeners()
    }
    
    private fun initViews() {
        frameLayout = findViewById(R.id.frameLayout)
        addOverlayButton = findViewById(R.id.addOverlayButton)
        clearOverlayButton = findViewById(R.id.clearOverlayButton)
    }
    
    private fun setupClickListeners() {
        addOverlayButton.setOnClickListener {
            addImageOverlay()
        }
        
        clearOverlayButton.setOnClickListener {
            clearOverlays()
        }
    }
    
    private fun addImageOverlay() {
        val overlayImage = ImageView(this).apply {
            layoutParams = FrameLayout.LayoutParams(
                FrameLayout.LayoutParams.MATCH_PARENT,
                FrameLayout.LayoutParams.MATCH_PARENT
            )
            
            // 设置半透明遮罩
            setBackgroundColor(Color.parseColor("#80000000"))
            
            // 添加点击事件
            setOnClickListener {
                Toast.makeText(this@ImageOverlayActivity, "点击了遮罩层", Toast.LENGTH_SHORT).show()
            }
        }
        
        frameLayout.addView(overlayImage)
    }
    
    private fun clearOverlays() {
        // 移除所有遮罩层（保留背景图片）
        val childCount = frameLayout.childCount
        for (i in childCount - 1 downTo 1) {
            frameLayout.removeViewAt(i)
        }
    }
}
```

## 实际应用场景

### 1. 图片叠加效果

```xml
<FrameLayout
    android:layout_width="match_parent"
    android:layout_height="200dp">
    
    <!-- 背景图片 -->
    <ImageView
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:src="@drawable/background_image"
        android:scaleType="centerCrop" />
    
    <!-- 半透明遮罩 -->
    <View
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:background="#80000000" />
    
    <!-- 文字内容 -->
    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_gravity="center"
        android:text="叠加文字"
        android:textColor="#FFFFFF"
        android:textSize="18sp"
        android:textStyle="bold" />
    
</FrameLayout>
```

### 2. 浮动按钮

```xml
<FrameLayout
    android:layout_width="match_parent"
    android:layout_height="match_parent">
    
    <!-- 主内容 -->
    <ScrollView
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:padding="16dp">
        
        <TextView
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:text="这里是主要内容..."
            android:textSize="16sp"
            android:lineSpacingMultiplier="1.5" />
        
    </ScrollView>
    
    <!-- 浮动按钮 -->
    <com.google.android.material.floatingactionbutton.FloatingActionButton
        android:id="@+id/fab"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_gravity="bottom|end"
        android:layout_margin="16dp"
        android:src="@drawable/ic_add"
        app:backgroundTint="@color/primary"
        app:tint="@color/white" />
    
</FrameLayout>
```

### 3. 加载遮罩

```kotlin
class LoadingOverlayActivity : AppCompatActivity() {
    
    private lateinit var frameLayout: FrameLayout
    private lateinit var loadButton: Button
    private lateinit var loadingView: View
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_loading_overlay)
        
        initViews()
        setupClickListeners()
    }
    
    private fun initViews() {
        frameLayout = findViewById(R.id.frameLayout)
        loadButton = findViewById(R.id.loadButton)
        
        // 创建加载遮罩
        loadingView = createLoadingOverlay()
    }
    
    private fun setupClickListeners() {
        loadButton.setOnClickListener {
            showLoading()
        }
    }
    
    private fun createLoadingOverlay(): View {
        return LinearLayout(this).apply {
            layoutParams = FrameLayout.LayoutParams(
                FrameLayout.LayoutParams.MATCH_PARENT,
                FrameLayout.LayoutParams.MATCH_PARENT
            )
            
            orientation = LinearLayout.VERTICAL
            gravity = Gravity.CENTER
            setBackgroundColor(Color.parseColor("#80000000"))
            
            // 添加进度条
            val progressBar = ProgressBar(this@LoadingOverlayActivity).apply {
                layoutParams = LinearLayout.LayoutParams(
                    LinearLayout.LayoutParams.WRAP_CONTENT,
                    LinearLayout.LayoutParams.WRAP_CONTENT
                )
            }
            addView(progressBar)
            
            // 添加文字
            val textView = TextView(this@LoadingOverlayActivity).apply {
                layoutParams = LinearLayout.LayoutParams(
                    LinearLayout.LayoutParams.WRAP_CONTENT,
                    LinearLayout.LayoutParams.WRAP_CONTENT
                ).apply {
                    topMargin = dpToPx(16)
                }
                
                text = "正在加载..."
                setTextColor(Color.WHITE)
                textSize = 16f
            }
            addView(textView)
            
            // 初始状态隐藏
            visibility = View.GONE
        }
    }
    
    private fun showLoading() {
        frameLayout.addView(loadingView)
        loadingView.visibility = View.VISIBLE
        
        // 模拟加载过程
        Handler(Looper.getMainLooper()).postDelayed({
            hideLoading()
        }, 3000)
    }
    
    private fun hideLoading() {
        loadingView.visibility = View.GONE
        frameLayout.removeView(loadingView)
        Toast.makeText(this, "加载完成", Toast.LENGTH_SHORT).show()
    }
    
    private fun dpToPx(dp: Int): Int {
        return (dp * resources.displayMetrics.density).toInt()
    }
}
```

### 4. 卡片叠加效果

```xml
<FrameLayout
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:padding="16dp">
    
    <!-- 卡片背景 -->
    <View
        android:layout_width="match_parent"
        android:layout_height="200dp"
        android:layout_marginTop="8dp"
        android:background="@drawable/card_background"
        android:elevation="2dp" />
    
    <!-- 卡片内容 -->
    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="200dp"
        android:orientation="vertical"
        android:padding="16dp"
        android:gravity="center">
        
        <ImageView
            android:layout_width="60dp"
            android:layout_height="60dp"
            android:src="@drawable/ic_card"
            android:layout_marginBottom="8dp" />
        
        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="卡片标题"
            android:textSize="18sp"
            android:textStyle="bold"
            android:layout_marginBottom="4dp" />
        
        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="卡片描述内容"
            android:textSize="14sp"
            android:textColor="#666666" />
        
    </LinearLayout>
    
</FrameLayout>
```

## 性能优化建议

### 1. 避免过度层叠

```kotlin
// 不好的做法：过多层叠
FrameLayout {
    ImageView { } // 第1层
    View { }      // 第2层
    TextView { }  // 第3层
    Button { }    // 第4层
    ImageView { } // 第5层
    // ... 更多层
}

// 好的做法：合理使用层叠
FrameLayout {
    ImageView { } // 背景
    LinearLayout { // 内容容器
        TextView { }
        Button { }
    }
}
```

### 2. 使用 ViewStub 延迟加载

```xml
<FrameLayout
    android:layout_width="match_parent"
    android:layout_height="match_parent">
    
    <!-- 主要内容 -->
    <TextView android:text="主要内容" />
    
    <!-- 延迟加载的内容 -->
    <ViewStub
        android:id="@+id/viewStub"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout="@layout/delayed_content" />
    
</FrameLayout>
```

### 3. 合理使用前景

```kotlin
class OptimizedFrameLayout {
    
    fun setupForeground(frameLayout: FrameLayout) {
        // 使用前景而不是额外的View
        frameLayout.foreground = ContextCompat.getDrawable(
            frameLayout.context, R.drawable.foreground_overlay
        )
        frameLayout.foregroundGravity = Gravity.CENTER
    }
}
```

## 常见问题解决

### 1. 子控件重叠

```xml
<!-- 错误：没有设置layout_gravity -->
<FrameLayout>
    <TextView android:text="文本1" />
    <TextView android:text="文本2" />
</FrameLayout>

<!-- 正确：设置不同的位置 -->
<FrameLayout>
    <TextView 
        android:layout_gravity="top|start"
        android:text="文本1" />
    <TextView 
        android:layout_gravity="bottom|end"
        android:text="文本2" />
</FrameLayout>
```

### 2. 触摸事件穿透

```kotlin
class TouchEventActivity : AppCompatActivity() {
    
    private lateinit var frameLayout: FrameLayout
    private lateinit var overlayView: View
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_touch_event)
        
        initViews()
        setupTouchEvents()
    }
    
    private fun initViews() {
        frameLayout = findViewById(R.id.frameLayout)
        overlayView = findViewById(R.id.overlayView)
    }
    
    private fun setupTouchEvents() {
        // 设置遮罩层不拦截触摸事件
        overlayView.setOnTouchListener { _, _ ->
            // 返回false，让触摸事件穿透到下层
            false
        }
    }
}
```

## 📋 总结

FrameLayout 是 Android 开发中简单而强大的布局容器：

- **层叠特性**：所有子控件从左上角开始层叠排列
- **灵活定位**：通过 layout_gravity 控制子控件位置
- **实际应用**：图片叠加、浮动按钮、加载遮罩等场景
- **性能考虑**：避免过度层叠，合理使用前景
- **触摸处理**：注意触摸事件的传递和拦截

掌握 FrameLayout 的使用方法对于创建复杂的层叠效果和特殊布局至关重要。

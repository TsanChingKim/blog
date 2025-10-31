---
title: LinearLayout 线性布局
date: 2025-10-24
categories: ["Android"]
robots: all
summary: 详细介绍Android LinearLayout线性布局的使用方法、属性配置和实际应用场景
featureimage: images/android/02.jpg
---

# LinearLayout 线性布局

LinearLayout 是 Android 中最常用的布局容器，它按照水平或垂直方向依次排列子控件。

## LinearLayout 基本属性

```xml
<LinearLayout
    android:id="@+id/linearLayout"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:gravity="center"
    android:padding="16dp"
    android:background="@color/background_color">
    
    <!-- 子控件 -->
    
</LinearLayout>
```

## 核心属性详解

### 1. orientation（方向）

控制子控件的排列方向：

```xml
<!-- 垂直排列（默认） -->
<LinearLayout
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical">
    
    <TextView android:text="第一行" />
    <TextView android:text="第二行" />
    <TextView android:text="第三行" />
    
</LinearLayout>

<!-- 水平排列 -->
<LinearLayout
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:orientation="horizontal">
    
    <TextView android:text="第一列" />
    <TextView android:text="第二列" />
    <TextView android:text="第三列" />
    
</LinearLayout>
```

### 2. layout_weight（权重）

按比例分配剩余空间：

```xml
<LinearLayout
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:orientation="horizontal">
    
    <!-- 占1/3空间 -->
    <TextView
        android:layout_width="0dp"
        android:layout_height="wrap_content"
        android:layout_weight="1"
        android:text="三分之一"
        android:background="#FF5722" />
    
    <!-- 占2/3空间 -->
    <TextView
        android:layout_width="0dp"
        android:layout_height="wrap_content"
        android:layout_weight="2"
        android:text="三分之二"
        android:background="#2196F3" />
    
</LinearLayout>
```

### 3. gravity（对齐方式）

控制子控件在容器中的对齐方式：

```xml
<LinearLayout
    android:layout_width="match_parent"
    android:layout_height="200dp"
    android:orientation="vertical"
    android:gravity="center">
    
    <TextView android:text="居中对齐" />
    
</LinearLayout>
```

## Kotlin 代码示例

### 动态创建 LinearLayout

```kotlin
class DynamicLinearLayoutActivity : AppCompatActivity() {
    
    private lateinit var containerLayout: LinearLayout
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_dynamic_linear_layout)
        
        initViews()
        createDynamicLayout()
    }
    
    private fun initViews() {
        containerLayout = findViewById(R.id.containerLayout)
    }
    
    private fun createDynamicLayout() {
        // 创建水平布局
        val horizontalLayout = LinearLayout(this).apply {
            orientation = LinearLayout.HORIZONTAL
            layoutParams = LinearLayout.LayoutParams(
                LinearLayout.LayoutParams.MATCH_PARENT,
                LinearLayout.LayoutParams.WRAP_CONTENT
            )
            gravity = Gravity.CENTER
            setPadding(16, 16, 16, 16)
        }
        
        // 添加按钮
        repeat(3) { index ->
            val button = Button(this).apply {
                text = "按钮 ${index + 1}"
                layoutParams = LinearLayout.LayoutParams(
                    LinearLayout.LayoutParams.WRAP_CONTENT,
                    LinearLayout.LayoutParams.WRAP_CONTENT
                ).apply {
                    marginEnd = if (index < 2) 16 else 0
                }
                setOnClickListener {
                    Toast.makeText(this@DynamicLinearLayoutActivity, 
                        "按钮 ${index + 1} 被点击", Toast.LENGTH_SHORT).show()
                }
            }
            horizontalLayout.addView(button)
        }
        
        containerLayout.addView(horizontalLayout)
    }
}
```

### 权重分配示例

```kotlin
class WeightDistributionActivity : AppCompatActivity() {
    
    private lateinit var containerLayout: LinearLayout
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_weight_distribution)
        
        initViews()
        setupWeightDistribution()
    }
    
    private fun initViews() {
        containerLayout = findViewById(R.id.containerLayout)
    }
    
    private fun setupWeightDistribution() {
        val weights = listOf(1, 2, 3) // 权重比例 1:2:3
        
        weights.forEachIndexed { index, weight ->
            val textView = TextView(this).apply {
                text = "权重: $weight"
                gravity = Gravity.CENTER
                setTextColor(Color.WHITE)
                setPadding(16, 16, 16, 16)
                
                layoutParams = LinearLayout.LayoutParams(
                    0, // 宽度设为0，让权重生效
                    LinearLayout.LayoutParams.MATCH_PARENT
                ).apply {
                    this.weight = weight.toFloat()
                }
                
                // 设置不同颜色
                setBackgroundColor(
                    when (index) {
                        0 -> Color.parseColor("#FF5722")
                        1 -> Color.parseColor("#2196F3")
                        2 -> Color.parseColor("#4CAF50")
                        else -> Color.GRAY
                    }
                )
            }
            
            containerLayout.addView(textView)
        }
    }
}
```

## 实际应用场景

### 1. 登录表单布局

```xml
<LinearLayout
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:gravity="center"
    android:padding="24dp">
    
    <!-- Logo -->
    <ImageView
        android:layout_width="120dp"
        android:layout_height="120dp"
        android:src="@drawable/logo"
        android:layout_marginBottom="32dp" />
    
    <!-- 用户名输入框 -->
    <EditText
        android:id="@+id/usernameEditText"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="请输入用户名"
        android:layout_marginBottom="16dp"
        android:padding="16dp"
        android:background="@drawable/edit_text_background" />
    
    <!-- 密码输入框 -->
    <EditText
        android:id="@+id/passwordEditText"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="请输入密码"
        android:inputType="textPassword"
        android:layout_marginBottom="24dp"
        android:padding="16dp"
        android:background="@drawable/edit_text_background" />
    
    <!-- 登录按钮 -->
    <Button
        android:id="@+id/loginButton"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="登录"
        android:textSize="16sp"
        android:padding="16dp"
        android:background="@drawable/button_background" />
    
</LinearLayout>
```

### 2. 底部导航栏

```xml
<LinearLayout
    android:layout_width="match_parent"
    android:layout_height="60dp"
    android:orientation="horizontal"
    android:background="@color/bottom_nav_background"
    android:gravity="center">
    
    <!-- 首页 -->
    <LinearLayout
        android:layout_width="0dp"
        android:layout_height="match_parent"
        android:layout_weight="1"
        android:orientation="vertical"
        android:gravity="center"
        android:clickable="true"
        android:background="?android:attr/selectableItemBackground">
        
        <ImageView
            android:layout_width="24dp"
            android:layout_height="24dp"
            android:src="@drawable/ic_home" />
        
        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="首页"
            android:textSize="12sp"
            android:layout_marginTop="4dp" />
        
    </LinearLayout>
    
    <!-- 其他导航项... -->
    
</LinearLayout>
```

### 3. 商品列表项

```xml
<LinearLayout
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:orientation="horizontal"
    android:padding="16dp"
    android:background="?android:attr/selectableItemBackground"
    android:clickable="true">
    
    <!-- 商品图片 -->
    <ImageView
        android:layout_width="80dp"
        android:layout_height="80dp"
        android:src="@drawable/product_image"
        android:scaleType="centerCrop"
        android:layout_marginEnd="16dp" />
    
    <!-- 商品信息 -->
    <LinearLayout
        android:layout_width="0dp"
        android:layout_height="wrap_content"
        android:layout_weight="1"
        android:orientation="vertical"
        android:gravity="center_vertical">
        
        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="商品名称"
            android:textSize="16sp"
            android:textStyle="bold"
            android:layout_marginBottom="4dp" />
        
        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="商品描述"
            android:textSize="14sp"
            android:textColor="#666666"
            android:layout_marginBottom="8dp" />
        
        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="¥99.00"
            android:textSize="18sp"
            android:textColor="#FF5722"
            android:textStyle="bold" />
        
    </LinearLayout>
    
    <!-- 操作按钮 -->
    <Button
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="加入购物车"
        android:layout_gravity="center_vertical" />
    
</LinearLayout>
```

## 嵌套布局示例

### 复杂表单布局

```xml
<ScrollView
    android:layout_width="match_parent"
    android:layout_height="match_parent">
    
    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="vertical"
        android:padding="16dp">
        
        <!-- 个人信息部分 -->
        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="个人信息"
            android:textSize="18sp"
            android:textStyle="bold"
            android:layout_marginBottom="16dp" />
        
        <LinearLayout
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:orientation="horizontal"
            android:layout_marginBottom="16dp">
            
            <EditText
                android:layout_width="0dp"
                android:layout_height="wrap_content"
                android:layout_weight="1"
                android:hint="姓名"
                android:layout_marginEnd="8dp" />
            
            <EditText
                android:layout_width="0dp"
                android:layout_height="wrap_content"
                android:layout_weight="1"
                android:hint="年龄"
                android:inputType="number" />
            
        </LinearLayout>
        
        <!-- 联系方式部分 -->
        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="联系方式"
            android:textSize="18sp"
            android:textStyle="bold"
            android:layout_marginBottom="16dp" />
        
        <EditText
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:hint="手机号码"
            android:inputType="phone"
            android:layout_marginBottom="16dp" />
        
        <EditText
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:hint="邮箱地址"
            android:inputType="textEmailAddress"
            android:layout_marginBottom="24dp" />
        
        <!-- 提交按钮 -->
        <Button
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:text="提交"
            android:textSize="16sp"
            android:padding="16dp" />
        
    </LinearLayout>
    
</ScrollView>
```

## 性能优化建议

### 1. 避免过度嵌套

```kotlin
// 不好的做法：过度嵌套
LinearLayout {
    LinearLayout {
        LinearLayout {
            TextView { }
        }
    }
}

// 好的做法：使用ConstraintLayout替代
ConstraintLayout {
    TextView { }
}
```

### 2. 使用 ViewStub 延迟加载

```xml
<LinearLayout
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical">
    
    <!-- 主要内容 -->
    <TextView android:text="主要内容" />
    
    <!-- 延迟加载的内容 -->
    <ViewStub
        android:id="@+id/viewStub"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout="@layout/delayed_content" />
    
</LinearLayout>
```

### 3. 合理使用权重

```kotlin
// 避免不必要的权重计算
class OptimizedLinearLayout {
    
    fun setupOptimizedLayout() {
        // 使用固定尺寸而不是权重
        val layoutParams = LinearLayout.LayoutParams(
            resources.getDimensionPixelSize(R.dimen.button_width),
            LinearLayout.LayoutParams.WRAP_CONTENT
        )
        
        // 只在必要时使用权重
        val weightParams = LinearLayout.LayoutParams(
            0,
            LinearLayout.LayoutParams.MATCH_PARENT
        ).apply {
            weight = 1f // 只在需要按比例分配时使用
        }
    }
}
```

## 常见问题解决

### 1. 权重不生效

```xml
<!-- 错误：设置了具体宽度 -->
<TextView
    android:layout_width="100dp"
    android:layout_height="wrap_content"
    android:layout_weight="1" />

<!-- 正确：宽度设为0dp -->
<TextView
    android:layout_width="0dp"
    android:layout_height="wrap_content"
    android:layout_weight="1" />
```

### 2. 子控件超出容器

```xml
<LinearLayout
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:orientation="horizontal">
    
    <!-- 使用权重避免超出 -->
    <TextView
        android:layout_width="0dp"
        android:layout_height="wrap_content"
        android:layout_weight="1"
        android:text="很长的文本内容..." />
    
</LinearLayout>
```

## 📋 总结

LinearLayout 是 Android 开发中最基础的布局容器：

- **简单易用**：按方向排列子控件，逻辑清晰
- **权重分配**：灵活控制空间分配比例
- **嵌套布局**：支持复杂的布局结构
- **性能考虑**：避免过度嵌套，合理使用权重
- **实际应用**：表单、列表、导航等常见场景

掌握 LinearLayout 的使用方法是 Android 布局开发的基础。

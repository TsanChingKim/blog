---
title: UI基础控件 View
date: 2025-10-24
categories: ["Android"]
robots: all
summary: 详细介绍Android UI基础控件View的分类、TextView和EditText的使用方法及属性配置
featureimage: images/android/04.jpg
---

# UI 基础控件 View

View 是 Android UI 的基础组件，所有的 UI 控件都继承自 View 类。View 提供了基本的绘制和事件处理功能。

## View 分类

### 文本显示类
- **TextView**：显示文本内容
- **Button**：可点击的按钮
- **EditText**：文本输入框

### 图片显示类
- **ImageView**：显示图片
- **ImageButton**：图片按钮

### 进度显示类
- **ProgressBar**：进度条
- **SeekBar**：可拖拽的进度条

### 选择类
- **CheckBox**：复选框
- **RadioButton**：单选按钮
- **Switch**：开关

## 📚 TextView 文本显示控件

TextView 是 Android 中最基础的文本显示控件，类似于 Swing 中的 JLabel。

### 基本属性

```xml
<TextView
    android:id="@+id/textView"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:text="Hello World!"
    android:textSize="16sp"
    android:textColor="#333333"
    android:gravity="center"
    android:padding="16dp" />
```

### 常用属性说明

| 属性 | 说明 | 示例值 |
|------|------|--------|
| `textSize` | 设置字体大小 | `16sp`, `20dp` |
| `textColor` | 设置文字颜色 | `#333333`, `@color/primary` |
| `gravity` | 设置文字对齐方式 | `center`, `left`, `right` |
| `lineSpacingMultiplier` | 设置行间距倍数 | `1.2` |
| `maxLines` | 设置最大行数 | `3` |
| `ellipsize` | 设置省略号位置 | `end`, `start`, `middle` |

### 长文本处理

#### 滚动显示
当文本内容超过屏幕高度时，使用 ScrollView 包装：

```xml
<ScrollView
    android:layout_width="match_parent"
    android:layout_height="match_parent">
    
    <TextView
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="@string/long_text"
        android:textSize="14sp"
        android:lineSpacingMultiplier="1.2" />
        
</ScrollView>
```

#### 跑马灯效果
实现文字滚动显示：

```xml
<TextView
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:text="这是一段很长的文字，会以跑马灯的形式滚动显示"
    android:singleLine="true"
    android:ellipsize="marquee"
    android:marqueeRepeatLimit="marquee_forever"
    android:focusable="true"
    android:focusableInTouchMode="true" />
```

### Kotlin 代码示例

```kotlin
class MainActivity : AppCompatActivity() {
    
    private lateinit var textView: TextView
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        
        initViews()
        setupTextView()
    }
    
    private fun initViews() {
        textView = findViewById(R.id.textView)
    }
    
    private fun setupTextView() {
        // 设置文本内容
        textView.text = "Hello Kotlin!"
        
        // 设置文字颜色
        textView.setTextColor(ContextCompat.getColor(this, R.color.primary))
        
        // 设置文字大小
        textView.textSize = 18f
        
        // 设置点击事件
        textView.setOnClickListener {
            Toast.makeText(this, "TextView被点击了", Toast.LENGTH_SHORT).show()
        }
        
        // 动态设置跑马灯效果
        textView.isSelected = true
    }
}
```

## 📝 EditText 文本输入控件

EditText 继承自 TextView，用于接收用户输入的文本。

### 基本属性

```xml
<EditText
    android:id="@+id/editText"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:hint="请输入用户名"
    android:inputType="text"
    android:maxLength="20"
    android:background="@drawable/edit_text_background"
    android:padding="12dp" />
```

### 输入类型 (inputType)

| 类型 | 说明 | 键盘类型 |
|------|------|----------|
| `text` | 普通文本 | 标准键盘 |
| `textPassword` | 密码输入 | 数字键盘 |
| `number` | 正整数 | 数字键盘 |
| `numberSigned` | 整数（含负数） | 数字键盘 |
| `numberDecimal` | 小数 | 数字键盘 |
| `phone` | 电话号码 | 电话键盘 |
| `email` | 邮箱地址 | 邮箱键盘 |
| `textMultiLine` | 多行文本 | 标准键盘 |

### 常用属性

| 属性 | 说明 | 示例值 |
|------|------|--------|
| `hint` | 提示文字 | `"请输入用户名"` |
| `maxLength` | 最大输入长度 | `20` |
| `minLines` | 最小行数 | `3` |
| `maxLines` | 最大行数 | `5` |
| `lines` | 固定行数 | `3` |

### Kotlin 代码示例

```kotlin
class MainActivity : AppCompatActivity() {
    
    private lateinit var editText: EditText
    private lateinit var button: Button
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        
        initViews()
        setupEditText()
    }
    
    private fun initViews() {
        editText = findViewById(R.id.editText)
        button = findViewById(R.id.button)
    }
    
    private fun setupEditText() {
        // 设置输入监听
        editText.addTextChangedListener(object : TextWatcher {
            override fun beforeTextChanged(s: CharSequence?, start: Int, count: Int, after: Int) {
                // 文本改变前的回调
            }
            
            override fun onTextChanged(s: CharSequence?, start: Int, before: Int, count: Int) {
                // 文本改变时的回调
                val inputText = s.toString()
                button.isEnabled = inputText.isNotEmpty()
            }
            
            override fun afterTextChanged(s: Editable?) {
                // 文本改变后的回调
            }
        })
        
        // 设置焦点变化监听
        editText.onFocusChangeListener = View.OnFocusChangeListener { _, hasFocus ->
            if (hasFocus) {
                // 获得焦点时的处理
                editText.setBackgroundResource(R.drawable.edit_text_focused)
            } else {
                // 失去焦点时的处理
                editText.setBackgroundResource(R.drawable.edit_text_normal)
            }
        }
        
        // 获取输入内容
        button.setOnClickListener {
            val inputText = editText.text.toString()
            if (inputText.isNotEmpty()) {
                Toast.makeText(this, "输入内容：$inputText", Toast.LENGTH_SHORT).show()
            } else {
                Toast.makeText(this, "请输入内容", Toast.LENGTH_SHORT).show()
            }
        }
    }
    
    // 验证输入内容
    private fun validateInput(): Boolean {
        val inputText = editText.text.toString()
        return inputText.length >= 3 && inputText.length <= 20
    }
}
```

## 🎨 样式和主题

### 自定义样式

在 `res/values/styles.xml` 中定义：

```xml
<style name="CustomTextViewStyle">
    <item name="android:textSize">16sp</item>
    <item name="android:textColor">#333333</item>
    <item name="android:background">@drawable/text_view_background</item>
    <item name="android:padding">12dp</item>
</style>
```

### 应用样式

```xml
<TextView
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    style="@style/CustomTextViewStyle"
    android:text="应用自定义样式" />
```

## 📱 响应式设计

### 不同屏幕尺寸适配

```xml
<!-- 小屏幕 -->
<TextView
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:textSize="14sp"
    android:minWidth="120dp" />

<!-- 大屏幕 -->
<TextView
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:textSize="18sp"
    android:minWidth="200dp" />
```

## 🔧 实用技巧

### 1. 动态设置文本
```kotlin
// 使用字符串资源
textView.text = getString(R.string.welcome_message, userName)

// 使用格式化字符串
textView.text = String.format("欢迎 %s，今天是 %s", userName, currentDate)
```

### 2. 文本选择
```kotlin
// 设置文本可选择
textView.setTextIsSelectable(true)

// 选中指定范围的文本
textView.setSelection(0, 5)
```

### 3. 链接处理
```kotlin
// 设置HTML内容
textView.text = Html.fromHtml("<a href='https://www.example.com'>点击访问</a>")
textView.movementMethod = LinkMovementMethod.getInstance()
```

## 📋 总结

TextView 和 EditText 是 Android 开发中最常用的基础控件：

- **TextView**：用于显示文本内容，支持多种样式和效果
- **EditText**：用于接收用户输入，支持多种输入类型和验证
- **样式定制**：通过样式和主题实现统一的视觉效果
- **响应式设计**：适配不同屏幕尺寸和密度

掌握这些基础控件的使用方法是 Android 开发的重要基础。

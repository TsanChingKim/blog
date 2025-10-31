---
title: PopupWindow 弹窗
date: 2025-10-24
categories: ["Android"]
robots: all
summary: 详细介绍Android PopupWindow弹窗的使用方法、动画效果和实际应用场景
featureimage: images/android/14.jpg
---

# PopupWindow 弹窗

PopupWindow 是 Android 中用于显示浮动窗口的组件，可以在指定位置弹出自定义的视图内容。

## PopupWindow 基本概念

PopupWindow 是一个可以在当前 Activity 之上显示的浮动窗口，常用于显示菜单、提示信息或自定义内容。

### 基本属性

| 属性 | 说明 | 示例值 |
|------|------|--------|
| `width` | 弹窗宽度 | `ViewGroup.LayoutParams.WRAP_CONTENT` |
| `height` | 弹窗高度 | `ViewGroup.LayoutParams.WRAP_CONTENT` |
| `focusable` | 是否可获得焦点 | `true`, `false` |
| `outsideTouchable` | 外部点击是否关闭 | `true`, `false` |
| `animationStyle` | 动画样式 | `R.style.PopupAnimation` |

## 基本使用示例

### 1. 简单弹窗

```kotlin
class PopupWindowActivity : AppCompatActivity() {
    
    private lateinit var showPopupButton: Button
    private lateinit var popupWindow: PopupWindow
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_popup_window)
        
        initViews()
        setupPopupWindow()
        setupClickListeners()
    }
    
    private fun initViews() {
        showPopupButton = findViewById(R.id.showPopupButton)
    }
    
    private fun setupPopupWindow() {
        // 创建弹窗内容视图
        val popupView = layoutInflater.inflate(R.layout.popup_content, null)
        
        // 创建 PopupWindow
        popupWindow = PopupWindow(
            popupView,
            ViewGroup.LayoutParams.WRAP_CONTENT,
            ViewGroup.LayoutParams.WRAP_CONTENT,
            true
        )
        
        // 设置弹窗属性
        popupWindow.isOutsideTouchable = true
        popupWindow.isTouchable = true
        
        // 设置弹窗内容点击事件
        setupPopupContent(popupView)
    }
    
    private fun setupPopupContent(popupView: View) {
        val item1 = popupView.findViewById<TextView>(R.id.item1)
        val item2 = popupView.findViewById<TextView>(R.id.item2)
        val item3 = popupView.findViewById<TextView>(R.id.item3)
        
        item1.setOnClickListener {
            Toast.makeText(this, "点击了选项1", Toast.LENGTH_SHORT).show()
            popupWindow.dismiss()
        }
        
        item2.setOnClickListener {
            Toast.makeText(this, "点击了选项2", Toast.LENGTH_SHORT).show()
            popupWindow.dismiss()
        }
        
        item3.setOnClickListener {
            Toast.makeText(this, "点击了选项3", Toast.LENGTH_SHORT).show()
            popupWindow.dismiss()
        }
    }
    
    private fun setupClickListeners() {
        showPopupButton.setOnClickListener {
            showPopupWindow(it)
        }
    }
    
    private fun showPopupWindow(anchorView: View) {
        popupWindow.showAsDropDown(anchorView)
    }
}
```

### 2. 自定义位置弹窗

```kotlin
class CustomPositionPopupActivity : AppCompatActivity() {
    
    private lateinit var showPopupButton: Button
    private lateinit var popupWindow: PopupWindow
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_custom_position_popup)
        
        initViews()
        setupPopupWindow()
        setupClickListeners()
    }
    
    private fun initViews() {
        showPopupButton = findViewById(R.id.showPopupButton)
    }
    
    private fun setupPopupWindow() {
        val popupView = layoutInflater.inflate(R.layout.popup_custom_content, null)
        
        popupWindow = PopupWindow(
            popupView,
            ViewGroup.LayoutParams.WRAP_CONTENT,
            ViewGroup.LayoutParams.WRAP_CONTENT,
            true
        )
        
        popupWindow.isOutsideTouchable = true
        popupWindow.isTouchable = true
        
        setupPopupContent(popupView)
    }
    
    private fun setupPopupContent(popupView: View) {
        val editText = popupView.findViewById<EditText>(R.id.editText)
        val confirmButton = popupView.findViewById<Button>(R.id.confirmButton)
        val cancelButton = popupView.findViewById<Button>(R.id.cancelButton)
        
        confirmButton.setOnClickListener {
            val inputText = editText.text.toString()
            if (inputText.isNotEmpty()) {
                Toast.makeText(this, "输入内容: $inputText", Toast.LENGTH_SHORT).show()
                popupWindow.dismiss()
            } else {
                Toast.makeText(this, "请输入内容", Toast.LENGTH_SHORT).show()
            }
        }
        
        cancelButton.setOnClickListener {
            popupWindow.dismiss()
        }
    }
    
    private fun setupClickListeners() {
        showPopupButton.setOnClickListener {
            showPopupAtCustomPosition(it)
        }
    }
    
    private fun showPopupAtCustomPosition(anchorView: View) {
        // 获取锚点视图的位置
        val location = IntArray(2)
        anchorView.getLocationOnScreen(location)
        
        // 计算弹窗位置（在锚点视图上方）
        val x = location[0]
        val y = location[1] - dpToPx(200) // 向上偏移200dp
        
        popupWindow.showAtLocation(anchorView, Gravity.NO_GRAVITY, x, y)
    }
    
    private fun dpToPx(dp: Int): Int {
        return (dp * resources.displayMetrics.density).toInt()
    }
}
```

### 3. 带动画的弹窗

```kotlin
class AnimatedPopupActivity : AppCompatActivity() {
    
    private lateinit var showAnimatedPopupButton: Button
    private lateinit var popupWindow: PopupWindow
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_animated_popup)
        
        initViews()
        setupAnimatedPopupWindow()
        setupClickListeners()
    }
    
    private fun initViews() {
        showAnimatedPopupButton = findViewById(R.id.showAnimatedPopupButton)
    }
    
    private fun setupAnimatedPopupWindow() {
        val popupView = layoutInflater.inflate(R.layout.popup_animated_content, null)
        
        popupWindow = PopupWindow(
            popupView,
            ViewGroup.LayoutParams.WRAP_CONTENT,
            ViewGroup.LayoutParams.WRAP_CONTENT,
            true
        )
        
        popupWindow.isOutsideTouchable = true
        popupWindow.isTouchable = true
        
        // 设置动画样式
        popupWindow.animationStyle = R.style.PopupAnimation
        
        setupPopupContent(popupView)
    }
    
    private fun setupPopupContent(popupView: View) {
        val titleText = popupView.findViewById<TextView>(R.id.titleText)
        val contentText = popupView.findViewById<TextView>(R.id.contentText)
        val closeButton = popupView.findViewById<Button>(R.id.closeButton)
        
        titleText.text = "动画弹窗"
        contentText.text = "这是一个带有动画效果的弹窗"
        
        closeButton.setOnClickListener {
            popupWindow.dismiss()
        }
    }
    
    private fun setupClickListeners() {
        showAnimatedPopupButton.setOnClickListener {
            showAnimatedPopup(it)
        }
    }
    
    private fun showAnimatedPopup(anchorView: View) {
        popupWindow.showAsDropDown(anchorView, 0, -dpToPx(10))
    }
    
    private fun dpToPx(dp: Int): Int {
        return (dp * resources.displayMetrics.density).toInt()
    }
}
```

## 弹窗动画

### 1. 创建动画资源

```xml
<!-- res/anim/popup_enter.xml -->
<set xmlns:android="http://schemas.android.com/apk/res/android">
    <alpha
        android:duration="300"
        android:fromAlpha="0.0"
        android:toAlpha="1.0" />
    <scale
        android:duration="300"
        android:fromXScale="0.5"
        android:fromYScale="0.5"
        android:pivotX="50%"
        android:pivotY="50%"
        android:toXScale="1.0"
        android:toYScale="1.0" />
</set>

<!-- res/anim/popup_exit.xml -->
<set xmlns:android="http://schemas.android.com/apk/res/android">
    <alpha
        android:duration="200"
        android:fromAlpha="1.0"
        android:toAlpha="0.0" />
    <scale
        android:duration="200"
        android:fromXScale="1.0"
        android:fromYScale="1.0"
        android:pivotX="50%"
        android:pivotY="50%"
        android:toXScale="0.5"
        android:toYScale="0.5" />
</set>
```

### 2. 创建动画样式

```xml
<!-- res/values/styles.xml -->
<style name="PopupAnimation">
    <item name="android:windowEnterAnimation">@anim/popup_enter</item>
    <item name="android:windowExitAnimation">@anim/popup_exit</item>
</style>
```

### 3. 使用动画弹窗

```kotlin
class AnimationPopupActivity : AppCompatActivity() {
    
    private lateinit var showAnimationPopupButton: Button
    private lateinit var popupWindow: PopupWindow
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_animation_popup)
        
        initViews()
        setupAnimationPopupWindow()
        setupClickListeners()
    }
    
    private fun initViews() {
        showAnimationPopupButton = findViewById(R.id.showAnimationPopupButton)
    }
    
    private fun setupAnimationPopupWindow() {
        val popupView = layoutInflater.inflate(R.layout.popup_animation_content, null)
        
        popupWindow = PopupWindow(
            popupView,
            ViewGroup.LayoutParams.WRAP_CONTENT,
            ViewGroup.LayoutParams.WRAP_CONTENT,
            true
        )
        
        popupWindow.isOutsideTouchable = true
        popupWindow.isTouchable = true
        popupWindow.animationStyle = R.style.PopupAnimation
        
        setupPopupContent(popupView)
    }
    
    private fun setupPopupContent(popupView: View) {
        val slideButton = popupView.findViewById<Button>(R.id.slideButton)
        val fadeButton = popupView.findViewById<Button>(R.id.fadeButton)
        val scaleButton = popupView.findViewById<Button>(R.id.scaleButton)
        
        slideButton.setOnClickListener {
            showSlideAnimation()
        }
        
        fadeButton.setOnClickListener {
            showFadeAnimation()
        }
        
        scaleButton.setOnClickListener {
            showScaleAnimation()
        }
    }
    
    private fun setupClickListeners() {
        showAnimationPopupButton.setOnClickListener {
            showAnimationPopup(it)
        }
    }
    
    private fun showAnimationPopup(anchorView: View) {
        popupWindow.showAsDropDown(anchorView)
    }
    
    private fun showSlideAnimation() {
        Toast.makeText(this, "滑动动画", Toast.LENGTH_SHORT).show()
    }
    
    private fun showFadeAnimation() {
        Toast.makeText(this, "淡入淡出动画", Toast.LENGTH_SHORT).show()
    }
    
    private fun showScaleAnimation() {
        Toast.makeText(this, "缩放动画", Toast.LENGTH_SHORT).show()
    }
}
```

## 实际应用场景

### 1. 长按菜单弹窗

```kotlin
class LongClickPopupActivity : AppCompatActivity() {
    
    private lateinit var longClickView: View
    private lateinit var popupWindow: PopupWindow
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_long_click_popup)
        
        initViews()
        setupPopupWindow()
        setupLongClickListener()
    }
    
    private fun initViews() {
        longClickView = findViewById(R.id.longClickView)
    }
    
    private fun setupPopupWindow() {
        val popupView = layoutInflater.inflate(R.layout.popup_long_click_menu, null)
        
        popupWindow = PopupWindow(
            popupView,
            ViewGroup.LayoutParams.WRAP_CONTENT,
            ViewGroup.LayoutParams.WRAP_CONTENT,
            true
        )
        
        popupWindow.isOutsideTouchable = true
        popupWindow.isTouchable = true
        
        setupMenuItems(popupView)
    }
    
    private fun setupMenuItems(popupView: View) {
        val copyItem = popupView.findViewById<TextView>(R.id.copyItem)
        val pasteItem = popupView.findViewById<TextView>(R.id.pasteItem)
        val shareItem = popupView.findViewById<TextView>(R.id.shareItem)
        val deleteItem = popupView.findViewById<TextView>(R.id.deleteItem)
        
        copyItem.setOnClickListener {
            Toast.makeText(this, "复制", Toast.LENGTH_SHORT).show()
            popupWindow.dismiss()
        }
        
        pasteItem.setOnClickListener {
            Toast.makeText(this, "粘贴", Toast.LENGTH_SHORT).show()
            popupWindow.dismiss()
        }
        
        shareItem.setOnClickListener {
            Toast.makeText(this, "分享", Toast.LENGTH_SHORT).show()
            popupWindow.dismiss()
        }
        
        deleteItem.setOnClickListener {
            Toast.makeText(this, "删除", Toast.LENGTH_SHORT).show()
            popupWindow.dismiss()
        }
    }
    
    private fun setupLongClickListener() {
        longClickView.setOnLongClickListener {
            showPopupAtLongClickPosition(it)
            true
        }
    }
    
    private fun showPopupAtLongClickPosition(view: View) {
        val location = IntArray(2)
        view.getLocationOnScreen(location)
        
        val x = location[0] + view.width / 2
        val y = location[1] + view.height / 2
        
        popupWindow.showAtLocation(view, Gravity.NO_GRAVITY, x, y)
    }
}
```

### 2. 搜索建议弹窗

```kotlin
class SearchSuggestionPopupActivity : AppCompatActivity() {
    
    private lateinit var searchEditText: EditText
    private lateinit var popupWindow: PopupWindow
    private lateinit var suggestionAdapter: ArrayAdapter<String>
    
    private val suggestions = listOf(
        "Android开发", "Kotlin编程", "Java基础", "移动开发",
        "UI设计", "数据库", "网络编程", "算法"
    )
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_search_suggestion_popup)
        
        initViews()
        setupPopupWindow()
        setupSearchListener()
    }
    
    private fun initViews() {
        searchEditText = findViewById(R.id.searchEditText)
    }
    
    private fun setupPopupWindow() {
        val popupView = layoutInflater.inflate(R.layout.popup_search_suggestions, null)
        val listView = popupView.findViewById<ListView>(R.id.suggestionListView)
        
        suggestionAdapter = ArrayAdapter(this, android.R.layout.simple_list_item_1, mutableListOf())
        listView.adapter = suggestionAdapter
        
        popupWindow = PopupWindow(
            popupView,
            ViewGroup.LayoutParams.MATCH_PARENT,
            ViewGroup.LayoutParams.WRAP_CONTENT,
            true
        )
        
        popupWindow.isOutsideTouchable = true
        popupWindow.isTouchable = true
        
        listView.setOnItemClickListener { _, _, position, _ ->
            val selectedSuggestion = suggestionAdapter.getItem(position)
            searchEditText.setText(selectedSuggestion)
            popupWindow.dismiss()
        }
    }
    
    private fun setupSearchListener() {
        searchEditText.addTextChangedListener(object : TextWatcher {
            override fun beforeTextChanged(s: CharSequence?, start: Int, count: Int, after: Int) {}
            
            override fun onTextChanged(s: CharSequence?, start: Int, before: Int, count: Int) {
                val query = s.toString()
                if (query.isNotEmpty()) {
                    showSuggestions(query)
                } else {
                    popupWindow.dismiss()
                }
            }
            
            override fun afterTextChanged(s: Editable?) {}
        })
    }
    
    private fun showSuggestions(query: String) {
        val filteredSuggestions = suggestions.filter { it.contains(query, ignoreCase = true) }
        
        suggestionAdapter.clear()
        suggestionAdapter.addAll(filteredSuggestions)
        suggestionAdapter.notifyDataSetChanged()
        
        if (filteredSuggestions.isNotEmpty()) {
            popupWindow.showAsDropDown(searchEditText)
        } else {
            popupWindow.dismiss()
        }
    }
}
```

### 3. 工具提示弹窗

```kotlin
class TooltipPopupActivity : AppCompatActivity() {
    
    private lateinit var showTooltipButton: Button
    private lateinit var popupWindow: PopupWindow
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_tooltip_popup)
        
        initViews()
        setupTooltipPopupWindow()
        setupClickListeners()
    }
    
    private fun initViews() {
        showTooltipButton = findViewById(R.id.showTooltipButton)
    }
    
    private fun setupTooltipPopupWindow() {
        val popupView = layoutInflater.inflate(R.layout.popup_tooltip, null)
        
        popupWindow = PopupWindow(
            popupView,
            ViewGroup.LayoutParams.WRAP_CONTENT,
            ViewGroup.LayoutParams.WRAP_CONTENT,
            true
        )
        
        popupWindow.isOutsideTouchable = true
        popupWindow.isTouchable = true
        
        val tooltipText = popupView.findViewById<TextView>(R.id.tooltipText)
        tooltipText.text = "这是一个工具提示弹窗，用于显示帮助信息"
    }
    
    private fun setupClickListeners() {
        showTooltipButton.setOnClickListener {
            showTooltip(it)
        }
    }
    
    private fun showTooltip(anchorView: View) {
        val location = IntArray(2)
        anchorView.getLocationOnScreen(location)
        
        val x = location[0] + anchorView.width / 2
        val y = location[1] - dpToPx(10)
        
        popupWindow.showAtLocation(anchorView, Gravity.NO_GRAVITY, x, y)
        
        // 3秒后自动关闭
        Handler(Looper.getMainLooper()).postDelayed({
            if (popupWindow.isShowing) {
                popupWindow.dismiss()
            }
        }, 3000)
    }
    
    private fun dpToPx(dp: Int): Int {
        return (dp * resources.displayMetrics.density).toInt()
    }
}
```

## PopupWindow 最佳实践

### 1. 弹窗管理类

```kotlin
class PopupWindowManager {
    
    private var currentPopup: PopupWindow? = null
    
    fun showPopup(
        context: Context,
        contentView: View,
        anchorView: View,
        width: Int = ViewGroup.LayoutParams.WRAP_CONTENT,
        height: Int = ViewGroup.LayoutParams.WRAP_CONTENT,
        animationStyle: Int = 0
    ) {
        dismissCurrentPopup()
        
        currentPopup = PopupWindow(contentView, width, height, true).apply {
            isOutsideTouchable = true
            isTouchable = true
            if (animationStyle != 0) {
                this.animationStyle = animationStyle
            }
        }
        
        currentPopup?.showAsDropDown(anchorView)
    }
    
    fun dismissCurrentPopup() {
        currentPopup?.dismiss()
        currentPopup = null
    }
}
```

### 2. 弹窗工具类

```kotlin
object PopupWindowUtils {
    
    fun createMenuPopup(
        context: Context,
        menuItems: List<String>,
        onItemClick: (String) -> Unit
    ): PopupWindow {
        val popupView = LayoutInflater.from(context).inflate(R.layout.popup_menu, null)
        val listView = popupView.findViewById<ListView>(R.id.menuListView)
        
        val adapter = ArrayAdapter(context, android.R.layout.simple_list_item_1, menuItems)
        listView.adapter = adapter
        
        listView.setOnItemClickListener { _, _, position, _ ->
            onItemClick(menuItems[position])
        }
        
        return PopupWindow(
            popupView,
            ViewGroup.LayoutParams.WRAP_CONTENT,
            ViewGroup.LayoutParams.WRAP_CONTENT,
            true
        ).apply {
            isOutsideTouchable = true
            isTouchable = true
        }
    }
    
    fun createTooltipPopup(
        context: Context,
        message: String
    ): PopupWindow {
        val popupView = LayoutInflater.from(context).inflate(R.layout.popup_tooltip, null)
        val textView = popupView.findViewById<TextView>(R.id.tooltipText)
        textView.text = message
        
        return PopupWindow(
            popupView,
            ViewGroup.LayoutParams.WRAP_CONTENT,
            ViewGroup.LayoutParams.WRAP_CONTENT,
            true
        ).apply {
            isOutsideTouchable = true
            isTouchable = true
        }
    }
}
```

## 📋 总结

PopupWindow 是 Android 开发中重要的浮动窗口组件：

- **基本用法**：创建弹窗、设置属性、显示和关闭
- **位置控制**：支持多种显示位置和锚点
- **动画效果**：支持进入和退出动画
- **实际应用**：长按菜单、搜索建议、工具提示等场景
- **最佳实践**：弹窗管理、工具类封装

掌握 PopupWindow 的使用方法对于创建丰富的用户交互体验至关重要。
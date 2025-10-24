---
title: AlertDialog 消息提示
date: 2025-10-24
categories: ["Android"]
robots: all
summary: 详细介绍Android AlertDialog消息提示对话框的使用方法、自定义样式和实际应用场景
featureimage: images/android/13.jpg
---

# AlertDialog 消息提示

AlertDialog 是 Android 中最常用的对话框组件，用于向用户传递信息、提示或警告用户的行为。

## AlertDialog 基本概念

AlertDialog 是一个模态对话框，用于显示重要信息或获取用户确认。它提供了多种样式和交互方式。

### 基本方法

| 方法 | 说明 | 示例 |
|------|------|------|
| `setTitle()` | 设置对话框标题 | `setTitle("提示")` |
| `setMessage()` | 设置对话框内容 | `setMessage("确定要删除吗？")` |
| `setPositiveButton()` | 设置确认按钮 | `setPositiveButton("确定")` |
| `setNegativeButton()` | 设置取消按钮 | `setNegativeButton("取消")` |
| `setNeutralButton()` | 设置中性按钮 | `setNeutralButton("稍后")` |
| `create()` | 创建对话框 | `builder.create()` |
| `show()` | 显示对话框 | `dialog.show()` |

## 基本使用示例

### 1. 简单提示对话框

```kotlin
class AlertDialogActivity : AppCompatActivity() {
    
    private lateinit var showDialogButton: Button
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_alert_dialog)
        
        initViews()
        setupClickListeners()
    }
    
    private fun initViews() {
        showDialogButton = findViewById(R.id.showDialogButton)
    }
    
    private fun setupClickListeners() {
        showDialogButton.setOnClickListener {
            showSimpleDialog()
        }
    }
    
    private fun showSimpleDialog() {
        AlertDialog.Builder(this)
            .setTitle("提示")
            .setMessage("这是一个简单的提示对话框")
            .setPositiveButton("确定") { dialog, which ->
                Toast.makeText(this, "点击了确定", Toast.LENGTH_SHORT).show()
            }
            .setNegativeButton("取消") { dialog, which ->
                Toast.makeText(this, "点击了取消", Toast.LENGTH_SHORT).show()
            }
            .show()
    }
}
```

### 2. 确认对话框

```kotlin
class ConfirmDialogActivity : AppCompatActivity() {
    
    private lateinit var deleteButton: Button
    private lateinit var exitButton: Button
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_confirm_dialog)
        
        initViews()
        setupClickListeners()
    }
    
    private fun initViews() {
        deleteButton = findViewById(R.id.deleteButton)
        exitButton = findViewById(R.id.exitButton)
    }
    
    private fun setupClickListeners() {
        deleteButton.setOnClickListener {
            showDeleteConfirmDialog()
        }
        
        exitButton.setOnClickListener {
            showExitConfirmDialog()
        }
    }
    
    private fun showDeleteConfirmDialog() {
        AlertDialog.Builder(this)
            .setTitle("删除确认")
            .setMessage("确定要删除这个项目吗？此操作不可撤销。")
            .setPositiveButton("删除") { dialog, which ->
                performDelete()
            }
            .setNegativeButton("取消") { dialog, which ->
                Toast.makeText(this, "取消删除", Toast.LENGTH_SHORT).show()
            }
            .setIcon(android.R.drawable.ic_dialog_alert)
            .show()
    }
    
    private fun showExitConfirmDialog() {
        AlertDialog.Builder(this)
            .setTitle("退出应用")
            .setMessage("确定要退出应用吗？")
            .setPositiveButton("退出") { dialog, which ->
                finish()
            }
            .setNegativeButton("取消") { dialog, which ->
                Toast.makeText(this, "取消退出", Toast.LENGTH_SHORT).show()
            }
            .setNeutralButton("最小化") { dialog, which ->
                moveTaskToBack(true)
            }
            .show()
    }
    
    private fun performDelete() {
        Toast.makeText(this, "删除成功", Toast.LENGTH_SHORT).show()
        // 执行删除操作
    }
}
```

### 3. 列表选择对话框

```kotlin
class ListDialogActivity : AppCompatActivity() {
    
    private lateinit var showListButton: Button
    private lateinit var showMultiChoiceButton: Button
    
    private val items = arrayOf("选项1", "选项2", "选项3", "选项4", "选项5")
    private val selectedItems = booleanArrayOf(false, false, false, false, false)
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_list_dialog)
        
        initViews()
        setupClickListeners()
    }
    
    private fun initViews() {
        showListButton = findViewById(R.id.showListButton)
        showMultiChoiceButton = findViewById(R.id.showMultiChoiceButton)
    }
    
    private fun setupClickListeners() {
        showListButton.setOnClickListener {
            showSingleChoiceDialog()
        }
        
        showMultiChoiceButton.setOnClickListener {
            showMultiChoiceDialog()
        }
    }
    
    private fun showSingleChoiceDialog() {
        AlertDialog.Builder(this)
            .setTitle("选择选项")
            .setItems(items) { dialog, which ->
                Toast.makeText(this, "选择了: ${items[which]}", Toast.LENGTH_SHORT).show()
            }
            .setNegativeButton("取消") { dialog, which ->
                Toast.makeText(this, "取消选择", Toast.LENGTH_SHORT).show()
            }
            .show()
    }
    
    private fun showMultiChoiceDialog() {
        AlertDialog.Builder(this)
            .setTitle("多选选项")
            .setMultiChoiceItems(items, selectedItems) { dialog, which, isChecked ->
                selectedItems[which] = isChecked
            }
            .setPositiveButton("确定") { dialog, which ->
                val selectedOptions = mutableListOf<String>()
                selectedItems.forEachIndexed { index, isSelected ->
                    if (isSelected) {
                        selectedOptions.add(items[index])
                    }
                }
                Toast.makeText(this, "选择了: ${selectedOptions.joinToString(", ")}", Toast.LENGTH_LONG).show()
            }
            .setNegativeButton("取消") { dialog, which ->
                Toast.makeText(this, "取消选择", Toast.LENGTH_SHORT).show()
            }
            .show()
    }
}
```

## 自定义对话框

### 1. 自定义布局对话框

```kotlin
class CustomDialogActivity : AppCompatActivity() {
    
    private lateinit var showCustomDialogButton: Button
    private lateinit var showLoginDialogButton: Button
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_custom_dialog)
        
        initViews()
        setupClickListeners()
    }
    
    private fun initViews() {
        showCustomDialogButton = findViewById(R.id.showCustomDialogButton)
        showLoginDialogButton = findViewById(R.id.showLoginDialogButton)
    }
    
    private fun setupClickListeners() {
        showCustomDialogButton.setOnClickListener {
            showCustomLayoutDialog()
        }
        
        showLoginDialogButton.setOnClickListener {
            showLoginDialog()
        }
    }
    
    private fun showCustomLayoutDialog() {
        val dialogView = layoutInflater.inflate(R.layout.dialog_custom, null)
        
        val editText = dialogView.findViewById<EditText>(R.id.editText)
        val checkBox = dialogView.findViewById<CheckBox>(R.id.checkBox)
        
        AlertDialog.Builder(this)
            .setTitle("自定义对话框")
            .setView(dialogView)
            .setPositiveButton("确定") { dialog, which ->
                val inputText = editText.text.toString()
                val isChecked = checkBox.isChecked
                Toast.makeText(this, "输入: $inputText, 勾选: $isChecked", Toast.LENGTH_SHORT).show()
            }
            .setNegativeButton("取消") { dialog, which ->
                Toast.makeText(this, "取消操作", Toast.LENGTH_SHORT).show()
            }
            .show()
    }
    
    private fun showLoginDialog() {
        val dialogView = layoutInflater.inflate(R.layout.dialog_login, null)
        
        val usernameEditText = dialogView.findViewById<EditText>(R.id.usernameEditText)
        val passwordEditText = dialogView.findViewById<EditText>(R.id.passwordEditText)
        val rememberCheckBox = dialogView.findViewById<CheckBox>(R.id.rememberCheckBox)
        
        AlertDialog.Builder(this)
            .setTitle("用户登录")
            .setView(dialogView)
            .setPositiveButton("登录") { dialog, which ->
                val username = usernameEditText.text.toString()
                val password = passwordEditText.text.toString()
                val remember = rememberCheckBox.isChecked
                
                if (username.isNotEmpty() && password.isNotEmpty()) {
                    performLogin(username, password, remember)
                } else {
                    Toast.makeText(this, "请输入用户名和密码", Toast.LENGTH_SHORT).show()
                }
            }
            .setNegativeButton("取消") { dialog, which ->
                Toast.makeText(this, "取消登录", Toast.LENGTH_SHORT).show()
            }
            .setCancelable(false)
            .show()
    }
    
    private fun performLogin(username: String, password: String, remember: Boolean) {
        Toast.makeText(this, "登录成功: $username, 记住密码: $remember", Toast.LENGTH_SHORT).show()
        // 执行登录逻辑
    }
}
```

### 2. 自定义样式对话框

```xml
<!-- res/values/styles.xml -->
<style name="CustomDialogTheme" parent="Theme.AppCompat.Dialog">
    <item name="android:windowBackground">@drawable/dialog_background</item>
    <item name="android:windowAnimationStyle">@style/DialogAnimation</item>
</style>

<style name="DialogAnimation">
    <item name="android:windowEnterAnimation">@anim/dialog_enter</item>
    <item name="android:windowExitAnimation">@anim/dialog_exit</item>
</style>
```

```kotlin
class StyledDialogActivity : AppCompatActivity() {
    
    private lateinit var showStyledDialogButton: Button
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_styled_dialog)
        
        initViews()
        setupClickListeners()
    }
    
    private fun initViews() {
        showStyledDialogButton = findViewById(R.id.showStyledDialogButton)
    }
    
    private fun setupClickListeners() {
        showStyledDialogButton.setOnClickListener {
            showStyledDialog()
        }
    }
    
    private fun showStyledDialog() {
        val dialog = AlertDialog.Builder(this, R.style.CustomDialogTheme)
            .setTitle("样式对话框")
            .setMessage("这是一个自定义样式的对话框")
            .setPositiveButton("确定") { dialog, which ->
                Toast.makeText(this, "点击了确定", Toast.LENGTH_SHORT).show()
            }
            .setNegativeButton("取消") { dialog, which ->
                Toast.makeText(this, "点击了取消", Toast.LENGTH_SHORT).show()
            }
            .create()
        
        dialog.show()
        
        // 自定义按钮样式
        dialog.getButton(AlertDialog.BUTTON_POSITIVE)?.setTextColor(ContextCompat.getColor(this, R.color.primary))
        dialog.getButton(AlertDialog.BUTTON_NEGATIVE)?.setTextColor(ContextCompat.getColor(this, R.color.secondary))
    }
}
```

## 实际应用场景

### 1. 权限请求对话框

```kotlin
class PermissionDialogActivity : AppCompatActivity() {
    
    private lateinit var requestPermissionButton: Button
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_permission_dialog)
        
        initViews()
        setupClickListeners()
    }
    
    private fun initViews() {
        requestPermissionButton = findViewById(R.id.requestPermissionButton)
    }
    
    private fun setupClickListeners() {
        requestPermissionButton.setOnClickListener {
            showPermissionDialog()
        }
    }
    
    private fun showPermissionDialog() {
        AlertDialog.Builder(this)
            .setTitle("权限请求")
            .setMessage("应用需要访问相机权限来拍照，是否允许？")
            .setPositiveButton("允许") { dialog, which ->
                requestCameraPermission()
            }
            .setNegativeButton("拒绝") { dialog, which ->
                Toast.makeText(this, "权限被拒绝", Toast.LENGTH_SHORT).show()
            }
            .setIcon(android.R.drawable.ic_dialog_info)
            .show()
    }
    
    private fun requestCameraPermission() {
        if (ContextCompat.checkSelfPermission(this, Manifest.permission.CAMERA) 
            != PackageManager.PERMISSION_GRANTED) {
            ActivityCompat.requestPermissions(this, arrayOf(Manifest.permission.CAMERA), 1001)
        }
    }
}
```

### 2. 网络错误对话框

```kotlin
class NetworkErrorDialogActivity : AppCompatActivity() {
    
    private lateinit var simulateErrorButton: Button
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_network_error_dialog)
        
        initViews()
        setupClickListeners()
    }
    
    private fun initViews() {
        simulateErrorButton = findViewById(R.id.simulateErrorButton)
    }
    
    private fun setupClickListeners() {
        simulateErrorButton.setOnClickListener {
            showNetworkErrorDialog()
        }
    }
    
    private fun showNetworkErrorDialog() {
        AlertDialog.Builder(this)
            .setTitle("网络错误")
            .setMessage("网络连接失败，请检查网络设置后重试")
            .setPositiveButton("重试") { dialog, which ->
                retryNetworkRequest()
            }
            .setNegativeButton("取消") { dialog, which ->
                Toast.makeText(this, "取消操作", Toast.LENGTH_SHORT).show()
            }
            .setNeutralButton("设置") { dialog, which ->
                openNetworkSettings()
            }
            .setIcon(android.R.drawable.ic_dialog_alert)
            .setCancelable(false)
            .show()
    }
    
    private fun retryNetworkRequest() {
        Toast.makeText(this, "正在重试...", Toast.LENGTH_SHORT).show()
        // 执行重试逻辑
    }
    
    private fun openNetworkSettings() {
        Toast.makeText(this, "打开网络设置", Toast.LENGTH_SHORT).show()
        // 打开网络设置页面
    }
}
```

### 3. 更新提示对话框

```kotlin
class UpdateDialogActivity : AppCompatActivity() {
    
    private lateinit var showUpdateButton: Button
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_update_dialog)
        
        initViews()
        setupClickListeners()
    }
    
    private fun initViews() {
        showUpdateButton = findViewById(R.id.showUpdateButton)
    }
    
    private fun setupClickListeners() {
        showUpdateButton.setOnClickListener {
            showUpdateDialog()
        }
    }
    
    private fun showUpdateDialog() {
        AlertDialog.Builder(this)
            .setTitle("发现新版本")
            .setMessage("发现新版本 v2.0.0，是否立即更新？\n\n更新内容：\n• 修复已知问题\n• 新增功能\n• 性能优化")
            .setPositiveButton("立即更新") { dialog, which ->
                startUpdate()
            }
            .setNegativeButton("稍后更新") { dialog, which ->
                Toast.makeText(this, "稍后更新", Toast.LENGTH_SHORT).show()
            }
            .setNeutralButton("跳过此版本") { dialog, which ->
                skipThisVersion()
            }
            .setIcon(android.R.drawable.ic_dialog_info)
            .setCancelable(false)
            .show()
    }
    
    private fun startUpdate() {
        Toast.makeText(this, "开始更新...", Toast.LENGTH_SHORT).show()
        // 执行更新逻辑
    }
    
    private fun skipThisVersion() {
        Toast.makeText(this, "跳过此版本", Toast.LENGTH_SHORT).show()
        // 记录跳过版本
    }
}
```

## 对话框最佳实践

### 1. 对话框管理

```kotlin
class DialogManager {
    
    private var currentDialog: AlertDialog? = null
    
    fun showDialog(
        context: Context,
        title: String,
        message: String,
        positiveText: String = "确定",
        negativeText: String = "取消",
        onPositiveClick: (() -> Unit)? = null,
        onNegativeClick: (() -> Unit)? = null
    ) {
        dismissCurrentDialog()
        
        currentDialog = AlertDialog.Builder(context)
            .setTitle(title)
            .setMessage(message)
            .setPositiveButton(positiveText) { dialog, which ->
                onPositiveClick?.invoke()
            }
            .setNegativeButton(negativeText) { dialog, which ->
                onNegativeClick?.invoke()
            }
            .setOnDismissListener {
                currentDialog = null
            }
            .show()
    }
    
    fun dismissCurrentDialog() {
        currentDialog?.dismiss()
        currentDialog = null
    }
}
```

### 2. 对话框工具类

```kotlin
object DialogUtils {
    
    fun showConfirmDialog(
        context: Context,
        title: String,
        message: String,
        onConfirm: () -> Unit
    ) {
        AlertDialog.Builder(context)
            .setTitle(title)
            .setMessage(message)
            .setPositiveButton("确定") { dialog, which ->
                onConfirm()
            }
            .setNegativeButton("取消") { dialog, which ->
                // 什么都不做
            }
            .show()
    }
    
    fun showInfoDialog(
        context: Context,
        title: String,
        message: String
    ) {
        AlertDialog.Builder(context)
            .setTitle(title)
            .setMessage(message)
            .setPositiveButton("确定") { dialog, which ->
                // 什么都不做
            }
            .show()
    }
    
    fun showErrorDialog(
        context: Context,
        title: String = "错误",
        message: String
    ) {
        AlertDialog.Builder(context)
            .setTitle(title)
            .setMessage(message)
            .setPositiveButton("确定") { dialog, which ->
                // 什么都不做
            }
            .setIcon(android.R.drawable.ic_dialog_alert)
            .show()
    }
}
```

## 📋 总结

AlertDialog 是 Android 开发中重要的用户交互组件：

- **基本用法**：标题、内容、按钮设置
- **多种样式**：简单提示、确认对话框、列表选择
- **自定义布局**：支持自定义视图和样式
- **实际应用**：权限请求、错误提示、更新通知等场景
- **最佳实践**：对话框管理、工具类封装

掌握 AlertDialog 的使用方法对于创建良好的用户交互体验至关重要。
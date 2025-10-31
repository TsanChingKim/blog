---
title: Activity 活动组件
date: 2025-10-24
categories: ["Android"]
robots: all
summary: 详细介绍Android Activity活动组件的生命周期、启动模式、数据传递和最佳实践
featureimage: images/android/11.jpg
---

# Activity 活动组件

Activity 是 Android 应用的核心组件，代表一个用户界面屏幕。每个 Activity 都是一个独立的用户交互单元。

## Activity 基本概念

### 什么是 Activity

Activity 是 Android 应用的四大组件之一，代表应用中的一个屏幕或界面。每个 Activity 都有其生命周期，由系统管理。

### Activity 与 Layout 的关系

```kotlin
class MainActivity : AppCompatActivity() {
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // 设置布局文件
        setContentView(R.layout.activity_main)
        
        // 初始化界面
        initViews()
    }
    
    private fun initViews() {
        // 通过 findViewById 获取布局中的控件
        val textView = findViewById<TextView>(R.id.textView)
        val button = findViewById<Button>(R.id.button)
        
        // 设置控件属性
        textView.text = "Hello Activity!"
        button.setOnClickListener {
            Toast.makeText(this, "按钮被点击", Toast.LENGTH_SHORT).show()
        }
    }
}
```

## Activity 启动方式

### 1. 显式启动

通过指定具体的 Activity 类来启动：

```kotlin
class MainActivity : AppCompatActivity() {
    
    private lateinit var startButton: Button
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        
        initViews()
        setupClickListeners()
    }
    
    private fun initViews() {
        startButton = findViewById(R.id.startButton)
    }
    
    private fun setupClickListeners() {
        startButton.setOnClickListener {
            // 显式启动 SecondActivity
            val intent = Intent(this, SecondActivity::class.java)
            startActivity(intent)
        }
    }
}
```

### 2. 隐式启动

通过 Intent 的 action、category、data 等属性来启动：

```kotlin
class MainActivity : AppCompatActivity() {
    
    private lateinit var openWebButton: Button
    private lateinit var dialButton: Button
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        
        initViews()
        setupClickListeners()
    }
    
    private fun initViews() {
        openWebButton = findViewById(R.id.openWebButton)
        dialButton = findViewById(R.id.dialButton)
    }
    
    private fun setupClickListeners() {
        // 打开网页
        openWebButton.setOnClickListener {
            val intent = Intent(Intent.ACTION_VIEW).apply {
                data = Uri.parse("https://www.example.com")
            }
            startActivity(intent)
        }
        
        // 拨打电话
        dialButton.setOnClickListener {
            val intent = Intent(Intent.ACTION_DIAL).apply {
                data = Uri.parse("tel:10086")
            }
            startActivity(intent)
        }
    }
}
```

### 3. startActivityForResult

启动 Activity 并等待返回结果：

```kotlin
class MainActivity : AppCompatActivity() {
    
    private lateinit var selectImageButton: Button
    private val REQUEST_CODE_SELECT_IMAGE = 1001
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        
        initViews()
        setupClickListeners()
    }
    
    private fun initViews() {
        selectImageButton = findViewById(R.id.selectImageButton)
    }
    
    private fun setupClickListeners() {
        selectImageButton.setOnClickListener {
            val intent = Intent(Intent.ACTION_PICK).apply {
                type = "image/*"
            }
            startActivityForResult(intent, REQUEST_CODE_SELECT_IMAGE)
        }
    }
    
    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        super.onActivityResult(requestCode, resultCode, data)
        
        if (requestCode == REQUEST_CODE_SELECT_IMAGE && resultCode == RESULT_OK) {
            data?.data?.let { imageUri ->
                // 处理选择的图片
                handleSelectedImage(imageUri)
            }
        }
    }
    
    private fun handleSelectedImage(imageUri: Uri) {
        Toast.makeText(this, "图片已选择: $imageUri", Toast.LENGTH_SHORT).show()
    }
}
```

## Activity 启动模式

### 1. Standard（标准模式）

默认模式，每次启动都会创建新的 Activity 实例：

```xml
<!-- AndroidManifest.xml -->
<activity
    android:name=".MainActivity"
    android:launchMode="standard" />
```

```kotlin
class MainActivity : AppCompatActivity() {
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        
        Log.d("Activity", "onCreate: ${this.hashCode()}")
    }
    
    override fun onNewIntent(intent: Intent?) {
        super.onNewIntent(intent)
        Log.d("Activity", "onNewIntent: ${this.hashCode()}")
    }
}
```

### 2. SingleTop（顶部复用模式）

如果 Activity 已经在栈顶，则不会创建新实例：

```xml
<activity
    android:name=".MainActivity"
    android:launchMode="singleTop" />
```

```kotlin
class MainActivity : AppCompatActivity() {
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        
        Log.d("Activity", "onCreate: ${this.hashCode()}")
    }
    
    override fun onNewIntent(intent: Intent?) {
        super.onNewIntent(intent)
        Log.d("Activity", "onNewIntent: ${this.hashCode()}")
        // 处理新的 Intent
        handleNewIntent(intent)
    }
    
    private fun handleNewIntent(intent: Intent?) {
        // 更新界面或处理新数据
        Toast.makeText(this, "收到新的 Intent", Toast.LENGTH_SHORT).show()
    }
}
```

### 3. SingleTask（单任务模式）

整个应用中只有一个实例，会清除其上的所有 Activity：

```xml
<activity
    android:name=".MainActivity"
    android:launchMode="singleTask" />
```

```kotlin
class MainActivity : AppCompatActivity() {
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        
        Log.d("Activity", "onCreate: ${this.hashCode()}")
    }
    
    override fun onNewIntent(intent: Intent?) {
        super.onNewIntent(intent)
        Log.d("Activity", "onNewIntent: ${this.hashCode()}")
        // 处理新的 Intent
        handleNewIntent(intent)
    }
    
    private fun handleNewIntent(intent: Intent?) {
        // 更新界面或处理新数据
        Toast.makeText(this, "回到主界面", Toast.LENGTH_SHORT).show()
    }
}
```

### 4. SingleInstance（单实例模式）

单独的任务栈，整个系统中只有一个实例：

```xml
<activity
    android:name=".MainActivity"
    android:launchMode="singleInstance" />
```

## Activity 生命周期

### 生命周期方法详解

```kotlin
class LifecycleActivity : AppCompatActivity() {
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_lifecycle)
        
        Log.d("Lifecycle", "onCreate")
        // 初始化界面和数据
        initViews()
        initData()
    }
    
    override fun onStart() {
        super.onStart()
        Log.d("Lifecycle", "onStart")
        // Activity 变为可见状态
    }
    
    override fun onResume() {
        super.onResume()
        Log.d("Lifecycle", "onResume")
        // Activity 获得焦点，可以接收用户输入
        startLocationUpdates()
    }
    
    override fun onPause() {
        super.onPause()
        Log.d("Lifecycle", "onPause")
        // Activity 失去焦点，暂停操作
        stopLocationUpdates()
    }
    
    override fun onStop() {
        super.onStop()
        Log.d("Lifecycle", "onStop")
        // Activity 不可见
    }
    
    override fun onRestart() {
        super.onRestart()
        Log.d("Lifecycle", "onRestart")
        // 从停止状态重新启动
    }
    
    override fun onDestroy() {
        super.onDestroy()
        Log.d("Lifecycle", "onDestroy")
        // 释放资源
        releaseResources()
    }
    
    private fun initViews() {
        // 初始化界面控件
    }
    
    private fun initData() {
        // 初始化数据
    }
    
    private fun startLocationUpdates() {
        // 开始位置更新
    }
    
    private fun stopLocationUpdates() {
        // 停止位置更新
    }
    
    private fun releaseResources() {
        // 释放资源
    }
}
```

### 生命周期状态图

{{< mermaid >}}
graph TD
    A[onCreate] --> B[onStart]
    B --> C[onResume]
    C --> D[onPause]
    D --> E[onStop]
    E --> F[onDestroy]
    
    D --> C
    E --> B
    E --> F
    
    G[onRestart] --> B
    E --> G
{{< /mermaid >}}

### 保存和恢复状态

```kotlin
class StateActivity : AppCompatActivity() {
    
    private lateinit var editText: EditText
    private lateinit var counterText: TextView
    private var counter = 0
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_state)
        
        initViews()
        
        // 恢复保存的状态
        savedInstanceState?.let {
            counter = it.getInt("counter", 0)
            updateCounterDisplay()
        }
    }
    
    private fun initViews() {
        editText = findViewById(R.id.editText)
        counterText = findViewById(R.id.counterText)
        
        findViewById<Button>(R.id.incrementButton).setOnClickListener {
            counter++
            updateCounterDisplay()
        }
    }
    
    private fun updateCounterDisplay() {
        counterText.text = "计数: $counter"
    }
    
    override fun onSaveInstanceState(outState: Bundle) {
        super.onSaveInstanceState(outState)
        // 保存状态
        outState.putInt("counter", counter)
        outState.putString("editText", editText.text.toString())
    }
    
    override fun onRestoreInstanceState(savedInstanceState: Bundle) {
        super.onRestoreInstanceState(savedInstanceState)
        // 恢复状态
        counter = savedInstanceState.getInt("counter", 0)
        editText.setText(savedInstanceState.getString("editText", ""))
        updateCounterDisplay()
    }
}
```

## Activity 数据传递

### 1. 传递简单数据

```kotlin
class MainActivity : AppCompatActivity() {
    
    private lateinit var startButton: Button
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        
        initViews()
        setupClickListeners()
    }
    
    private fun initViews() {
        startButton = findViewById(R.id.startButton)
    }
    
    private fun setupClickListeners() {
        startButton.setOnClickListener {
            val intent = Intent(this, SecondActivity::class.java).apply {
                // 传递简单数据
                putExtra("name", "张三")
                putExtra("age", 25)
                putExtra("isStudent", true)
            }
            startActivity(intent)
        }
    }
}

class SecondActivity : AppCompatActivity() {
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_second)
        
        // 接收传递的数据
        val name = intent.getStringExtra("name")
        val age = intent.getIntExtra("age", 0)
        val isStudent = intent.getBooleanExtra("isStudent", false)
        
        // 显示数据
        findViewById<TextView>(R.id.nameText).text = "姓名: $name"
        findViewById<TextView>(R.id.ageText).text = "年龄: $age"
        findViewById<TextView>(R.id.studentText).text = "学生: $isStudent"
    }
}
```

### 2. 传递对象数据

```kotlin
// 数据类
data class User(
    val name: String,
    val age: Int,
    val email: String
) : Parcelable {
    
    constructor(parcel: Parcel) : this(
        parcel.readString() ?: "",
        parcel.readInt(),
        parcel.readString() ?: ""
    )
    
    override fun writeToParcel(parcel: Parcel, flags: Int) {
        parcel.writeString(name)
        parcel.writeInt(age)
        parcel.writeString(email)
    }
    
    override fun describeContents(): Int = 0
    
    companion object CREATOR : Parcelable.Creator<User> {
        override fun createFromParcel(parcel: Parcel): User = User(parcel)
        override fun newArray(size: Int): Array<User?> = arrayOfNulls(size)
    }
}

class MainActivity : AppCompatActivity() {
    
    private lateinit var startButton: Button
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        
        initViews()
        setupClickListeners()
    }
    
    private fun initViews() {
        startButton = findViewById(R.id.startButton)
    }
    
    private fun setupClickListeners() {
        startButton.setOnClickListener {
            val user = User("李四", 30, "lisi@example.com")
            val intent = Intent(this, SecondActivity::class.java).apply {
                putExtra("user", user)
            }
            startActivity(intent)
        }
    }
}

class SecondActivity : AppCompatActivity() {
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_second)
        
        // 接收传递的对象
        val user = intent.getParcelableExtra<User>("user")
        user?.let {
            findViewById<TextView>(R.id.nameText).text = "姓名: ${it.name}"
            findViewById<TextView>(R.id.ageText).text = "年龄: ${it.age}"
            findViewById<TextView>(R.id.emailText).text = "邮箱: ${it.email}"
        }
    }
}
```

### 3. 返回数据给上一个 Activity

```kotlin
class SecondActivity : AppCompatActivity() {
    
    private lateinit var resultButton: Button
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_second)
        
        initViews()
        setupClickListeners()
    }
    
    private fun initViews() {
        resultButton = findViewById(R.id.resultButton)
    }
    
    private fun setupClickListeners() {
        resultButton.setOnClickListener {
            val resultIntent = Intent().apply {
                putExtra("result", "操作成功")
                putExtra("code", 200)
            }
            setResult(RESULT_OK, resultIntent)
            finish()
        }
    }
}

class MainActivity : AppCompatActivity() {
    
    private val REQUEST_CODE_SECOND = 1001
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        
        initViews()
        setupClickListeners()
    }
    
    private fun initViews() {
        findViewById<Button>(R.id.startButton).setOnClickListener {
            val intent = Intent(this, SecondActivity::class.java)
            startActivityForResult(intent, REQUEST_CODE_SECOND)
        }
    }
    
    private fun setupClickListeners() {
        // 点击事件已在 initViews 中设置
    }
    
    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        super.onActivityResult(requestCode, resultCode, data)
        
        if (requestCode == REQUEST_CODE_SECOND && resultCode == RESULT_OK) {
            val result = data?.getStringExtra("result")
            val code = data?.getIntExtra("code", 0)
            
            Toast.makeText(this, "结果: $result, 代码: $code", Toast.LENGTH_SHORT).show()
        }
    }
}
```

## Activity 最佳实践

### 1. 内存泄漏防护

```kotlin
class MainActivity : AppCompatActivity() {
    
    private var handler: Handler? = null
    private var runnable: Runnable? = null
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        
        // 使用弱引用避免内存泄漏
        handler = Handler(Looper.getMainLooper())
        runnable = Runnable {
            // 更新界面
            updateUI()
        }
        
        handler?.postDelayed(runnable!!, 1000)
    }
    
    override fun onDestroy() {
        super.onDestroy()
        // 清理资源
        handler?.removeCallbacks(runnable!!)
        handler = null
        runnable = null
    }
    
    private fun updateUI() {
        // 更新界面逻辑
    }
}
```

### 2. 状态保存和恢复

```kotlin
class MainActivity : AppCompatActivity() {
    
    private lateinit var editText: EditText
    private var userInput: String = ""
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        
        initViews()
        
        // 恢复保存的状态
        savedInstanceState?.let {
            userInput = it.getString("userInput", "")
            editText.setText(userInput)
        }
    }
    
    private fun initViews() {
        editText = findViewById(R.id.editText)
        
        editText.addTextChangedListener(object : TextWatcher {
            override fun beforeTextChanged(s: CharSequence?, start: Int, count: Int, after: Int) {}
            
            override fun onTextChanged(s: CharSequence?, start: Int, before: Int, count: Int) {
                userInput = s.toString()
            }
            
            override fun afterTextChanged(s: Editable?) {}
        })
    }
    
    override fun onSaveInstanceState(outState: Bundle) {
        super.onSaveInstanceState(outState)
        outState.putString("userInput", userInput)
    }
}
```

### 3. 权限处理

```kotlin
class MainActivity : AppCompatActivity() {
    
    private val REQUEST_CODE_PERMISSION = 1001
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        
        checkPermissions()
    }
    
    private fun checkPermissions() {
        if (ContextCompat.checkSelfPermission(this, Manifest.permission.CAMERA) 
            != PackageManager.PERMISSION_GRANTED) {
            ActivityCompat.requestPermissions(
                this,
                arrayOf(Manifest.permission.CAMERA),
                REQUEST_CODE_PERMISSION
            )
        } else {
            // 权限已授予，执行相关操作
            openCamera()
        }
    }
    
    override fun onRequestPermissionsResult(
        requestCode: Int,
        permissions: Array<out String>,
        grantResults: IntArray
    ) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults)
        
        if (requestCode == REQUEST_CODE_PERMISSION) {
            if (grantResults.isNotEmpty() && grantResults[0] == PackageManager.PERMISSION_GRANTED) {
                // 权限已授予
                openCamera()
            } else {
                // 权限被拒绝
                Toast.makeText(this, "需要相机权限", Toast.LENGTH_SHORT).show()
            }
        }
    }
    
    private fun openCamera() {
        // 打开相机
        Toast.makeText(this, "相机已打开", Toast.LENGTH_SHORT).show()
    }
}
```

## 📋 总结

Activity 是 Android 应用的核心组件：

- **生命周期管理**：理解 onCreate、onStart、onResume 等生命周期方法
- **启动模式**：Standard、SingleTop、SingleTask、SingleInstance 四种模式
- **数据传递**：通过 Intent 传递简单数据和对象
- **状态保存**：使用 onSaveInstanceState 保存和恢复状态
- **最佳实践**：避免内存泄漏、正确处理权限、合理使用生命周期

掌握 Activity 的使用方法是 Android 开发的基础，对于构建高质量的应用至关重要。
---
title: ProgressBar 进度条控件
date: 2025-10-24
categories: ["Android"]
robots: all
summary: 详细介绍Android ProgressBar进度条控件的使用方法、样式配置和实际应用场景
featureimage: images/android/07.jpg
---

# ProgressBar 进度条控件

ProgressBar 是 Android 中用于显示进度的控件，支持多种样式和动画效果。

## ProgressBar 基本属性

```xml
<ProgressBar
    android:id="@+id/progressBar"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:layout_gravity="center" />
```

## ProgressBar 样式类型

### 1. 默认圆形进度条

```xml
<ProgressBar  
    android:layout_width="wrap_content"  
    android:layout_height="wrap_content"
    android:layout_gravity="center" />
```

### 2. 水平进度条

```xml
<ProgressBar  
    android:id="@+id/horizontalProgressBar"
    android:layout_width="match_parent"  
    android:layout_height="wrap_content"  
    style="?android:attr/progressBarStyleHorizontal"  
    android:progress="30"  
    android:max="100"
    android:layout_margin="16dp" />
```

### 3. 小尺寸进度条

```xml
<ProgressBar
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    style="?android:attr/progressBarStyleSmall"
    android:layout_gravity="center" />
```

### 4. 大尺寸进度条

```xml
<ProgressBar
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    style="?android:attr/progressBarStyleLarge"
    android:layout_gravity="center" />
```

## Kotlin 代码示例

### 基本使用

```kotlin
class ProgressBarActivity : AppCompatActivity() {
    
    private lateinit var progressBar: ProgressBar
    private lateinit var horizontalProgressBar: ProgressBar
    private lateinit var startButton: Button
    private lateinit var resetButton: Button
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_progress_bar)
        
        initViews()
        setupClickListeners()
    }
    
    private fun initViews() {
        progressBar = findViewById(R.id.progressBar)
        horizontalProgressBar = findViewById(R.id.horizontalProgressBar)
        startButton = findViewById(R.id.startButton)
        resetButton = findViewById(R.id.resetButton)
    }
    
    private fun setupClickListeners() {
        startButton.setOnClickListener {
            startProgress()
        }
        
        resetButton.setOnClickListener {
            resetProgress()
        }
    }
    
    private fun startProgress() {
        // 显示进度条
        progressBar.visibility = View.VISIBLE
        
        // 模拟进度更新
        simulateProgress()
    }
    
    private fun simulateProgress() {
        val handler = Handler(Looper.getMainLooper())
        var progress = 0
        
        val runnable = object : Runnable {
            override fun run() {
                progress += 10
                horizontalProgressBar.progress = progress
                
                if (progress < 100) {
                    handler.postDelayed(this, 200)
                } else {
                    // 进度完成，隐藏圆形进度条
                    progressBar.visibility = View.GONE
                    Toast.makeText(this@ProgressBarActivity, "进度完成！", Toast.LENGTH_SHORT).show()
                }
            }
        }
        
        handler.post(runnable)
    }
    
    private fun resetProgress() {
        horizontalProgressBar.progress = 0
        progressBar.visibility = View.GONE
    }
}
```

### 自定义进度条

```kotlin
class CustomProgressBarActivity : AppCompatActivity() {
    
    private lateinit var customProgressBar: ProgressBar
    private lateinit var seekBar: SeekBar
    private lateinit var progressText: TextView
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_custom_progress_bar)
        
        initViews()
        setupSeekBar()
    }
    
    private fun initViews() {
        customProgressBar = findViewById(R.id.customProgressBar)
        seekBar = findViewById(R.id.seekBar)
        progressText = findViewById(R.id.progressText)
    }
    
    private fun setupSeekBar() {
        seekBar.max = 100
        seekBar.progress = 0
        
        seekBar.setOnSeekBarChangeListener(object : SeekBar.OnSeekBarChangeListener {
            override fun onProgressChanged(seekBar: SeekBar?, progress: Int, fromUser: Boolean) {
                customProgressBar.progress = progress
                progressText.text = "进度: $progress%"
            }
            
            override fun onStartTrackingTouch(seekBar: SeekBar?) {
                // 开始拖拽
            }
            
            override fun onStopTrackingTouch(seekBar: SeekBar?) {
                // 停止拖拽
            }
        })
    }
}
```

### 文件下载进度示例

```kotlin
class DownloadActivity : AppCompatActivity() {
    
    private lateinit var downloadProgressBar: ProgressBar
    private lateinit var downloadButton: Button
    private lateinit var progressText: TextView
    private lateinit var statusText: TextView
    
    private var isDownloading = false
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_download)
        
        initViews()
        setupClickListeners()
    }
    
    private fun initViews() {
        downloadProgressBar = findViewById(R.id.downloadProgressBar)
        downloadButton = findViewById(R.id.downloadButton)
        progressText = findViewById(R.id.progressText)
        statusText = findViewById(R.id.statusText)
        
        downloadProgressBar.max = 100
        downloadProgressBar.progress = 0
    }
    
    private fun setupClickListeners() {
        downloadButton.setOnClickListener {
            if (!isDownloading) {
                startDownload()
            } else {
                cancelDownload()
            }
        }
    }
    
    private fun startDownload() {
        isDownloading = true
        downloadButton.text = "取消下载"
        statusText.text = "正在下载..."
        
        // 模拟文件下载
        simulateFileDownload()
    }
    
    private fun simulateFileDownload() {
        val handler = Handler(Looper.getMainLooper())
        var progress = 0
        
        val runnable = object : Runnable {
            override fun run() {
                if (isDownloading && progress < 100) {
                    progress += 2
                    downloadProgressBar.progress = progress
                    progressText.text = "下载进度: $progress%"
                    
                    handler.postDelayed(this, 100)
                } else if (progress >= 100) {
                    downloadComplete()
                }
            }
        }
        
        handler.post(runnable)
    }
    
    private fun downloadComplete() {
        isDownloading = false
        downloadButton.text = "开始下载"
        statusText.text = "下载完成！"
        Toast.makeText(this, "文件下载完成", Toast.LENGTH_SHORT).show()
    }
    
    private fun cancelDownload() {
        isDownloading = false
        downloadButton.text = "开始下载"
        statusText.text = "下载已取消"
        downloadProgressBar.progress = 0
        progressText.text = "下载进度: 0%"
    }
}
```

## 实际应用场景

### 1. 应用启动页面

```xml
<LinearLayout
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:gravity="center"
    android:background="@color/primary">
    
    <ImageView
        android:layout_width="120dp"
        android:layout_height="120dp"
        android:src="@drawable/app_logo"
        android:layout_marginBottom="32dp" />
    
    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="正在加载..."
        android:textSize="16sp"
        android:textColor="@color/white"
        android:layout_marginBottom="16dp" />
    
    <ProgressBar
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:indeterminateTint="@color/white" />
    
</LinearLayout>
```

### 2. 文件上传进度

```kotlin
class FileUploadActivity : AppCompatActivity() {
    
    private lateinit var uploadProgressBar: ProgressBar
    private lateinit var uploadButton: Button
    private lateinit var progressText: TextView
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_file_upload)
        
        initViews()
        setupUploadButton()
    }
    
    private fun initViews() {
        uploadProgressBar = findViewById(R.id.uploadProgressBar)
        uploadButton = findViewById(R.id.uploadButton)
        progressText = findViewById(R.id.progressText)
    }
    
    private fun setupUploadButton() {
        uploadButton.setOnClickListener {
            uploadFile()
        }
    }
    
    private fun uploadFile() {
        uploadButton.isEnabled = false
        uploadButton.text = "上传中..."
        
        // 模拟文件上传
        simulateFileUpload()
    }
    
    private fun simulateFileUpload() {
        val handler = Handler(Looper.getMainLooper())
        var progress = 0
        
        val runnable = object : Runnable {
            override fun run() {
                progress += 5
                uploadProgressBar.progress = progress
                progressText.text = "上传进度: $progress%"
                
                if (progress < 100) {
                    handler.postDelayed(this, 300)
                } else {
                    uploadComplete()
                }
            }
        }
        
        handler.post(runnable)
    }
    
    private fun uploadComplete() {
        uploadButton.isEnabled = true
        uploadButton.text = "上传文件"
        Toast.makeText(this, "文件上传成功", Toast.LENGTH_SHORT).show()
    }
}
```

### 3. 数据同步进度

```kotlin
class DataSyncActivity : AppCompatActivity() {
    
    private lateinit var syncProgressBar: ProgressBar
    private lateinit var syncButton: Button
    private lateinit var syncStatusText: TextView
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_data_sync)
        
        initViews()
        setupSyncButton()
    }
    
    private fun initViews() {
        syncProgressBar = findViewById(R.id.syncProgressBar)
        syncButton = findViewById(R.id.syncButton)
        syncStatusText = findViewById(R.id.syncStatusText)
    }
    
    private fun setupSyncButton() {
        syncButton.setOnClickListener {
            startDataSync()
        }
    }
    
    private fun startDataSync() {
        syncButton.isEnabled = false
        syncStatusText.text = "正在同步数据..."
        
        // 模拟数据同步
        simulateDataSync()
    }
    
    private fun simulateDataSync() {
        val syncSteps = listOf(
            "连接服务器" to 20,
            "下载用户数据" to 40,
            "同步设置" to 60,
            "更新缓存" to 80,
            "完成同步" to 100
        )
        
        var currentStep = 0
        
        val handler = Handler(Looper.getMainLooper())
        val runnable = object : Runnable {
            override fun run() {
                if (currentStep < syncSteps.size) {
                    val (stepName, progress) = syncSteps[currentStep]
                    syncStatusText.text = stepName
                    syncProgressBar.progress = progress
                    currentStep++
                    
                    handler.postDelayed(this, 1000)
                } else {
                    syncComplete()
                }
            }
        }
        
        handler.post(runnable)
    }
    
    private fun syncComplete() {
        syncButton.isEnabled = true
        syncStatusText.text = "数据同步完成"
        Toast.makeText(this, "数据同步成功", Toast.LENGTH_SHORT).show()
    }
}
```

## 自定义样式

### 自定义进度条样式

```xml
<!-- res/drawable/progress_bar_background.xml -->
<shape xmlns:android="http://schemas.android.com/apk/res/android"
    android:shape="rectangle">
    <corners android:radius="8dp" />
    <solid android:color="#E0E0E0" />
</shape>

<!-- res/drawable/progress_bar_progress.xml -->
<shape xmlns:android="http://schemas.android.com/apk/res/android"
    android:shape="rectangle">
    <corners android:radius="8dp" />
    <solid android:color="#2196F3" />
</shape>
```

```xml
<ProgressBar
    android:id="@+id/customProgressBar"
    android:layout_width="match_parent"
    android:layout_height="8dp"
    style="?android:attr/progressBarStyleHorizontal"
    android:progressDrawable="@drawable/custom_progress_bar"
    android:max="100"
    android:progress="50" />
```

### 自定义圆形进度条

```xml
<!-- res/drawable/circular_progress.xml -->
<shape xmlns:android="http://schemas.android.com/apk/res/android"
    android:shape="ring"
    android:innerRadiusRatio="3"
    android:thicknessRatio="8"
    android:useLevel="false">
    <solid android:color="#2196F3" />
</shape>
```

## 性能优化建议

### 1. 避免频繁更新

```kotlin
class OptimizedProgressBar {
    
    private var lastUpdateTime = 0L
    private val UPDATE_INTERVAL = 100L // 100ms更新一次
    
    fun updateProgress(progressBar: ProgressBar, progress: Int) {
        val currentTime = System.currentTimeMillis()
        if (currentTime - lastUpdateTime >= UPDATE_INTERVAL) {
            progressBar.progress = progress
            lastUpdateTime = currentTime
        }
    }
}
```

### 2. 使用动画平滑过渡

```kotlin
class SmoothProgressBar {
    
    fun animateProgress(progressBar: ProgressBar, targetProgress: Int) {
        val animator = ObjectAnimator.ofInt(progressBar, "progress", 
            progressBar.progress, targetProgress)
        animator.duration = 300
        animator.interpolator = DecelerateInterpolator()
        animator.start()
    }
}
```

## 📋 总结

ProgressBar 是 Android 开发中重要的进度显示控件：

- **多种样式**：圆形、水平、大小尺寸等不同样式
- **动态更新**：支持程序控制进度更新
- **实际应用**：文件下载、数据同步、应用启动等场景
- **自定义样式**：支持自定义外观和动画效果
- **性能优化**：合理控制更新频率，使用动画平滑过渡

掌握 ProgressBar 的使用方法对于提升用户体验至关重要。

---
title: ImageView 图片控件
date: 2025-10-24
categories: ["Android"]
robots: all
summary: 详细介绍Android ImageView图片控件的使用方法、属性配置、图片加载和缩放模式
featureimage: images/android/06.jpg
---

# ImageView 图片控件

ImageView 是 Android 中用于显示图片的控件，支持多种图片格式和显示模式。

## ImageView 基本属性

```xml
<ImageView
    android:id="@+id/imageView"
    android:layout_width="200dp"
    android:layout_height="200dp"
    android:src="@drawable/sample_image"
    android:scaleType="centerCrop"
    android:background="@color/image_background"
    android:padding="8dp"
    android:layout_margin="16dp" />
```

## 图片资源管理

### 资源文件夹说明

| 文件夹 | 用途 | 推荐使用场景 |
|--------|------|-------------|
| `drawable` | 矢量图、形状、选择器 | 图标、背景、状态选择器 |
| `drawable-hdpi` | 高密度屏幕图片 | 150dpi 屏幕 |
| `drawable-mdpi` | 中密度屏幕图片 | 160dpi 屏幕 |
| `drawable-xhdpi` | 超高密度屏幕图片 | 240dpi 屏幕 |
| `drawable-xxhdpi` | 超超高密度屏幕图片 | 320dpi 屏幕 |
| `drawable-xxxhdpi` | 超超超高密度屏幕图片 | 480dpi 屏幕 |
| `mipmap` | 应用图标 | 启动图标 |

### 基本使用

```xml
<!-- 使用 drawable 资源 -->
<ImageView
    android:id="@+id/imageView1"
    android:layout_width="100dp"
    android:layout_height="100dp"
    android:src="@drawable/ic_launcher_foreground" />

<!-- 使用 mipmap 资源 -->
<ImageView
    android:id="@+id/imageView2"
    android:layout_width="100dp"
    android:layout_height="100dp"
    android:src="@mipmap/ic_launcher" />
```

## 图片显示模式 (scaleType)

ImageView 提供了多种图片缩放模式：

### 1. centerCrop（推荐）
保持宽高比，裁剪多余部分，填满整个ImageView

```xml
<ImageView
    android:layout_width="200dp"
    android:layout_height="200dp"
    android:src="@drawable/sample_image"
    android:scaleType="centerCrop" />
```

### 2. centerInside
保持宽高比，完整显示图片，可能有空白区域

```xml
<ImageView
    android:layout_width="200dp"
    android:layout_height="200dp"
    android:src="@drawable/sample_image"
    android:scaleType="centerInside" />
```

### 3. fitCenter
保持宽高比，居中显示，可能有空白区域

```xml
<ImageView
    android:layout_width="200dp"
    android:layout_height="200dp"
    android:src="@drawable/sample_image"
    android:scaleType="fitCenter" />
```

### 4. fitXY
拉伸图片填满整个ImageView，可能变形

```xml
<ImageView
    android:layout_width="200dp"
    android:layout_height="200dp"
    android:src="@drawable/sample_image"
    android:scaleType="fitXY" />
```

### 5. matrix
使用矩阵变换，需要自定义

```xml
<ImageView
    android:layout_width="200dp"
    android:layout_height="200dp"
    android:src="@drawable/sample_image"
    android:scaleType="matrix" />
```

## Kotlin 代码示例

### 基本使用

```kotlin
class MainActivity : AppCompatActivity() {
    
    private lateinit var imageView: ImageView
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        
        initViews()
        setupImageView()
    }
    
    private fun initViews() {
        imageView = findViewById(R.id.imageView)
    }
    
    private fun setupImageView() {
        // 设置图片资源
        imageView.setImageResource(R.drawable.sample_image)
        
        // 设置缩放模式
        imageView.scaleType = ImageView.ScaleType.CENTER_CROP
        
        // 设置点击事件
        imageView.setOnClickListener {
            Toast.makeText(this, "图片被点击", Toast.LENGTH_SHORT).show()
        }
        
        // 设置长按事件
        imageView.setOnLongClickListener {
            showImageOptions()
            true
        }
    }
    
    private fun showImageOptions() {
        val options = arrayOf("保存图片", "分享图片", "设为壁纸")
        AlertDialog.Builder(this)
            .setTitle("图片操作")
            .setItems(options) { _, which ->
                when (which) {
                    0 -> saveImage()
                    1 -> shareImage()
                    2 -> setAsWallpaper()
                }
            }
            .show()
    }
    
    private fun saveImage() {
        Toast.makeText(this, "图片已保存", Toast.LENGTH_SHORT).show()
    }
    
    private fun shareImage() {
        Toast.makeText(this, "分享图片", Toast.LENGTH_SHORT).show()
    }
    
    private fun setAsWallpaper() {
        Toast.makeText(this, "设为壁纸", Toast.LENGTH_SHORT).show()
    }
}
```

### 动态切换图片

```kotlin
class ImageGalleryActivity : AppCompatActivity() {
    
    private lateinit var imageView: ImageView
    private lateinit var prevButton: Button
    private lateinit var nextButton: Button
    
    private val imageList = listOf(
        R.drawable.image1,
        R.drawable.image2,
        R.drawable.image3,
        R.drawable.image4
    )
    
    private var currentIndex = 0
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_image_gallery)
        
        initViews()
        setupImageGallery()
    }
    
    private fun initViews() {
        imageView = findViewById(R.id.imageView)
        prevButton = findViewById(R.id.prevButton)
        nextButton = findViewById(R.id.nextButton)
    }
    
    private fun setupImageGallery() {
        // 显示第一张图片
        updateImage()
        
        // 上一张按钮
        prevButton.setOnClickListener {
            currentIndex = if (currentIndex > 0) currentIndex - 1 else imageList.size - 1
            updateImage()
        }
        
        // 下一张按钮
        nextButton.setOnClickListener {
            currentIndex = if (currentIndex < imageList.size - 1) currentIndex + 1 else 0
            updateImage()
        }
        
        // 图片点击切换
        imageView.setOnClickListener {
            currentIndex = if (currentIndex < imageList.size - 1) currentIndex + 1 else 0
            updateImage()
        }
    }
    
    private fun updateImage() {
        imageView.setImageResource(imageList[currentIndex])
        
        // 添加切换动画
        val fadeIn = AlphaAnimation(0f, 1f)
        fadeIn.duration = 300
        imageView.startAnimation(fadeIn)
    }
}
```

## ImageButton 图片按钮

ImageButton 继承自 ImageView，专门用于显示图片按钮：

```xml
<ImageButton
    android:id="@+id/imageButton"
    android:layout_width="60dp"
    android:layout_height="60dp"
    android:src="@drawable/ic_add"
    android:background="@drawable/image_button_background"
    android:scaleType="centerInside"
    android:contentDescription="添加按钮" />
```

```kotlin
private fun setupImageButton() {
    imageButton.setOnClickListener {
        Toast.makeText(this, "图片按钮被点击", Toast.LENGTH_SHORT).show()
    }
    
    // 设置不同状态的图片
    val stateListDrawable = StateListDrawable()
    stateListDrawable.addState(intArrayOf(android.R.attr.state_pressed), 
        ContextCompat.getDrawable(this, R.drawable.ic_add_pressed))
    stateListDrawable.addState(intArrayOf(), 
        ContextCompat.getDrawable(this, R.drawable.ic_add_normal))
    
    imageButton.background = stateListDrawable
}
```

## 图片加载优化

### 使用 Glide 加载网络图片

```kotlin
// 添加依赖：implementation 'com.github.bumptech.glide:glide:4.15.1'

class NetworkImageActivity : AppCompatActivity() {
    
    private lateinit var imageView: ImageView
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_network_image)
        
        initViews()
        loadNetworkImage()
    }
    
    private fun initViews() {
        imageView = findViewById(R.id.imageView)
    }
    
    private fun loadNetworkImage() {
        val imageUrl = "https://example.com/image.jpg"
        
        Glide.with(this)
            .load(imageUrl)
            .placeholder(R.drawable.placeholder) // 占位图
            .error(R.drawable.error_image) // 错误图
            .centerCrop()
            .into(imageView)
    }
}
```

### 图片缓存管理

```kotlin
class ImageCacheManager {
    
    companion object {
        private const val CACHE_SIZE = 50 * 1024 * 1024 // 50MB
        
        fun setupImageCache(context: Context) {
            val cacheDir = File(context.cacheDir, "image_cache")
            if (!cacheDir.exists()) {
                cacheDir.mkdirs()
            }
        }
        
        fun clearImageCache(context: Context) {
            try {
                val cacheDir = File(context.cacheDir, "image_cache")
                if (cacheDir.exists()) {
                    cacheDir.deleteRecursively()
                }
            } catch (e: Exception) {
                Log.e("ImageCache", "清除缓存失败", e)
            }
        }
    }
}
```

## 图片处理功能

### 图片旋转

```kotlin
class ImageRotationActivity : AppCompatActivity() {
    
    private lateinit var imageView: ImageView
    private lateinit var rotateButton: Button
    
    private var rotationAngle = 0f
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_image_rotation)
        
        initViews()
        setupImageRotation()
    }
    
    private fun initViews() {
        imageView = findViewById(R.id.imageView)
        rotateButton = findViewById(R.id.rotateButton)
    }
    
    private fun setupImageRotation() {
        rotateButton.setOnClickListener {
            rotationAngle += 90f
            rotateImage()
        }
    }
    
    private fun rotateImage() {
        val rotation = ObjectAnimator.ofFloat(imageView, "rotation", 
            imageView.rotation, rotationAngle)
        rotation.duration = 300
        rotation.start()
    }
}
```

### 图片缩放

```kotlin
class ImageZoomActivity : AppCompatActivity() {
    
    private lateinit var imageView: ImageView
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_image_zoom)
        
        initViews()
        setupImageZoom()
    }
    
    private fun initViews() {
        imageView = findViewById(R.id.imageView)
    }
    
    private fun setupImageZoom() {
        // 设置触摸监听器实现缩放
        imageView.setOnTouchListener { _, event ->
            when (event.action) {
                MotionEvent.ACTION_DOWN -> {
                    // 开始缩放
                    true
                }
                MotionEvent.ACTION_MOVE -> {
                    // 处理缩放
                    true
                }
                MotionEvent.ACTION_UP -> {
                    // 结束缩放
                    true
                }
                else -> false
            }
        }
    }
}
```

## 图片选择器

### 从相册选择图片

```kotlin
class ImagePickerActivity : AppCompatActivity() {
    
    private lateinit var imageView: ImageView
    private lateinit var selectButton: Button
    
    private val REQUEST_CODE_GALLERY = 1001
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_image_picker)
        
        initViews()
        setupImagePicker()
    }
    
    private fun initViews() {
        imageView = findViewById(R.id.imageView)
        selectButton = findViewById(R.id.selectButton)
    }
    
    private fun setupImagePicker() {
        selectButton.setOnClickListener {
            openImagePicker()
        }
    }
    
    private fun openImagePicker() {
        val intent = Intent(Intent.ACTION_PICK)
        intent.type = "image/*"
        startActivityForResult(intent, REQUEST_CODE_GALLERY)
    }
    
    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        super.onActivityResult(requestCode, resultCode, data)
        
        if (requestCode == REQUEST_CODE_GALLERY && resultCode == RESULT_OK) {
            data?.data?.let { uri ->
                imageView.setImageURI(uri)
            }
        }
    }
}
```

## 性能优化建议

### 1. 图片压缩

```kotlin
class ImageCompression {
    
    companion object {
        fun compressImage(bitmap: Bitmap, quality: Int = 80): Bitmap {
            val outputStream = ByteArrayOutputStream()
            bitmap.compress(Bitmap.CompressFormat.JPEG, quality, outputStream)
            val byteArray = outputStream.toByteArray()
            return BitmapFactory.decodeByteArray(byteArray, 0, byteArray.size)
        }
        
        fun resizeImage(bitmap: Bitmap, maxWidth: Int, maxHeight: Int): Bitmap {
            val width = bitmap.width
            val height = bitmap.height
            
            val ratio = min(maxWidth.toFloat() / width, maxHeight.toFloat() / height)
            val newWidth = (width * ratio).toInt()
            val newHeight = (height * ratio).toInt()
            
            return Bitmap.createScaledBitmap(bitmap, newWidth, newHeight, true)
        }
    }
}
```

### 2. 内存管理

```kotlin
class ImageMemoryManager {
    
    companion object {
        fun getOptimalImageSize(context: Context, imageView: ImageView): Pair<Int, Int> {
            val displayMetrics = context.resources.displayMetrics
            val screenWidth = displayMetrics.widthPixels
            val screenHeight = displayMetrics.heightPixels
            
            // 根据屏幕尺寸计算最佳图片尺寸
            val optimalWidth = screenWidth / 2
            val optimalHeight = screenHeight / 3
            
            return Pair(optimalWidth, optimalHeight)
        }
        
        fun recycleBitmap(bitmap: Bitmap?) {
            bitmap?.let {
                if (!it.isRecycled) {
                    it.recycle()
                }
            }
        }
    }
}
```

## 📋 总结

ImageView 是 Android 开发中重要的图片显示控件：

- **多种缩放模式**：centerCrop、centerInside、fitCenter 等
- **资源管理**：合理使用 drawable 和 mipmap 文件夹
- **性能优化**：图片压缩、缓存管理、内存控制
- **功能扩展**：图片选择、旋转、缩放等交互功能
- **第三方库**：使用 Glide、Picasso 等库优化网络图片加载

掌握 ImageView 的使用方法和优化技巧是 Android 开发的重要技能。

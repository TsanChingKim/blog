---
title: ViewPager 滑动切换视图
date: 2025-10-24
categories: ["Android"]
robots: all
summary: 详细介绍了ViewPager2的作用、应用场景、引入方式等
featureimage: images/android/20.jpg
---

# ViewPager2 滑动切换视图

ViewPager2 是 Android 中用于实现页面滑动切换的重要组件，它支持水平滑动、垂直滑动，并且提供了丰富的自定义选项。

## 应用场景

### 1. 引导界面
- 应用首次启动时的功能介绍
- 新功能引导页面
- 用户操作指引

### 2. 相册多图片预览
- 图片浏览器的滑动切换
- 相册中的图片轮播
- 媒体文件的连续播放

### 3. 多Tab页面
- App主界面的Tab切换
- 分类页面的滑动浏览
- 内容分页展示

### 4. 广告播放
- Banner广告轮播
- 产品展示轮播
- 新闻资讯轮播

## ViewPager2 的优势

相比传统的 ViewPager，ViewPager2 具有以下优势：

- **基于 RecyclerView**：性能更好，内存占用更少
- **支持垂直滑动**：可以垂直方向滑动
- **Fragment 支持**：原生支持 Fragment
- **更好的生命周期管理**：自动处理 Fragment 生命周期
- **RTL 支持**：支持从右到左的语言

## 引入方式

### 1. 添加依赖

在 `build.gradle` (Module: app) 中添加：

```gradle
dependencies {
    implementation 'androidx.viewpager2:viewpager2:1.0.0'
}
```

### 2. 版本说明

- **ViewPager2**: 最新版本，推荐使用
- **ViewPager**: 旧版本，已不推荐
- **Support Library**: 已废弃，建议迁移到 AndroidX

## 使用步骤

### 步骤1：布局文件中添加 ViewPager2

```xml
<!-- activity_main.xml -->
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical">

    <androidx.viewpager2.widget.ViewPager2
        android:id="@+id/viewPager2"
        android:layout_width="match_parent"
        android:layout_height="0dp"
        android:layout_weight="1" />

    <!-- 指示器 -->
    <LinearLayout
        android:id="@+id/indicatorLayout"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_gravity="center"
        android:layout_marginTop="16dp"
        android:orientation="horizontal" />

</LinearLayout>
```

### 步骤2：创建页面布局

```xml
<!-- item_page.xml -->
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:gravity="center"
    android:padding="16dp">

    <ImageView
        android:id="@+id/imageView"
        android:layout_width="200dp"
        android:layout_height="200dp"
        android:layout_marginBottom="16dp"
        android:scaleType="centerCrop" />

    <TextView
        android:id="@+id/textView"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:textSize="18sp"
        android:textStyle="bold"
        android:textColor="#333333" />

    <TextView
        android:id="@+id/descriptionTextView"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_marginTop="8dp"
        android:textSize="14sp"
        android:textColor="#666666"
        android:gravity="center" />

</LinearLayout>
```

### 步骤3：创建适配器

```kotlin
class ViewPagerAdapter(private val pageList: List<PageData>) : 
    RecyclerView.Adapter<ViewPagerAdapter.ViewHolder>() {
    
    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        val view = LayoutInflater.from(parent.context)
            .inflate(R.layout.item_page, parent, false)
        return ViewHolder(view)
    }
    
    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        val pageData = pageList[position]
        holder.imageView.setImageResource(pageData.imageRes)
        holder.textView.text = pageData.title
        holder.descriptionTextView.text = pageData.description
    }
    
    override fun getItemCount(): Int = pageList.size
    
    class ViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        val imageView: ImageView = itemView.findViewById(R.id.imageView)
        val textView: TextView = itemView.findViewById(R.id.textView)
        val descriptionTextView: TextView = itemView.findViewById(R.id.descriptionTextView)
    }
}
```

### 步骤4：数据模型

```kotlin
data class PageData(
    val imageRes: Int,
    val title: String,
    val description: String
)
```

### 步骤5：在 Activity 中使用

```kotlin
class MainActivity : AppCompatActivity() {
    
    private lateinit var viewPager2: ViewPager2
    private lateinit var indicatorLayout: LinearLayout
    private lateinit var adapter: ViewPagerAdapter
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        
        initViews()
        setupViewPager()
        setupIndicators()
    }
    
    private fun initViews() {
        viewPager2 = findViewById(R.id.viewPager2)
        indicatorLayout = findViewById(R.id.indicatorLayout)
    }
    
    private fun setupViewPager() {
        // 准备数据
        val pageList = listOf(
            PageData(R.drawable.image1, "欢迎使用", "这是第一个页面"),
            PageData(R.drawable.image2, "功能介绍", "这是第二个页面"),
            PageData(R.drawable.image3, "开始使用", "这是第三个页面")
        )
        
        // 设置适配器
        adapter = ViewPagerAdapter(pageList)
        viewPager2.adapter = adapter
        
        // 设置页面变化监听
        viewPager2.registerOnPageChangeCallback(object : ViewPager2.OnPageChangeCallback() {
            override fun onPageSelected(position: Int) {
                super.onPageSelected(position)
                updateIndicators(position)
            }
        })
    }
    
    private fun setupIndicators() {
        // 创建指示器
        repeat(adapter.itemCount) { i ->
            val indicator = View(this).apply {
                setBackgroundResource(R.drawable.indicator_unselected)
                layoutParams = LinearLayout.LayoutParams(
                    dpToPx(8), dpToPx(8)
                ).apply {
                    setMargins(dpToPx(4), 0, dpToPx(4), 0)
                }
            }
            indicatorLayout.addView(indicator)
        }
        
        // 设置第一个指示器为选中状态
        updateIndicators(0)
    }
    
    private fun updateIndicators(position: Int) {
        repeat(indicatorLayout.childCount) { i ->
            val indicator = indicatorLayout.getChildAt(i)
            indicator.setBackgroundResource(
                if (i == position) R.drawable.indicator_selected 
                else R.drawable.indicator_unselected
            )
        }
    }
    
    private fun dpToPx(dp: Int): Int {
        return (dp * resources.displayMetrics.density).toInt()
    }
}
```

## 高级功能

### 1. 垂直滑动

```kotlin
// 设置垂直滑动
viewPager2.orientation = ViewPager2.ORIENTATION_VERTICAL
```

### 2. 禁用滑动

```kotlin
// 禁用用户滑动
viewPager2.isUserInputEnabled = false
```

### 3. 预加载页面

```kotlin
// 设置预加载页面数量
viewPager2.offscreenPageLimit = 2
```

### 4. Fragment 支持

```kotlin
class FragmentAdapter(fragmentActivity: FragmentActivity) : 
    FragmentStateAdapter(fragmentActivity) {
    
    override fun createFragment(position: Int): Fragment {
        // 根据位置返回对应的 Fragment
        return PageFragment.newInstance(position)
    }
    
    override fun getItemCount(): Int = 3 // 页面数量
}
```

## 注意事项

1. **内存管理**：ViewPager2 会自动回收不可见的页面，但仍需注意图片等资源的释放
2. **生命周期**：Fragment 的生命周期会被 ViewPager2 自动管理
3. **性能优化**：对于大量页面，建议使用 `FragmentStateAdapter` 而不是 `RecyclerView.Adapter`
4. **滑动冲突**：如果页面内部有滑动组件，需要注意滑动冲突的处理

## 总结

ViewPager2 是 Android 开发中实现页面滑动切换的最佳选择，它提供了丰富的功能和良好的性能。通过合理使用 ViewPager2，可以创建出流畅的用户体验和美观的界面效果。
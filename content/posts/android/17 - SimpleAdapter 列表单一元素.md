---
title: SimpleAdapter 列表单一元素
date: 2025-10-24
categories: ["Android"]
robots: all
summary: 详细介绍Android SimpleAdapter的使用方法、数据映射和实际应用场景
featureimage: images/android/17.jpg
---

# SimpleAdapter 列表单一元素

SimpleAdapter 是 Android 中用于显示复杂列表项的适配器，可以将 Map 数据映射到布局中的多个控件上。

## SimpleAdapter 基本概念

SimpleAdapter 用于显示包含多个字段的列表项，每个列表项可以包含多个文本、图片等控件。它通过 Map 数据结构来存储每个列表项的数据。

### 构造方法

```kotlin
SimpleAdapter(Context context, List<? extends Map<String, ?>> data, int resource, String[] from, int[] to)
```

| 参数 | 说明 | 示例 |
|------|------|------|
| `context` | 环境上下文 | `this` |
| `data` | 数据源（Map列表） | `listOf(map1, map2)` |
| `resource` | 布局资源ID | `R.layout.list_item` |
| `from` | Map中的键名数组 | `arrayOf("title", "subtitle")` |
| `to` | 布局中控件的ID数组 | `arrayOf(R.id.title, R.id.subtitle)` |

## 基本使用示例

### 1. 简单列表项

```kotlin
class SimpleAdapterActivity : AppCompatActivity() {
    
    private lateinit var listView: ListView
    private lateinit var adapter: SimpleAdapter
    
    private val dataList = mutableListOf<Map<String, Any>>()
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_simple_adapter)
        
        initViews()
        setupData()
        setupAdapter()
        setupListView()
    }
    
    private fun initViews() {
        listView = findViewById(R.id.listView)
    }
    
    private fun setupData() {
        dataList.addAll(listOf(
            mapOf(
                "title" to "Android开发",
                "subtitle" to "移动应用开发技术",
                "icon" to android.R.drawable.ic_menu_info_details
            ),
            mapOf(
                "title" to "Kotlin编程",
                "subtitle" to "现代编程语言",
                "icon" to android.R.drawable.ic_menu_edit
            ),
            mapOf(
                "title" to "Java基础",
                "subtitle" to "面向对象编程",
                "icon" to android.R.drawable.ic_menu_help
            ),
            mapOf(
                "title" to "UI设计",
                "subtitle" to "用户界面设计",
                "icon" to android.R.drawable.ic_menu_gallery
            )
        ))
    }
    
    private fun setupAdapter() {
        adapter = SimpleAdapter(
            this,
            dataList,
            R.layout.simple_list_item,
            arrayOf("title", "subtitle", "icon"),
            arrayOf(R.id.titleText, R.id.subtitleText, R.id.iconImage)
        )
    }
    
    private fun setupListView() {
        listView.adapter = adapter
        
        listView.onItemClickListener = AdapterView.OnItemClickListener { _, _, position, _ ->
            val item = dataList[position]
            val title = item["title"] as String
            Toast.makeText(this, "选择了: $title", Toast.LENGTH_SHORT).show()
        }
        
        listView.onItemLongClickListener = AdapterView.OnItemLongClickListener { _, _, position, _ ->
            showItemOptions(position)
            true
        }
    }
    
    private fun showItemOptions(position: Int) {
        val item = dataList[position]
        val title = item["title"] as String
        
        AlertDialog.Builder(this)
            .setTitle("操作选项")
            .setMessage("对 '$title' 执行什么操作？")
            .setPositiveButton("编辑") { _, _ ->
                editItem(position)
            }
            .setNegativeButton("删除") { _, _ ->
                removeItem(position)
            }
            .setNeutralButton("取消") { _, _ ->
                // 什么都不做
            }
            .show()
    }
    
    private fun editItem(position: Int) {
        val item = dataList[position]
        val currentTitle = item["title"] as String
        val currentSubtitle = item["subtitle"] as String
        
        val editText = EditText(this).apply {
            setText(currentTitle)
        }
        
        AlertDialog.Builder(this)
            .setTitle("编辑标题")
            .setView(editText)
            .setPositiveButton("确定") { _, _ ->
                val newTitle = editText.text.toString()
                if (newTitle.isNotEmpty()) {
                    dataList[position] = mapOf(
                        "title" to newTitle,
                        "subtitle" to currentSubtitle,
                        "icon" to item["icon"]!!
                    )
                    adapter.notifyDataSetChanged()
                    Toast.makeText(this, "已更新", Toast.LENGTH_SHORT).show()
                }
            }
            .setNegativeButton("取消") { _, _ ->
                // 什么都不做
            }
            .show()
    }
    
    private fun removeItem(position: Int) {
        dataList.removeAt(position)
        adapter.notifyDataSetChanged()
        Toast.makeText(this, "已删除", Toast.LENGTH_SHORT).show()
    }
}
```

### 2. 自定义布局文件

```xml
<!-- res/layout/simple_list_item.xml -->
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:orientation="horizontal"
    android:padding="16dp"
    android:background="?android:attr/selectableItemBackground">
    
    <ImageView
        android:id="@+id/iconImage"
        android:layout_width="48dp"
        android:layout_height="48dp"
        android:src="@drawable/ic_default"
        android:layout_marginEnd="16dp"
        android:scaleType="centerCrop" />
    
    <LinearLayout
        android:layout_width="0dp"
        android:layout_height="wrap_content"
        android:layout_weight="1"
        android:orientation="vertical">
        
        <TextView
            android:id="@+id/titleText"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:textSize="16sp"
            android:textStyle="bold"
            android:textColor="@android:color/black" />
        
        <TextView
            android:id="@+id/subtitleText"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:textSize="14sp"
            android:textColor="@android:color/darker_gray"
            android:layout_marginTop="4dp" />
        
    </LinearLayout>
    
    <ImageView
        android:id="@+id/arrowImage"
        android:layout_width="24dp"
        android:layout_height="24dp"
        android:src="@drawable/ic_arrow_right"
        android:layout_gravity="center_vertical" />
    
</LinearLayout>
```

### 3. 复杂列表项

```kotlin
class ComplexSimpleAdapterActivity : AppCompatActivity() {
    
    private lateinit var listView: ListView
    private lateinit var adapter: SimpleAdapter
    
    private val dataList = mutableListOf<Map<String, Any>>()
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_complex_simple_adapter)
        
        initViews()
        setupComplexData()
        setupAdapter()
        setupListView()
    }
    
    private fun initViews() {
        listView = findViewById(R.id.listView)
    }
    
    private fun setupComplexData() {
        dataList.addAll(listOf(
            mapOf(
                "name" to "张三",
                "phone" to "13800138000",
                "email" to "zhangsan@example.com",
                "avatar" to android.R.drawable.ic_menu_myplaces,
                "status" to "在线",
                "lastMessage" to "你好，最近怎么样？"
            ),
            mapOf(
                "name" to "李四",
                "phone" to "13800138001",
                "email" to "lisi@example.com",
                "avatar" to android.R.drawable.ic_menu_camera,
                "status" to "离线",
                "lastMessage" to "明天见面吧"
            ),
            mapOf(
                "name" to "王五",
                "phone" to "13800138002",
                "email" to "wangwu@example.com",
                "avatar" to android.R.drawable.ic_menu_send,
                "status" to "在线",
                "lastMessage" to "好的，没问题"
            ),
            mapOf(
                "name" to "赵六",
                "phone" to "13800138003",
                "email" to "zhaoliu@example.com",
                "avatar" to android.R.drawable.ic_menu_share,
                "status" to "忙碌",
                "lastMessage" to "稍后回复"
            )
        ))
    }
    
    private fun setupAdapter() {
        adapter = SimpleAdapter(
            this,
            dataList,
            R.layout.complex_list_item,
            arrayOf("name", "phone", "email", "avatar", "status", "lastMessage"),
            arrayOf(R.id.nameText, R.id.phoneText, R.id.emailText, R.id.avatarImage, R.id.statusText, R.id.lastMessageText)
        )
    }
    
    private fun setupListView() {
        listView.adapter = adapter
        
        listView.onItemClickListener = AdapterView.OnItemClickListener { _, _, position, _ ->
            val item = dataList[position]
            val name = item["name"] as String
            val phone = item["phone"] as String
            showContactDetail(name, phone)
        }
    }
    
    private fun showContactDetail(name: String, phone: String) {
        AlertDialog.Builder(this)
            .setTitle("联系人详情")
            .setMessage("姓名: $name\n电话: $phone")
            .setPositiveButton("确定") { _, _ ->
                // 什么都不做
            }
            .show()
    }
}
```

### 4. 复杂布局文件

```xml
<!-- res/layout/complex_list_item.xml -->
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:orientation="horizontal"
    android:padding="16dp"
    android:background="?android:attr/selectableItemBackground">
    
    <ImageView
        android:id="@+id/avatarImage"
        android:layout_width="60dp"
        android:layout_height="60dp"
        android:src="@drawable/ic_default_avatar"
        android:layout_marginEnd="16dp"
        android:scaleType="centerCrop"
        android:background="@drawable/circle_background" />
    
    <LinearLayout
        android:layout_width="0dp"
        android:layout_height="wrap_content"
        android:layout_weight="1"
        android:orientation="vertical">
        
        <LinearLayout
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:orientation="horizontal"
            android:gravity="center_vertical">
            
            <TextView
                android:id="@+id/nameText"
                android:layout_width="0dp"
                android:layout_height="wrap_content"
                android:layout_weight="1"
                android:textSize="18sp"
                android:textStyle="bold"
                android:textColor="@android:color/black" />
            
            <TextView
                android:id="@+id/statusText"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:textSize="12sp"
                android:textColor="@android:color/holo_green_dark"
                android:background="@drawable/status_background"
                android:padding="4dp" />
            
        </LinearLayout>
        
        <TextView
            android:id="@+id/phoneText"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:textSize="14sp"
            android:textColor="@android:color/darker_gray"
            android:layout_marginTop="4dp" />
        
        <TextView
            android:id="@+id/emailText"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:textSize="12sp"
            android:textColor="@android:color/darker_gray"
            android:layout_marginTop="2dp" />
        
        <TextView
            android:id="@+id/lastMessageText"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:textSize="14sp"
            android:textColor="@android:color/black"
            android:layout_marginTop="8dp"
            android:maxLines="2"
            android:ellipsize="end" />
        
    </LinearLayout>
    
</LinearLayout>
```

## 高级用法示例

### 1. 动态数据更新

```kotlin
class DynamicSimpleAdapterActivity : AppCompatActivity() {
    
    private lateinit var listView: ListView
    private lateinit var adapter: SimpleAdapter
    private lateinit var addButton: Button
    private lateinit var refreshButton: Button
    
    private val dataList = mutableListOf<Map<String, Any>>()
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_dynamic_simple_adapter)
        
        initViews()
        setupInitialData()
        setupAdapter()
        setupListView()
        setupButtons()
    }
    
    private fun initViews() {
        listView = findViewById(R.id.listView)
        addButton = findViewById(R.id.addButton)
        refreshButton = findViewById(R.id.refreshButton)
    }
    
    private fun setupInitialData() {
        dataList.addAll(listOf(
            mapOf(
                "title" to "初始项目1",
                "subtitle" to "这是初始数据",
                "icon" to android.R.drawable.ic_menu_info_details,
                "timestamp" to System.currentTimeMillis()
            ),
            mapOf(
                "title" to "初始项目2",
                "subtitle" to "这也是初始数据",
                "icon" to android.R.drawable.ic_menu_edit,
                "timestamp" to System.currentTimeMillis()
            )
        ))
    }
    
    private fun setupAdapter() {
        adapter = SimpleAdapter(
            this,
            dataList,
            R.layout.dynamic_list_item,
            arrayOf("title", "subtitle", "icon", "timestamp"),
            arrayOf(R.id.titleText, R.id.subtitleText, R.id.iconImage, R.id.timestampText)
        )
    }
    
    private fun setupListView() {
        listView.adapter = adapter
        
        listView.onItemClickListener = AdapterView.OnItemClickListener { _, _, position, _ ->
            val item = dataList[position]
            val title = item["title"] as String
            Toast.makeText(this, "选择了: $title", Toast.LENGTH_SHORT).show()
        }
    }
    
    private fun setupButtons() {
        addButton.setOnClickListener {
            addNewItem()
        }
        
        refreshButton.setOnClickListener {
            refreshData()
        }
    }
    
    private fun addNewItem() {
        val editText = EditText(this).apply {
            hint = "请输入新项目标题"
        }
        
        AlertDialog.Builder(this)
            .setTitle("添加新项目")
            .setView(editText)
            .setPositiveButton("添加") { _, _ ->
                val newTitle = editText.text.toString()
                if (newTitle.isNotEmpty()) {
                    val newItem = mapOf(
                        "title" to newTitle,
                        "subtitle" to "新添加的项目",
                        "icon" to android.R.drawable.ic_menu_add,
                        "timestamp" to System.currentTimeMillis()
                    )
                    dataList.add(newItem)
                    adapter.notifyDataSetChanged()
                    Toast.makeText(this, "已添加: $newTitle", Toast.LENGTH_SHORT).show()
                }
            }
            .setNegativeButton("取消") { _, _ ->
                // 什么都不做
            }
            .show()
    }
    
    private fun refreshData() {
        dataList.clear()
        setupInitialData()
        
        // 添加一些随机数据
        repeat(3) { index ->
            val randomItem = mapOf(
                "title" to "刷新项目${index + 1}",
                "subtitle" to "这是刷新后的数据",
                "icon" to android.R.drawable.ic_menu_refresh,
                "timestamp" to System.currentTimeMillis()
            )
            dataList.add(randomItem)
        }
        
        adapter.notifyDataSetChanged()
        Toast.makeText(this, "数据已刷新", Toast.LENGTH_SHORT).show()
    }
}
```

### 2. 自定义数据转换

```kotlin
class CustomSimpleAdapterActivity : AppCompatActivity() {
    
    private lateinit var listView: ListView
    private lateinit var adapter: SimpleAdapter
    
    private val dataList = mutableListOf<Map<String, Any>>()
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_custom_simple_adapter)
        
        initViews()
        setupCustomData()
        setupCustomAdapter()
        setupListView()
    }
    
    private fun initViews() {
        listView = findViewById(R.id.listView)
    }
    
    private fun setupCustomData() {
        dataList.addAll(listOf(
            mapOf(
                "name" to "张三",
                "age" to 25,
                "salary" to 8000.0,
                "department" to "技术部",
                "avatar" to android.R.drawable.ic_menu_myplaces
            ),
            mapOf(
                "name" to "李四",
                "age" to 30,
                "salary" to 12000.0,
                "department" to "产品部",
                "avatar" to android.R.drawable.ic_menu_camera
            ),
            mapOf(
                "name" to "王五",
                "age" to 28,
                "salary" to 10000.0,
                "department" to "设计部",
                "avatar" to android.R.drawable.ic_menu_send
            )
        ))
    }
    
    private fun setupCustomAdapter() {
        adapter = object : SimpleAdapter(
            this,
            dataList,
            R.layout.custom_list_item,
            arrayOf("name", "age", "salary", "department", "avatar"),
            arrayOf(R.id.nameText, R.id.ageText, R.id.salaryText, R.id.departmentText, R.id.avatarImage)
        ) {
            override fun setViewText(TextView v: TextView, String text: String) {
                when (v.id) {
                    R.id.ageText -> {
                        v.text = "年龄: $text 岁"
                    }
                    R.id.salaryText -> {
                        v.text = "薪资: ¥$text"
                    }
                    R.id.departmentText -> {
                        v.text = "部门: $text"
                    }
                    else -> {
                        super.setViewText(v, text)
                    }
                }
            }
            
            override fun setViewImage(ImageView v: ImageView, Int value: Int) {
                v.setImageResource(value)
            }
        }
    }
    
    private fun setupListView() {
        listView.adapter = adapter
        
        listView.onItemClickListener = AdapterView.OnItemClickListener { _, _, position, _ ->
            val item = dataList[position]
            val name = item["name"] as String
            val age = item["age"] as Int
            val salary = item["salary"] as Double
            val department = item["department"] as String
            
            showEmployeeDetail(name, age, salary, department)
        }
    }
    
    private fun showEmployeeDetail(name: String, age: Int, salary: Double, department: String) {
        AlertDialog.Builder(this)
            .setTitle("员工详情")
            .setMessage("姓名: $name\n年龄: $age\n薪资: ¥$salary\n部门: $department")
            .setPositiveButton("确定") { _, _ ->
                // 什么都不做
            }
            .show()
    }
}
```

## 实际应用场景

### 1. 联系人列表

```kotlin
class ContactListActivity : AppCompatActivity() {
    
    private lateinit var listView: ListView
    private lateinit var adapter: SimpleAdapter
    
    private val contactList = mutableListOf<Map<String, Any>>()
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_contact_list)
        
        initViews()
        loadContacts()
        setupAdapter()
        setupListView()
    }
    
    private fun initViews() {
        listView = findViewById(R.id.listView)
    }
    
    private fun loadContacts() {
        contactList.addAll(listOf(
            mapOf(
                "name" to "张三",
                "phone" to "13800138000",
                "email" to "zhangsan@example.com",
                "avatar" to android.R.drawable.ic_menu_myplaces,
                "isOnline" to true
            ),
            mapOf(
                "name" to "李四",
                "phone" to "13800138001",
                "email" to "lisi@example.com",
                "avatar" to android.R.drawable.ic_menu_camera,
                "isOnline" to false
            ),
            mapOf(
                "name" to "王五",
                "phone" to "13800138002",
                "email" to "wangwu@example.com",
                "avatar" to android.R.drawable.ic_menu_send,
                "isOnline" to true
            )
        ))
    }
    
    private fun setupAdapter() {
        adapter = SimpleAdapter(
            this,
            contactList,
            R.layout.contact_list_item,
            arrayOf("name", "phone", "email", "avatar", "isOnline"),
            arrayOf(R.id.nameText, R.id.phoneText, R.id.emailText, R.id.avatarImage, R.id.statusIndicator)
        )
    }
    
    private fun setupListView() {
        listView.adapter = adapter
        
        listView.onItemClickListener = AdapterView.OnItemClickListener { _, _, position, _ ->
            val contact = contactList[position]
            val name = contact["name"] as String
            val phone = contact["phone"] as String
            callContact(name, phone)
        }
    }
    
    private fun callContact(name: String, phone: String) {
        AlertDialog.Builder(this)
            .setTitle("拨打电话")
            .setMessage("是否拨打 $name 的电话: $phone")
            .setPositiveButton("拨打") { _, _ ->
                Toast.makeText(this, "正在拨打 $phone", Toast.LENGTH_SHORT).show()
            }
            .setNegativeButton("取消") { _, _ ->
                // 什么都不做
            }
            .show()
    }
}
```

## SimpleAdapter 最佳实践

### 1. 数据模型类

```kotlin
data class ListItem(
    val title: String,
    val subtitle: String,
    val icon: Int,
    val timestamp: Long = System.currentTimeMillis()
) {
    fun toMap(): Map<String, Any> {
        return mapOf(
            "title" to title,
            "subtitle" to subtitle,
            "icon" to icon,
            "timestamp" to timestamp
        )
    }
}

object ListItemMapper {
    fun fromMap(map: Map<String, Any>): ListItem {
        return ListItem(
            title = map["title"] as String,
            subtitle = map["subtitle"] as String,
            icon = map["icon"] as Int,
            timestamp = map["timestamp"] as Long
        )
    }
}
```

### 2. 适配器工具类

```kotlin
object SimpleAdapterUtils {
    
    fun createSimpleAdapter(
        context: Context,
        data: List<Map<String, Any>>,
        layoutRes: Int,
        fromKeys: Array<String>,
        toIds: IntArray
    ): SimpleAdapter {
        return SimpleAdapter(context, data, layoutRes, fromKeys, toIds)
    }
    
    fun createContactAdapter(
        context: Context,
        contacts: List<Map<String, Any>>
    ): SimpleAdapter {
        return SimpleAdapter(
            context,
            contacts,
            R.layout.contact_list_item,
            arrayOf("name", "phone", "email", "avatar"),
            arrayOf(R.id.nameText, R.id.phoneText, R.id.emailText, R.id.avatarImage)
        )
    }
    
    fun createMessageAdapter(
        context: Context,
        messages: List<Map<String, Any>>
    ): SimpleAdapter {
        return SimpleAdapter(
            context,
            messages,
            R.layout.message_list_item,
            arrayOf("sender", "content", "time", "avatar"),
            arrayOf(R.id.senderText, R.id.contentText, R.id.timeText, R.id.avatarImage)
        )
    }
}
```

## 📋 总结

SimpleAdapter 是 Android 开发中用于复杂列表项的适配器：

- **基本用法**：Map数据映射到多个控件
- **数据绑定**：支持文本、图片等多种数据类型
- **自定义转换**：支持自定义数据转换逻辑
- **实际应用**：联系人列表、消息列表、员工列表等场景
- **最佳实践**：数据模型类、工具类封装

掌握 SimpleAdapter 的使用方法对于创建复杂的列表界面至关重要。
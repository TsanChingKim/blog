---
title: ArrayAdapter 数组适配器
date: 2025-10-24
categories: ["Android"]
robots: all
summary: 详细介绍Android ArrayAdapter数组适配器的使用方法、自定义样式和实际应用场景
featureimage: images/android/15.jpg
---

# ArrayAdapter 数组适配器

ArrayAdapter 是 Android 中最简单的适配器，用于将数组或列表数据绑定到 ListView 等列表控件上。

## ArrayAdapter 基本概念

ArrayAdapter 是一个简单的适配器，只能用来显示单一的文本内容。它适用于简单的文本列表显示场景。

### 构造方法

```kotlin
ArrayAdapter(Context context, int resource, int textViewResourceId, List<T> objects)
```

| 参数 | 说明 | 示例 |
|------|------|------|
| `context` | 环境上下文 | `this` |
| `resource` | 布局资源ID | `R.layout.list_item` |
| `textViewResourceId` | 文本控件ID | `R.id.textView` |
| `objects` | 数据源 | `listOf("项目1", "项目2")` |

## 基本使用示例

### 1. 简单文本列表

```kotlin
class ArrayAdapterActivity : AppCompatActivity() {
    
    private lateinit var listView: ListView
    private lateinit var adapter: ArrayAdapter<String>
    
    private val dataList = mutableListOf(
        "Android开发",
        "Kotlin编程",
        "Java基础",
        "移动开发",
        "UI设计",
        "数据库",
        "网络编程",
        "算法"
    )
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_array_adapter)
        
        initViews()
        setupAdapter()
        setupListView()
    }
    
    private fun initViews() {
        listView = findViewById(R.id.listView)
    }
    
    private fun setupAdapter() {
        adapter = ArrayAdapter(
            this,
            android.R.layout.simple_list_item_1,
            android.R.id.text1,
            dataList
        )
    }
    
    private fun setupListView() {
        listView.adapter = adapter
        
        listView.onItemClickListener = AdapterView.OnItemClickListener { _, _, position, _ ->
            val selectedItem = dataList[position]
            Toast.makeText(this, "选择了: $selectedItem", Toast.LENGTH_SHORT).show()
        }
        
        listView.onItemLongClickListener = AdapterView.OnItemLongClickListener { _, _, position, _ ->
            showItemOptions(position)
            true
        }
    }
    
    private fun showItemOptions(position: Int) {
        val item = dataList[position]
        AlertDialog.Builder(this)
            .setTitle("操作选项")
            .setMessage("对 '$item' 执行什么操作？")
            .setPositiveButton("删除") { _, _ ->
                removeItem(position)
            }
            .setNegativeButton("编辑") { _, _ ->
                editItem(position)
            }
            .setNeutralButton("取消") { _, _ ->
                // 什么都不做
            }
            .show()
    }
    
    private fun removeItem(position: Int) {
        dataList.removeAt(position)
        adapter.notifyDataSetChanged()
        Toast.makeText(this, "已删除", Toast.LENGTH_SHORT).show()
    }
    
    private fun editItem(position: Int) {
        val currentItem = dataList[position]
        val editText = EditText(this).apply {
            setText(currentItem)
        }
        
        AlertDialog.Builder(this)
            .setTitle("编辑项目")
            .setView(editText)
            .setPositiveButton("确定") { _, _ ->
                val newText = editText.text.toString()
                if (newText.isNotEmpty()) {
                    dataList[position] = newText
                    adapter.notifyDataSetChanged()
                    Toast.makeText(this, "已更新", Toast.LENGTH_SHORT).show()
                }
            }
            .setNegativeButton("取消") { _, _ ->
                // 什么都不做
            }
            .show()
    }
}
```

### 2. 自定义布局适配器

```kotlin
class CustomArrayAdapterActivity : AppCompatActivity() {
    
    private lateinit var listView: ListView
    private lateinit var adapter: ArrayAdapter<String>
    private lateinit var addButton: Button
    
    private val dataList = mutableListOf(
        "项目1", "项目2", "项目3", "项目4", "项目5"
    )
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_custom_array_adapter)
        
        initViews()
        setupCustomAdapter()
        setupListView()
        setupAddButton()
    }
    
    private fun initViews() {
        listView = findViewById(R.id.listView)
        addButton = findViewById(R.id.addButton)
    }
    
    private fun setupCustomAdapter() {
        adapter = ArrayAdapter(
            this,
            R.layout.custom_list_item,
            R.id.itemText,
            dataList
        )
    }
    
    private fun setupListView() {
        listView.adapter = adapter
        
        listView.onItemClickListener = AdapterView.OnItemClickListener { _, _, position, _ ->
            val selectedItem = dataList[position]
            Toast.makeText(this, "选择了: $selectedItem", Toast.LENGTH_SHORT).show()
        }
    }
    
    private fun setupAddButton() {
        addButton.setOnClickListener {
            addNewItem()
        }
    }
    
    private fun addNewItem() {
        val editText = EditText(this).apply {
            hint = "请输入新项目"
        }
        
        AlertDialog.Builder(this)
            .setTitle("添加新项目")
            .setView(editText)
            .setPositiveButton("添加") { _, _ ->
                val newItem = editText.text.toString()
                if (newItem.isNotEmpty()) {
                    dataList.add(newItem)
                    adapter.notifyDataSetChanged()
                    Toast.makeText(this, "已添加: $newItem", Toast.LENGTH_SHORT).show()
                }
            }
            .setNegativeButton("取消") { _, _ ->
                // 什么都不做
            }
            .show()
    }
}
```

### 3. 自定义布局文件

```xml
<!-- res/layout/custom_list_item.xml -->
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:orientation="horizontal"
    android:padding="16dp"
    android:background="?android:attr/selectableItemBackground">
    
    <ImageView
        android:id="@+id/itemIcon"
        android:layout_width="24dp"
        android:layout_height="24dp"
        android:src="@drawable/ic_item"
        android:layout_marginEnd="16dp" />
    
    <TextView
        android:id="@+id/itemText"
        android:layout_width="0dp"
        android:layout_height="wrap_content"
        android:layout_weight="1"
        android:textSize="16sp"
        android:textColor="@android:color/black" />
    
    <ImageView
        android:id="@+id/arrowIcon"
        android:layout_width="16dp"
        android:layout_height="16dp"
        android:src="@drawable/ic_arrow_right"
        android:layout_gravity="center_vertical" />
    
</LinearLayout>
```

## 高级用法示例

### 1. 带过滤功能的适配器

```kotlin
class FilterableArrayAdapterActivity : AppCompatActivity() {
    
    private lateinit var listView: ListView
    private lateinit var searchEditText: EditText
    private lateinit var adapter: ArrayAdapter<String>
    
    private val originalData = listOf(
        "Android开发", "Kotlin编程", "Java基础", "移动开发",
        "UI设计", "数据库", "网络编程", "算法",
        "Android Studio", "Kotlin协程", "Java集合", "移动端开发",
        "Material Design", "SQLite", "HTTP协议", "排序算法"
    )
    
    private val filteredData = mutableListOf<String>()
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_filterable_array_adapter)
        
        initViews()
        setupAdapter()
        setupListView()
        setupSearch()
    }
    
    private fun initViews() {
        listView = findViewById(R.id.listView)
        searchEditText = findViewById(R.id.searchEditText)
    }
    
    private fun setupAdapter() {
        filteredData.addAll(originalData)
        adapter = ArrayAdapter(
            this,
            android.R.layout.simple_list_item_1,
            android.R.id.text1,
            filteredData
        )
    }
    
    private fun setupListView() {
        listView.adapter = adapter
        
        listView.onItemClickListener = AdapterView.OnItemClickListener { _, _, position, _ ->
            val selectedItem = filteredData[position]
            Toast.makeText(this, "选择了: $selectedItem", Toast.LENGTH_SHORT).show()
        }
    }
    
    private fun setupSearch() {
        searchEditText.addTextChangedListener(object : TextWatcher {
            override fun beforeTextChanged(s: CharSequence?, start: Int, count: Int, after: Int) {}
            
            override fun onTextChanged(s: CharSequence?, start: Int, before: Int, count: Int) {
                filterData(s.toString())
            }
            
            override fun afterTextChanged(s: Editable?) {}
        })
    }
    
    private fun filterData(query: String) {
        filteredData.clear()
        
        if (query.isEmpty()) {
            filteredData.addAll(originalData)
        } else {
            originalData.forEach { item ->
                if (item.contains(query, ignoreCase = true)) {
                    filteredData.add(item)
                }
            }
        }
        
        adapter.notifyDataSetChanged()
    }
}
```

### 2. 多选列表适配器

```kotlin
class MultiSelectArrayAdapterActivity : AppCompatActivity() {
    
    private lateinit var listView: ListView
    private lateinit var adapter: ArrayAdapter<String>
    private lateinit var selectAllButton: Button
    private lateinit var clearAllButton: Button
    private lateinit var selectedCountText: TextView
    
    private val dataList = mutableListOf(
        "选项1", "选项2", "选项3", "选项4", "选项5",
        "选项6", "选项7", "选项8", "选项9", "选项10"
    )
    
    private val selectedItems = mutableSetOf<Int>()
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_multi_select_array_adapter)
        
        initViews()
        setupAdapter()
        setupListView()
        setupButtons()
    }
    
    private fun initViews() {
        listView = findViewById(R.id.listView)
        selectAllButton = findViewById(R.id.selectAllButton)
        clearAllButton = findViewById(R.id.clearAllButton)
        selectedCountText = findViewById(R.id.selectedCountText)
    }
    
    private fun setupAdapter() {
        adapter = ArrayAdapter(
            this,
            android.R.layout.simple_list_item_multiple_choice,
            android.R.id.text1,
            dataList
        )
    }
    
    private fun setupListView() {
        listView.adapter = adapter
        listView.choiceMode = ListView.CHOICE_MODE_MULTIPLE
        
        listView.onItemClickListener = AdapterView.OnItemClickListener { _, _, position, _ ->
            if (selectedItems.contains(position)) {
                selectedItems.remove(position)
            } else {
                selectedItems.add(position)
            }
            updateSelectedCount()
        }
        
        updateSelectedCount()
    }
    
    private fun setupButtons() {
        selectAllButton.setOnClickListener {
            selectAllItems()
        }
        
        clearAllButton.setOnClickListener {
            clearAllItems()
        }
    }
    
    private fun selectAllItems() {
        selectedItems.clear()
        for (i in dataList.indices) {
            selectedItems.add(i)
            listView.setItemChecked(i, true)
        }
        updateSelectedCount()
    }
    
    private fun clearAllItems() {
        selectedItems.clear()
        for (i in dataList.indices) {
            listView.setItemChecked(i, false)
        }
        updateSelectedCount()
    }
    
    private fun updateSelectedCount() {
        selectedCountText.text = "已选择: ${selectedItems.size} 项"
    }
}
```

## 实际应用场景

### 1. 设置列表

```kotlin
class SettingsListActivity : AppCompatActivity() {
    
    private lateinit var listView: ListView
    private lateinit var adapter: ArrayAdapter<String>
    
    private val settingsItems = listOf(
        "账户设置",
        "隐私设置",
        "通知设置",
        "语言设置",
        "主题设置",
        "存储设置",
        "关于应用",
        "帮助与反馈"
    )
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_settings_list)
        
        initViews()
        setupAdapter()
        setupListView()
    }
    
    private fun initViews() {
        listView = findViewById(R.id.listView)
    }
    
    private fun setupAdapter() {
        adapter = ArrayAdapter(
            this,
            R.layout.settings_list_item,
            R.id.settingText,
            settingsItems
        )
    }
    
    private fun setupListView() {
        listView.adapter = adapter
        
        listView.onItemClickListener = AdapterView.OnItemClickListener { _, _, position, _ ->
            val settingItem = settingsItems[position]
            openSettingDetail(settingItem)
        }
    }
    
    private fun openSettingDetail(setting: String) {
        Toast.makeText(this, "打开: $setting", Toast.LENGTH_SHORT).show()
        // 根据设置项打开对应的设置页面
    }
}
```

### 2. 历史记录列表

```kotlin
class HistoryListActivity : AppCompatActivity() {
    
    private lateinit var listView: ListView
    private lateinit var adapter: ArrayAdapter<String>
    private lateinit var clearHistoryButton: Button
    
    private val historyList = mutableListOf<String>()
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_history_list)
        
        initViews()
        loadHistory()
        setupAdapter()
        setupListView()
        setupClearButton()
    }
    
    private fun initViews() {
        listView = findViewById(R.id.listView)
        clearHistoryButton = findViewById(R.id.clearHistoryButton)
    }
    
    private fun loadHistory() {
        // 模拟加载历史记录
        historyList.addAll(listOf(
            "Android开发教程",
            "Kotlin基础语法",
            "Java集合框架",
            "移动端UI设计",
            "数据库操作"
        ))
    }
    
    private fun setupAdapter() {
        adapter = ArrayAdapter(
            this,
            R.layout.history_list_item,
            R.id.historyText,
            historyList
        )
    }
    
    private fun setupListView() {
        listView.adapter = adapter
        
        listView.onItemClickListener = AdapterView.OnItemClickListener { _, _, position, _ ->
            val historyItem = historyList[position]
            openHistoryItem(historyItem)
        }
        
        listView.onItemLongClickListener = AdapterView.OnItemLongClickListener { _, _, position, _ ->
            showHistoryOptions(position)
            true
        }
    }
    
    private fun setupClearButton() {
        clearHistoryButton.setOnClickListener {
            clearHistory()
        }
    }
    
    private fun openHistoryItem(item: String) {
        Toast.makeText(this, "打开: $item", Toast.LENGTH_SHORT).show()
        // 打开历史记录项
    }
    
    private fun showHistoryOptions(position: Int) {
        val item = historyList[position]
        AlertDialog.Builder(this)
            .setTitle("历史记录选项")
            .setMessage("对 '$item' 执行什么操作？")
            .setPositiveButton("删除") { _, _ ->
                removeHistoryItem(position)
            }
            .setNegativeButton("取消") { _, _ ->
                // 什么都不做
            }
            .show()
    }
    
    private fun removeHistoryItem(position: Int) {
        historyList.removeAt(position)
        adapter.notifyDataSetChanged()
        Toast.makeText(this, "已删除", Toast.LENGTH_SHORT).show()
    }
    
    private fun clearHistory() {
        AlertDialog.Builder(this)
            .setTitle("清除历史记录")
            .setMessage("确定要清除所有历史记录吗？")
            .setPositiveButton("确定") { _, _ ->
                historyList.clear()
                adapter.notifyDataSetChanged()
                Toast.makeText(this, "已清除所有历史记录", Toast.LENGTH_SHORT).show()
            }
            .setNegativeButton("取消") { _, _ ->
                // 什么都不做
            }
            .show()
    }
}
```

## ArrayAdapter 最佳实践

### 1. 适配器工具类

```kotlin
object ArrayAdapterUtils {
    
    fun createSimpleAdapter(
        context: Context,
        data: List<String>
    ): ArrayAdapter<String> {
        return ArrayAdapter(
            context,
            android.R.layout.simple_list_item_1,
            android.R.id.text1,
            data
        )
    }
    
    fun createCustomAdapter(
        context: Context,
        layoutRes: Int,
        textViewResId: Int,
        data: List<String>
    ): ArrayAdapter<String> {
        return ArrayAdapter(
            context,
            layoutRes,
            textViewResId,
            data
        )
    }
    
    fun createFilterableAdapter(
        context: Context,
        data: List<String>
    ): ArrayAdapter<String> {
        return object : ArrayAdapter<String>(
            context,
            android.R.layout.simple_list_item_1,
            android.R.id.text1,
            data
        ) {
            override fun getFilter(): Filter {
                return object : Filter() {
                    override fun performFiltering(constraint: CharSequence?): FilterResults {
                        val results = FilterResults()
                        val filteredList = mutableListOf<String>()
                        
                        if (constraint.isNullOrEmpty()) {
                            filteredList.addAll(data)
                        } else {
                            data.forEach { item ->
                                if (item.contains(constraint, ignoreCase = true)) {
                                    filteredList.add(item)
                                }
                            }
                        }
                        
                        results.values = filteredList
                        results.count = filteredList.size
                        return results
                    }
                    
                    override fun publishResults(constraint: CharSequence?, results: FilterResults?) {
                        clear()
                        if (results != null) {
                            addAll(results.values as List<String>)
                            notifyDataSetChanged()
                        }
                    }
                }
            }
        }
    }
}
```

### 2. 适配器管理类

```kotlin
class AdapterManager<T> {
    
    private var adapter: ArrayAdapter<T>? = null
    private var dataList = mutableListOf<T>()
    
    fun createAdapter(
        context: Context,
        layoutRes: Int,
        textViewResId: Int
    ): ArrayAdapter<T> {
        adapter = ArrayAdapter(context, layoutRes, textViewResId, dataList)
        return adapter!!
    }
    
    fun addItem(item: T) {
        dataList.add(item)
        adapter?.notifyDataSetChanged()
    }
    
    fun removeItem(position: Int) {
        if (position in 0 until dataList.size) {
            dataList.removeAt(position)
            adapter?.notifyDataSetChanged()
        }
    }
    
    fun updateItem(position: Int, item: T) {
        if (position in 0 until dataList.size) {
            dataList[position] = item
            adapter?.notifyDataSetChanged()
        }
    }
    
    fun clearAll() {
        dataList.clear()
        adapter?.notifyDataSetChanged()
    }
    
    fun getItem(position: Int): T? {
        return if (position in 0 until dataList.size) dataList[position] else null
    }
    
    fun getItemCount(): Int = dataList.size
}
```

## 📋 总结

ArrayAdapter 是 Android 开发中最简单的适配器：

- **基本用法**：简单的文本列表显示
- **自定义布局**：支持自定义列表项布局
- **过滤功能**：支持数据过滤和搜索
- **多选功能**：支持多选列表
- **实际应用**：设置列表、历史记录、简单菜单等场景
- **最佳实践**：工具类封装、适配器管理

掌握 ArrayAdapter 的使用方法对于创建简单的列表界面至关重要。 
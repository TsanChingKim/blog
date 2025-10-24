---
title: Menu 菜单组件
date: 2025-10-24
categories: ["Android"]
robots: all
summary: 详细介绍Android Menu菜单组件的使用方法，包括OptionMenu、ContextMenu和PopupMenu
featureimage: images/android/12.jpg
---

# Menu 菜单组件

Android 提供了多种菜单组件，用于不同的用户交互场景。本文将详细介绍各种菜单的使用方法。

## OptionMenu 选项菜单

OptionMenu 是应用的主菜单，通常显示在 ActionBar 或标题栏中，用于放置对应用产生全局影响的操作。

### 基本属性

| 属性 | 说明 | 示例值 |
|------|------|--------|
| `android:id` | 菜单项ID | `@+id/menu_item` |
| `android:title` | 菜单项标题 | `"设置"` |
| `android:icon` | 菜单项图标 | `@drawable/ic_settings` |
| `android:showAsAction` | 显示方式 | `always`, `never`, `ifRoom` |

### 创建菜单资源

```xml
<!-- res/menu/main_menu.xml -->
<menu xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto">
    
    <item
        android:id="@+id/menu_settings"
        android:title="设置"
        android:icon="@drawable/ic_settings"
        app:showAsAction="ifRoom" />
    
    <item
        android:id="@+id/menu_help"
        android:title="帮助"
        android:icon="@drawable/ic_help"
        app:showAsAction="never" />
    
    <item
        android:id="@+id/menu_about"
        android:title="关于"
        android:icon="@drawable/ic_info"
        app:showAsAction="never" />
    
</menu>
```

### Kotlin 代码示例

```kotlin
class OptionMenuActivity : AppCompatActivity() {
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_option_menu)
        
        // 设置 ActionBar
        setSupportActionBar(findViewById(R.id.toolbar))
    }
    
    override fun onCreateOptionsMenu(menu: Menu?): Boolean {
        menuInflater.inflate(R.menu.main_menu, menu)
        return true
    }
    
    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        return when (item.itemId) {
            R.id.menu_settings -> {
                openSettings()
                true
            }
            R.id.menu_help -> {
                showHelp()
                true
            }
            R.id.menu_about -> {
                showAbout()
                true
            }
            else -> super.onOptionsItemSelected(item)
        }
    }
    
    private fun openSettings() {
        Toast.makeText(this, "打开设置", Toast.LENGTH_SHORT).show()
        // 启动设置页面
        // startActivity(Intent(this, SettingsActivity::class.java))
    }
    
    private fun showHelp() {
        Toast.makeText(this, "显示帮助", Toast.LENGTH_SHORT).show()
        // 显示帮助对话框
    }
    
    private fun showAbout() {
        Toast.makeText(this, "显示关于", Toast.LENGTH_SHORT).show()
        // 显示关于对话框
    }
}
```

### 动态创建菜单

```kotlin
class DynamicOptionMenuActivity : AppCompatActivity() {
    
    private val menuItems = mutableListOf("菜单项1", "菜单项2", "菜单项3")
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_dynamic_option_menu)
        
        setSupportActionBar(findViewById(R.id.toolbar))
    }
    
    override fun onCreateOptionsMenu(menu: Menu?): Boolean {
        menu?.let {
            // 动态添加菜单项
            menuItems.forEachIndexed { index, title ->
                it.add(Menu.NONE, index, Menu.NONE, title)
            }
            
            // 添加分隔符
            it.add(Menu.NONE, Menu.NONE, Menu.NONE, "分隔符")
                .setEnabled(false)
            
            // 添加更多菜单项
            it.add(Menu.NONE, 999, Menu.NONE, "更多选项")
        }
        return true
    }
    
    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        return when (item.itemId) {
            in 0 until menuItems.size -> {
                Toast.makeText(this, "选择了: ${menuItems[item.itemId]}", Toast.LENGTH_SHORT).show()
                true
            }
            999 -> {
                Toast.makeText(this, "更多选项", Toast.LENGTH_SHORT).show()
                true
            }
            else -> super.onOptionsItemSelected(item)
        }
    }
}
```

## ContextMenu 上下文菜单

ContextMenu 是长按某个 View 时弹出的菜单，提供与该 View 相关的操作选项。

### 基本使用

```kotlin
class ContextMenuActivity : AppCompatActivity() {
    
    private lateinit var textView: TextView
    private lateinit var imageView: ImageView
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_context_menu)
        
        initViews()
        registerContextMenus()
    }
    
    private fun initViews() {
        textView = findViewById(R.id.textView)
        imageView = findViewById(R.id.imageView)
    }
    
    private fun registerContextMenus() {
        // 注册上下文菜单
        registerForContextMenu(textView)
        registerForContextMenu(imageView)
    }
    
    override fun onCreateContextMenu(
        menu: ContextMenu?,
        v: View?,
        menuInfo: ContextMenu.ContextMenuInfo?
    ) {
        super.onCreateContextMenu(menu, v, menuInfo)
        
        when (v?.id) {
            R.id.textView -> {
                menuInflater.inflate(R.menu.text_context_menu, menu)
            }
            R.id.imageView -> {
                menuInflater.inflate(R.menu.image_context_menu, menu)
            }
        }
    }
    
    override fun onContextItemSelected(item: MenuItem): Boolean {
        return when (item.itemId) {
            R.id.menu_copy -> {
                copyText()
                true
            }
            R.id.menu_paste -> {
                pasteText()
                true
            }
            R.id.menu_share -> {
                shareContent()
                true
            }
            R.id.menu_delete -> {
                deleteItem()
                true
            }
            R.id.menu_edit -> {
                editItem()
                true
            }
            else -> super.onContextItemSelected(item)
        }
    }
    
    private fun copyText() {
        Toast.makeText(this, "复制文本", Toast.LENGTH_SHORT).show()
    }
    
    private fun pasteText() {
        Toast.makeText(this, "粘贴文本", Toast.LENGTH_SHORT).show()
    }
    
    private fun shareContent() {
        Toast.makeText(this, "分享内容", Toast.LENGTH_SHORT).show()
    }
    
    private fun deleteItem() {
        Toast.makeText(this, "删除项目", Toast.LENGTH_SHORT).show()
    }
    
    private fun editItem() {
        Toast.makeText(this, "编辑项目", Toast.LENGTH_SHORT).show()
    }
}
```

### 上下文菜单资源

```xml
<!-- res/menu/text_context_menu.xml -->
<menu xmlns:android="http://schemas.android.com/apk/res/android">
    
    <item
        android:id="@+id/menu_copy"
        android:title="复制"
        android:icon="@drawable/ic_copy" />
    
    <item
        android:id="@+id/menu_paste"
        android:title="粘贴"
        android:icon="@drawable/ic_paste" />
    
    <item
        android:id="@+id/menu_share"
        android:title="分享"
        android:icon="@drawable/ic_share" />
    
</menu>

<!-- res/menu/image_context_menu.xml -->
<menu xmlns:android="http://schemas.android.com/apk/res/android">
    
    <item
        android:id="@+id/menu_share"
        android:title="分享"
        android:icon="@drawable/ic_share" />
    
    <item
        android:id="@+id/menu_delete"
        android:title="删除"
        android:icon="@drawable/ic_delete" />
    
    <item
        android:id="@+id/menu_edit"
        android:title="编辑"
        android:icon="@drawable/ic_edit" />
    
</menu>
```

## PopupMenu 弹出菜单

PopupMenu 是模态形式的弹出菜单，通常绑定在某个 View 上，出现在被绑定 View 的下方。

### 基本使用

```kotlin
class PopupMenuActivity : AppCompatActivity() {
    
    private lateinit var showMenuButton: Button
    private lateinit var anchorView: View
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_popup_menu)
        
        initViews()
        setupPopupMenu()
    }
    
    private fun initViews() {
        showMenuButton = findViewById(R.id.showMenuButton)
        anchorView = findViewById(R.id.anchorView)
    }
    
    private fun setupPopupMenu() {
        showMenuButton.setOnClickListener {
            showPopupMenu(it)
        }
        
        anchorView.setOnClickListener {
            showPopupMenu(it)
        }
    }
    
    private fun showPopupMenu(anchor: View) {
        val popupMenu = PopupMenu(this, anchor)
        popupMenu.menuInflater.inflate(R.menu.popup_menu, popupMenu.menu)
        
        // 设置菜单项点击监听器
        popupMenu.setOnMenuItemClickListener { item ->
            handlePopupMenuItemClick(item)
            true
        }
        
        // 设置菜单关闭监听器
        popupMenu.setOnDismissListener {
            Toast.makeText(this, "菜单已关闭", Toast.LENGTH_SHORT).show()
        }
        
        popupMenu.show()
    }
    
    private fun handlePopupMenuItemClick(item: MenuItem): Boolean {
        return when (item.itemId) {
            R.id.menu_item1 -> {
                Toast.makeText(this, "选择了菜单项1", Toast.LENGTH_SHORT).show()
                true
            }
            R.id.menu_item2 -> {
                Toast.makeText(this, "选择了菜单项2", Toast.LENGTH_SHORT).show()
                true
            }
            R.id.menu_item3 -> {
                Toast.makeText(this, "选择了菜单项3", Toast.LENGTH_SHORT).show()
                true
            }
            else -> false
        }
    }
}
```

### 动态创建 PopupMenu

```kotlin
class DynamicPopupMenuActivity : AppCompatActivity() {
    
    private lateinit var showMenuButton: Button
    private val menuItems = mutableListOf("动态菜单1", "动态菜单2", "动态菜单3")
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_dynamic_popup_menu)
        
        initViews()
        setupDynamicPopupMenu()
    }
    
    private fun initViews() {
        showMenuButton = findViewById(R.id.showMenuButton)
    }
    
    private fun setupDynamicPopupMenu() {
        showMenuButton.setOnClickListener {
            showDynamicPopupMenu(it)
        }
    }
    
    private fun showDynamicPopupMenu(anchor: View) {
        val popupMenu = PopupMenu(this, anchor)
        
        // 动态添加菜单项
        menuItems.forEachIndexed { index, title ->
            popupMenu.menu.add(Menu.NONE, index, Menu.NONE, title)
        }
        
        // 添加分隔符
        popupMenu.menu.add(Menu.NONE, Menu.NONE, Menu.NONE, "分隔符")
            .setEnabled(false)
        
        // 添加更多选项
        popupMenu.menu.add(Menu.NONE, 999, Menu.NONE, "添加新项")
        
        popupMenu.setOnMenuItemClickListener { item ->
            when (item.itemId) {
                in 0 until menuItems.size -> {
                    Toast.makeText(this, "选择了: ${menuItems[item.itemId]}", Toast.LENGTH_SHORT).show()
                    true
                }
                999 -> {
                    addNewMenuItem()
                    true
                }
                else -> false
            }
        }
        
        popupMenu.show()
    }
    
    private fun addNewMenuItem() {
        val newItem = "动态菜单${menuItems.size + 1}"
        menuItems.add(newItem)
        Toast.makeText(this, "添加了新菜单项: $newItem", Toast.LENGTH_SHORT).show()
    }
}
```

### PopupMenu 资源文件

```xml
<!-- res/menu/popup_menu.xml -->
<menu xmlns:android="http://schemas.android.com/apk/res/android">
    
    <item
        android:id="@+id/menu_item1"
        android:title="菜单项1"
        android:icon="@drawable/ic_item1" />
    
    <item
        android:id="@+id/menu_item2"
        android:title="菜单项2"
        android:icon="@drawable/ic_item2" />
    
    <item
        android:id="@+id/menu_item3"
        android:title="菜单项3"
        android:icon="@drawable/ic_item3" />
    
</menu>
```

## 实际应用场景

### 1. 列表项操作菜单

```kotlin
class ListItemMenuActivity : AppCompatActivity() {
    
    private lateinit var recyclerView: RecyclerView
    private lateinit var adapter: ItemAdapter
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_list_item_menu)
        
        initViews()
        setupRecyclerView()
    }
    
    private fun initViews() {
        recyclerView = findViewById(R.id.recyclerView)
    }
    
    private fun setupRecyclerView() {
        val items = listOf("项目1", "项目2", "项目3", "项目4", "项目5")
        adapter = ItemAdapter(items) { item, view ->
            showItemMenu(item, view)
        }
        recyclerView.adapter = adapter
        recyclerView.layoutManager = LinearLayoutManager(this)
    }
    
    private fun showItemMenu(item: String, anchorView: View) {
        val popupMenu = PopupMenu(this, anchorView)
        popupMenu.menuInflater.inflate(R.menu.list_item_menu, popupMenu.menu)
        
        popupMenu.setOnMenuItemClickListener { menuItem ->
            when (menuItem.itemId) {
                R.id.menu_edit -> {
                    editItem(item)
                    true
                }
                R.id.menu_delete -> {
                    deleteItem(item)
                    true
                }
                R.id.menu_share -> {
                    shareItem(item)
                    true
                }
                else -> false
            }
        }
        
        popupMenu.show()
    }
    
    private fun editItem(item: String) {
        Toast.makeText(this, "编辑: $item", Toast.LENGTH_SHORT).show()
    }
    
    private fun deleteItem(item: String) {
        Toast.makeText(this, "删除: $item", Toast.LENGTH_SHORT).show()
    }
    
    private fun shareItem(item: String) {
        Toast.makeText(this, "分享: $item", Toast.LENGTH_SHORT).show()
    }
}

class ItemAdapter(
    private val items: List<String>,
    private val onItemClick: (String, View) -> Unit
) : RecyclerView.Adapter<ItemAdapter.ViewHolder>() {
    
    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        val view = LayoutInflater.from(parent.context)
            .inflate(R.layout.item_list, parent, false)
        return ViewHolder(view)
    }
    
    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        holder.bind(items[position])
    }
    
    override fun getItemCount(): Int = items.size
    
    inner class ViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        private val textView: TextView = itemView.findViewById(R.id.textView)
        private val menuButton: Button = itemView.findViewById(R.id.menuButton)
        
        fun bind(item: String) {
            textView.text = item
            menuButton.setOnClickListener {
                onItemClick(item, it)
            }
        }
    }
}
```

### 2. 工具栏菜单

```kotlin
class ToolbarMenuActivity : AppCompatActivity() {
    
    private lateinit var toolbar: Toolbar
    private lateinit var searchView: SearchView
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_toolbar_menu)
        
        initViews()
        setupToolbar()
    }
    
    private fun initViews() {
        toolbar = findViewById(R.id.toolbar)
    }
    
    private fun setupToolbar() {
        setSupportActionBar(toolbar)
        supportActionBar?.setDisplayHomeAsUpEnabled(true)
    }
    
    override fun onCreateOptionsMenu(menu: Menu?): Boolean {
        menuInflater.inflate(R.menu.toolbar_menu, menu)
        
        // 设置搜索视图
        val searchItem = menu?.findItem(R.id.menu_search)
        searchView = searchItem?.actionView as SearchView
        
        searchView.setOnQueryTextListener(object : SearchView.OnQueryTextListener {
            override fun onQueryTextSubmit(query: String?): Boolean {
                performSearch(query)
                return true
            }
            
            override fun onQueryTextChange(newText: String?): Boolean {
                // 实时搜索
                return true
            }
        })
        
        return true
    }
    
    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        return when (item.itemId) {
            android.R.id.home -> {
                onBackPressed()
                true
            }
            R.id.menu_search -> {
                searchView.isIconified = false
                true
            }
            R.id.menu_filter -> {
                showFilterDialog()
                true
            }
            R.id.menu_sort -> {
                showSortDialog()
                true
            }
            else -> super.onOptionsItemSelected(item)
        }
    }
    
    private fun performSearch(query: String?) {
        Toast.makeText(this, "搜索: $query", Toast.LENGTH_SHORT).show()
    }
    
    private fun showFilterDialog() {
        Toast.makeText(this, "显示筛选对话框", Toast.LENGTH_SHORT).show()
    }
    
    private fun showSortDialog() {
        Toast.makeText(this, "显示排序对话框", Toast.LENGTH_SHORT).show()
    }
}
```

### 3. 工具栏菜单资源

```xml
<!-- res/menu/toolbar_menu.xml -->
<menu xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto">
    
    <item
        android:id="@+id/menu_search"
        android:title="搜索"
        android:icon="@drawable/ic_search"
        app:actionViewClass="androidx.appcompat.widget.SearchView"
        app:showAsAction="ifRoom" />
    
    <item
        android:id="@+id/menu_filter"
        android:title="筛选"
        android:icon="@drawable/ic_filter"
        app:showAsAction="ifRoom" />
    
    <item
        android:id="@+id/menu_sort"
        android:title="排序"
        android:icon="@drawable/ic_sort"
        app:showAsAction="never" />
    
</menu>
```

## 菜单最佳实践

### 1. 菜单项分组

```xml
<menu xmlns:android="http://schemas.android.com/apk/res/android">
    
    <group android:id="@+id/group_main">
        <item
            android:id="@+id/menu_home"
            android:title="首页"
            android:icon="@drawable/ic_home" />
        
        <item
            android:id="@+id/menu_profile"
            android:title="个人资料"
            android:icon="@drawable/ic_profile" />
    </group>
    
    <group android:id="@+id/group_settings">
        <item
            android:id="@+id/menu_settings"
            android:title="设置"
            android:icon="@drawable/ic_settings" />
        
        <item
            android:id="@+id/menu_help"
            android:title="帮助"
            android:icon="@drawable/ic_help" />
    </group>
    
</menu>
```

### 2. 菜单项状态管理

```kotlin
class MenuStateActivity : AppCompatActivity() {
    
    private var isEditMode = false
    
    override fun onCreateOptionsMenu(menu: Menu?): Boolean {
        menuInflater.inflate(R.menu.state_menu, menu)
        updateMenuState(menu)
        return true
    }
    
    private fun updateMenuState(menu: Menu?) {
        menu?.let {
            val editItem = it.findItem(R.id.menu_edit)
            val saveItem = it.findItem(R.id.menu_save)
            val cancelItem = it.findItem(R.id.menu_cancel)
            
            editItem?.isVisible = !isEditMode
            saveItem?.isVisible = isEditMode
            cancelItem?.isVisible = isEditMode
        }
    }
    
    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        return when (item.itemId) {
            R.id.menu_edit -> {
                enterEditMode()
                true
            }
            R.id.menu_save -> {
                saveChanges()
                true
            }
            R.id.menu_cancel -> {
                cancelEdit()
                true
            }
            else -> super.onOptionsItemSelected(item)
        }
    }
    
    private fun enterEditMode() {
        isEditMode = true
        invalidateOptionsMenu()
        Toast.makeText(this, "进入编辑模式", Toast.LENGTH_SHORT).show()
    }
    
    private fun saveChanges() {
        isEditMode = false
        invalidateOptionsMenu()
        Toast.makeText(this, "保存更改", Toast.LENGTH_SHORT).show()
    }
    
    private fun cancelEdit() {
        isEditMode = false
        invalidateOptionsMenu()
        Toast.makeText(this, "取消编辑", Toast.LENGTH_SHORT).show()
    }
}
```

## 📋 总结

Android Menu 组件提供了丰富的菜单交互方式：

- **OptionMenu**：主菜单，显示在 ActionBar 中
- **ContextMenu**：上下文菜单，长按触发
- **PopupMenu**：弹出菜单，绑定到特定 View
- **动态创建**：支持程序动态添加菜单项
- **状态管理**：支持菜单项状态切换和分组

掌握这些菜单组件的使用方法对于创建良好的用户交互体验至关重要。



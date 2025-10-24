---
title: BaseAdapter 基础单一元素
date: 2025-10-24
categories: ["Android"]
robots: all
summary: 详细介绍Android BaseAdapter的使用方法、自定义实现和ViewHolder模式
featureimage: images/android/18.jpg
---

# BaseAdapter 基础单一元素

BaseAdapter 是 Android 中所有适配器的基类，提供了最大的灵活性，可以完全自定义列表项的显示和交互。

## BaseAdapter 基本概念

BaseAdapter 是所有适配器的抽象基类，与 SimpleAdapter 的区别在于可以完全自定义每个列表项的内容和样式。它提供了最大的灵活性，但需要更多的代码实现。

### 核心方法

| 方法 | 说明 | 返回值 |
|------|------|--------|
| `getCount()` | 返回数据项数量 | `Int` |
| `getItem(position)` | 返回指定位置的数据项 | `Any?` |
| `getItemId(position)` | 返回指定位置的数据项ID | `Long` |
| `getView(position, convertView, parent)` | 创建或复用列表项视图 | `View` |

## 基本使用示例

### 1. 简单BaseAdapter实现

```kotlin
class BaseAdapterActivity : AppCompatActivity() {
    
    private lateinit var listView: ListView
    private lateinit var adapter: CustomBaseAdapter
    
    private val dataList = mutableListOf<String>()
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_base_adapter)
        
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
            "Android开发",
            "Kotlin编程",
            "Java基础",
            "移动开发",
            "UI设计",
            "数据库",
            "网络编程",
            "算法"
        ))
    }
    
    private fun setupAdapter() {
        adapter = CustomBaseAdapter(this, dataList)
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
    
    private fun removeItem(position: Int) {
        dataList.removeAt(position)
        adapter.notifyDataSetChanged()
        Toast.makeText(this, "已删除", Toast.LENGTH_SHORT).show()
    }
}

class CustomBaseAdapter(
    private val context: Context,
    private val dataList: MutableList<String>
) : BaseAdapter() {
    
    override fun getCount(): Int = dataList.size
    
    override fun getItem(position: Int): Any? = dataList[position]
    
    override fun getItemId(position: Int): Long = position.toLong()
    
    override fun getView(position: Int, convertView: View?, parent: ViewGroup?): View {
        val view: View
        val holder: ViewHolder
        
        if (convertView == null) {
            view = LayoutInflater.from(context).inflate(R.layout.base_adapter_item, parent, false)
            holder = ViewHolder(view)
            view.tag = holder
        } else {
            view = convertView
            holder = view.tag as ViewHolder
        }
        
        val item = dataList[position]
        holder.titleText.text = item
        holder.subtitleText.text = "这是第 ${position + 1} 个项目"
        
        // 根据位置设置不同的背景色
        when (position % 3) {
            0 -> holder.container.setBackgroundColor(ContextCompat.getColor(context, R.color.colorPrimary))
            1 -> holder.container.setBackgroundColor(ContextCompat.getColor(context, R.color.colorAccent))
            2 -> holder.container.setBackgroundColor(ContextCompat.getColor(context, R.color.colorSecondary))
        }
        
        return view
    }
    
    private class ViewHolder(view: View) {
        val container: LinearLayout = view.findViewById(R.id.container)
        val titleText: TextView = view.findViewById(R.id.titleText)
        val subtitleText: TextView = view.findViewById(R.id.subtitleText)
    }
}
```

### 2. 自定义布局文件

```xml
<!-- res/layout/base_adapter_item.xml -->
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:id="@+id/container"
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
            android:textColor="@android:color/white" />
        
        <TextView
            android:id="@+id/subtitleText"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:textSize="14sp"
            android:textColor="@android:color/white"
            android:alpha="0.8"
            android:layout_marginTop="4dp" />
        
    </LinearLayout>
    
    <ImageView
        android:id="@+id/arrowImage"
        android:layout_width="24dp"
        android:layout_height="24dp"
        android:src="@drawable/ic_arrow_right"
        android:layout_gravity="center_vertical"
        android:tint="@android:color/white" />
    
</LinearLayout>
```

### 3. 复杂数据模型BaseAdapter

```kotlin
class ComplexBaseAdapterActivity : AppCompatActivity() {
    
    private lateinit var listView: ListView
    private lateinit var adapter: ComplexBaseAdapter
    
    private val dataList = mutableListOf<ContactItem>()
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_complex_base_adapter)
        
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
            ContactItem("张三", "13800138000", "zhangsan@example.com", true),
            ContactItem("李四", "13800138001", "lisi@example.com", false),
            ContactItem("王五", "13800138002", "wangwu@example.com", true),
            ContactItem("赵六", "13800138003", "zhaoliu@example.com", false),
            ContactItem("钱七", "13800138004", "qianqi@example.com", true)
        ))
    }
    
    private fun setupAdapter() {
        adapter = ComplexBaseAdapter(this, dataList)
    }
    
    private fun setupListView() {
        listView.adapter = adapter
        
        listView.onItemClickListener = AdapterView.OnItemClickListener { _, _, position, _ ->
            val contact = dataList[position]
            showContactDetail(contact)
        }
    }
    
    private fun showContactDetail(contact: ContactItem) {
        AlertDialog.Builder(this)
            .setTitle("联系人详情")
            .setMessage("姓名: ${contact.name}\n电话: ${contact.phone}\n邮箱: ${contact.email}\n状态: ${if (contact.isOnline) "在线" else "离线"}")
            .setPositiveButton("确定") { _, _ ->
                // 什么都不做
            }
            .show()
    }
}

data class ContactItem(
    val name: String,
    val phone: String,
    val email: String,
    val isOnline: Boolean
)

class ComplexBaseAdapter(
    private val context: Context,
    private val dataList: MutableList<ContactItem>
) : BaseAdapter() {
    
    override fun getCount(): Int = dataList.size
    
    override fun getItem(position: Int): ContactItem = dataList[position]
    
    override fun getItemId(position: Int): Long = position.toLong()
    
    override fun getView(position: Int, convertView: View?, parent: ViewGroup?): View {
        val view: View
        val holder: ContactViewHolder
        
        if (convertView == null) {
            view = LayoutInflater.from(context).inflate(R.layout.contact_item, parent, false)
            holder = ContactViewHolder(view)
            view.tag = holder
        } else {
            view = convertView
            holder = view.tag as ContactViewHolder
        }
        
        val contact = dataList[position]
        
        holder.nameText.text = contact.name
        holder.phoneText.text = contact.phone
        holder.emailText.text = contact.email
        
        // 设置在线状态
        if (contact.isOnline) {
            holder.statusIndicator.setBackgroundColor(ContextCompat.getColor(context, R.color.online_color))
            holder.statusText.text = "在线"
            holder.statusText.setTextColor(ContextCompat.getColor(context, R.color.online_color))
        } else {
            holder.statusIndicator.setBackgroundColor(ContextCompat.getColor(context, R.color.offline_color))
            holder.statusText.text = "离线"
            holder.statusText.setTextColor(ContextCompat.getColor(context, R.color.offline_color))
        }
        
        // 设置头像
        holder.avatarImage.setImageResource(
            when (position % 4) {
                0 -> android.R.drawable.ic_menu_myplaces
                1 -> android.R.drawable.ic_menu_camera
                2 -> android.R.drawable.ic_menu_send
                else -> android.R.drawable.ic_menu_share
            }
        )
        
        return view
    }
    
    private class ContactViewHolder(view: View) {
        val container: LinearLayout = view.findViewById(R.id.container)
        val avatarImage: ImageView = view.findViewById(R.id.avatarImage)
        val nameText: TextView = view.findViewById(R.id.nameText)
        val phoneText: TextView = view.findViewById(R.id.phoneText)
        val emailText: TextView = view.findViewById(R.id.emailText)
        val statusIndicator: View = view.findViewById(R.id.statusIndicator)
        val statusText: TextView = view.findViewById(R.id.statusText)
    }
}
```

### 4. 复杂布局文件

```xml
<!-- res/layout/contact_item.xml -->
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:id="@+id/container"
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
            
            <View
                android:id="@+id/statusIndicator"
                android:layout_width="12dp"
                android:layout_height="12dp"
                android:layout_marginEnd="8dp"
                android:background="@drawable/circle_background" />
            
            <TextView
                android:id="@+id/statusText"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:textSize="12sp" />
            
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
        
    </LinearLayout>
    
</LinearLayout>
```

## 高级用法示例

### 1. 多类型列表项

```kotlin
class MultiTypeBaseAdapterActivity : AppCompatActivity() {
    
    private lateinit var listView: ListView
    private lateinit var adapter: MultiTypeBaseAdapter
    
    private val dataList = mutableListOf<Any>()
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_multi_type_base_adapter)
        
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
            HeaderItem("联系人"),
            ContactItem("张三", "13800138000", "zhangsan@example.com", true),
            ContactItem("李四", "13800138001", "lisi@example.com", false),
            HeaderItem("群组"),
            GroupItem("工作群", "5人", "最新消息：明天开会"),
            GroupItem("朋友群", "8人", "最新消息：周末聚餐"),
            HeaderItem("最近聊天"),
            RecentChatItem("王五", "你好，最近怎么样？", "10:30", 2),
            RecentChatItem("赵六", "好的，没问题", "09:15", 0)
        ))
    }
    
    private fun setupAdapter() {
        adapter = MultiTypeBaseAdapter(this, dataList)
    }
    
    private fun setupListView() {
        listView.adapter = adapter
        
        listView.onItemClickListener = AdapterView.OnItemClickListener { _, _, position, _ ->
            val item = dataList[position]
            when (item) {
                is ContactItem -> showContactDetail(item)
                is GroupItem -> showGroupDetail(item)
                is RecentChatItem -> showChatDetail(item)
                else -> Toast.makeText(this, "点击了标题", Toast.LENGTH_SHORT).show()
            }
        }
    }
    
    private fun showContactDetail(contact: ContactItem) {
        Toast.makeText(this, "联系人: ${contact.name}", Toast.LENGTH_SHORT).show()
    }
    
    private fun showGroupDetail(group: GroupItem) {
        Toast.makeText(this, "群组: ${group.name}", Toast.LENGTH_SHORT).show()
    }
    
    private fun showChatDetail(chat: RecentChatItem) {
        Toast.makeText(this, "聊天: ${chat.name}", Toast.LENGTH_SHORT).show()
    }
}

data class HeaderItem(val title: String)
data class GroupItem(val name: String, val memberCount: String, val lastMessage: String)
data class RecentChatItem(val name: String, val lastMessage: String, val time: String, val unreadCount: Int)

class MultiTypeBaseAdapter(
    private val context: Context,
    private val dataList: MutableList<Any>
) : BaseAdapter() {
    
    companion object {
        private const val TYPE_HEADER = 0
        private const val TYPE_CONTACT = 1
        private const val TYPE_GROUP = 2
        private const val TYPE_RECENT_CHAT = 3
    }
    
    override fun getCount(): Int = dataList.size
    
    override fun getItem(position: Int): Any = dataList[position]
    
    override fun getItemId(position: Int): Long = position.toLong()
    
    override fun getViewTypeCount(): Int = 4
    
    override fun getItemViewType(position: Int): Int {
        return when (dataList[position]) {
            is HeaderItem -> TYPE_HEADER
            is ContactItem -> TYPE_CONTACT
            is GroupItem -> TYPE_GROUP
            is RecentChatItem -> TYPE_RECENT_CHAT
            else -> TYPE_HEADER
        }
    }
    
    override fun getView(position: Int, convertView: View?, parent: ViewGroup?): View {
        val item = dataList[position]
        val viewType = getItemViewType(position)
        
        when (viewType) {
            TYPE_HEADER -> {
                val view = convertView ?: LayoutInflater.from(context).inflate(R.layout.header_item, parent, false)
                val holder = view.tag as? HeaderViewHolder ?: HeaderViewHolder(view).also { view.tag = it }
                val header = item as HeaderItem
                holder.titleText.text = header.title
                return view
            }
            TYPE_CONTACT -> {
                val view = convertView ?: LayoutInflater.from(context).inflate(R.layout.contact_item, parent, false)
                val holder = view.tag as? ContactViewHolder ?: ContactViewHolder(view).also { view.tag = it }
                val contact = item as ContactItem
                holder.nameText.text = contact.name
                holder.phoneText.text = contact.phone
                holder.emailText.text = contact.email
                return view
            }
            TYPE_GROUP -> {
                val view = convertView ?: LayoutInflater.from(context).inflate(R.layout.group_item, parent, false)
                val holder = view.tag as? GroupViewHolder ?: GroupViewHolder(view).also { view.tag = it }
                val group = item as GroupItem
                holder.nameText.text = group.name
                holder.memberCountText.text = group.memberCount
                holder.lastMessageText.text = group.lastMessage
                return view
            }
            TYPE_RECENT_CHAT -> {
                val view = convertView ?: LayoutInflater.from(context).inflate(R.layout.recent_chat_item, parent, false)
                val holder = view.tag as? RecentChatViewHolder ?: RecentChatViewHolder(view).also { view.tag = it }
                val chat = item as RecentChatItem
                holder.nameText.text = chat.name
                holder.lastMessageText.text = chat.lastMessage
                holder.timeText.text = chat.time
                holder.unreadCountText.text = if (chat.unreadCount > 0) chat.unreadCount.toString() else ""
                return view
            }
            else -> return convertView ?: View(context)
        }
    }
    
    private class HeaderViewHolder(view: View) {
        val titleText: TextView = view.findViewById(R.id.titleText)
    }
    
    private class ContactViewHolder(view: View) {
        val nameText: TextView = view.findViewById(R.id.nameText)
        val phoneText: TextView = view.findViewById(R.id.phoneText)
        val emailText: TextView = view.findViewById(R.id.emailText)
    }
    
    private class GroupViewHolder(view: View) {
        val nameText: TextView = view.findViewById(R.id.nameText)
        val memberCountText: TextView = view.findViewById(R.id.memberCountText)
        val lastMessageText: TextView = view.findViewById(R.id.lastMessageText)
    }
    
    private class RecentChatViewHolder(view: View) {
        val nameText: TextView = view.findViewById(R.id.nameText)
        val lastMessageText: TextView = view.findViewById(R.id.lastMessageText)
        val timeText: TextView = view.findViewById(R.id.timeText)
        val unreadCountText: TextView = view.findViewById(R.id.unreadCountText)
    }
}
```

### 2. 动态数据更新

```kotlin
class DynamicBaseAdapterActivity : AppCompatActivity() {
    
    private lateinit var listView: ListView
    private lateinit var adapter: DynamicBaseAdapter
    private lateinit var addButton: Button
    private lateinit var refreshButton: Button
    
    private val dataList = mutableListOf<String>()
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_dynamic_base_adapter)
        
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
            "初始项目1",
            "初始项目2",
            "初始项目3"
        ))
    }
    
    private fun setupAdapter() {
        adapter = DynamicBaseAdapter(this, dataList)
    }
    
    private fun setupListView() {
        listView.adapter = adapter
        
        listView.onItemClickListener = AdapterView.OnItemClickListener { _, _, position, _ ->
            val item = dataList[position]
            Toast.makeText(this, "选择了: $item", Toast.LENGTH_SHORT).show()
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
    
    private fun refreshData() {
        dataList.clear()
        setupInitialData()
        
        // 添加一些随机数据
        repeat(5) { index ->
            dataList.add("刷新项目${index + 1}")
        }
        
        adapter.notifyDataSetChanged()
        Toast.makeText(this, "数据已刷新", Toast.LENGTH_SHORT).show()
    }
}

class DynamicBaseAdapter(
    private val context: Context,
    private val dataList: MutableList<String>
) : BaseAdapter() {
    
    override fun getCount(): Int = dataList.size
    
    override fun getItem(position: Int): String = dataList[position]
    
    override fun getItemId(position: Int): Long = position.toLong()
    
    override fun getView(position: Int, convertView: View?, parent: ViewGroup?): View {
        val view: View
        val holder: DynamicViewHolder
        
        if (convertView == null) {
            view = LayoutInflater.from(context).inflate(R.layout.dynamic_item, parent, false)
            holder = DynamicViewHolder(view)
            view.tag = holder
        } else {
            view = convertView
            holder = view.tag as DynamicViewHolder
        }
        
        val item = dataList[position]
        holder.titleText.text = item
        holder.subtitleText.text = "位置: $position, 时间: ${System.currentTimeMillis()}"
        
        // 根据位置设置不同的样式
        when (position % 4) {
            0 -> {
                holder.container.setBackgroundColor(ContextCompat.getColor(context, R.color.colorPrimary))
                holder.titleText.setTextColor(ContextCompat.getColor(context, android.R.color.white))
                holder.subtitleText.setTextColor(ContextCompat.getColor(context, android.R.color.white))
            }
            1 -> {
                holder.container.setBackgroundColor(ContextCompat.getColor(context, R.color.colorAccent))
                holder.titleText.setTextColor(ContextCompat.getColor(context, android.R.color.white))
                holder.subtitleText.setTextColor(ContextCompat.getColor(context, android.R.color.white))
            }
            2 -> {
                holder.container.setBackgroundColor(ContextCompat.getColor(context, R.color.colorSecondary))
                holder.titleText.setTextColor(ContextCompat.getColor(context, android.R.color.white))
                holder.subtitleText.setTextColor(ContextCompat.getColor(context, android.R.color.white))
            }
            else -> {
                holder.container.setBackgroundColor(ContextCompat.getColor(context, android.R.color.white))
                holder.titleText.setTextColor(ContextCompat.getColor(context, android.R.color.black))
                holder.subtitleText.setTextColor(ContextCompat.getColor(context, android.R.color.black))
            }
        }
        
        return view
    }
    
    private class DynamicViewHolder(view: View) {
        val container: LinearLayout = view.findViewById(R.id.container)
        val titleText: TextView = view.findViewById(R.id.titleText)
        val subtitleText: TextView = view.findViewById(R.id.subtitleText)
    }
}
```

## 实际应用场景

### 1. 聊天消息列表

```kotlin
class ChatMessageActivity : AppCompatActivity() {
    
    private lateinit var listView: ListView
    private lateinit var adapter: ChatMessageAdapter
    
    private val messageList = mutableListOf<ChatMessage>()
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_chat_message)
        
        initViews()
        setupData()
        setupAdapter()
        setupListView()
    }
    
    private fun initViews() {
        listView = findViewById(R.id.listView)
    }
    
    private fun setupData() {
        messageList.addAll(listOf(
            ChatMessage("张三", "你好，最近怎么样？", "10:30", true),
            ChatMessage("我", "还不错，你呢？", "10:32", false),
            ChatMessage("张三", "我也很好，明天见面吧", "10:35", true),
            ChatMessage("我", "好的，没问题", "10:36", false),
            ChatMessage("张三", "那就这样定了", "10:37", true)
        ))
    }
    
    private fun setupAdapter() {
        adapter = ChatMessageAdapter(this, messageList)
    }
    
    private fun setupListView() {
        listView.adapter = adapter
        
        listView.onItemClickListener = AdapterView.OnItemClickListener { _, _, position, _ ->
            val message = messageList[position]
            Toast.makeText(this, "消息: ${message.content}", Toast.LENGTH_SHORT).show()
        }
    }
}

data class ChatMessage(
    val sender: String,
    val content: String,
    val time: String,
    val isFromMe: Boolean
)

class ChatMessageAdapter(
    private val context: Context,
    private val messageList: MutableList<ChatMessage>
) : BaseAdapter() {
    
    override fun getCount(): Int = messageList.size
    
    override fun getItem(position: Int): ChatMessage = messageList[position]
    
    override fun getItemId(position: Int): Long = position.toLong()
    
    override fun getView(position: Int, convertView: View?, parent: ViewGroup?): View {
        val message = messageList[position]
        val view: View
        val holder: ChatMessageViewHolder
        
        if (convertView == null) {
            view = LayoutInflater.from(context).inflate(R.layout.chat_message_item, parent, false)
            holder = ChatMessageViewHolder(view)
            view.tag = holder
        } else {
            view = convertView
            holder = view.tag as ChatMessageViewHolder
        }
        
        holder.senderText.text = message.sender
        holder.contentText.text = message.content
        holder.timeText.text = message.time
        
        // 根据消息来源设置不同的样式
        if (message.isFromMe) {
            holder.messageContainer.setBackgroundColor(ContextCompat.getColor(context, R.color.my_message_bg))
            holder.senderText.setTextColor(ContextCompat.getColor(context, R.color.my_message_text))
            holder.contentText.setTextColor(ContextCompat.getColor(context, R.color.my_message_text))
        } else {
            holder.messageContainer.setBackgroundColor(ContextCompat.getColor(context, R.color.other_message_bg))
            holder.senderText.setTextColor(ContextCompat.getColor(context, R.color.other_message_text))
            holder.contentText.setTextColor(ContextCompat.getColor(context, R.color.other_message_text))
        }
        
        return view
    }
    
    private class ChatMessageViewHolder(view: View) {
        val messageContainer: LinearLayout = view.findViewById(R.id.messageContainer)
        val senderText: TextView = view.findViewById(R.id.senderText)
        val contentText: TextView = view.findViewById(R.id.contentText)
        val timeText: TextView = view.findViewById(R.id.timeText)
    }
}
```

## BaseAdapter 最佳实践

### 1. ViewHolder模式

```kotlin
abstract class BaseViewHolder {
    abstract fun bindData(data: Any)
}

class ContactViewHolder(view: View) : BaseViewHolder() {
    val nameText: TextView = view.findViewById(R.id.nameText)
    val phoneText: TextView = view.findViewById(R.id.phoneText)
    val emailText: TextView = view.findViewById(R.id.emailText)
    
    override fun bindData(data: Any) {
        if (data is ContactItem) {
            nameText.text = data.name
            phoneText.text = data.phone
            emailText.text = data.email
        }
    }
}
```

### 2. 适配器工具类

```kotlin
object BaseAdapterUtils {
    
    fun <T> createSimpleAdapter(
        context: Context,
        data: List<T>,
        layoutRes: Int,
        bindView: (View, T, Int) -> Unit
    ): BaseAdapter {
        return object : BaseAdapter() {
            override fun getCount(): Int = data.size
            override fun getItem(position: Int): T = data[position]
            override fun getItemId(position: Int): Long = position.toLong()
            
            override fun getView(position: Int, convertView: View?, parent: ViewGroup?): View {
                val view = convertView ?: LayoutInflater.from(context).inflate(layoutRes, parent, false)
                bindView(view, data[position], position)
                return view
            }
        }
    }
    
    fun createContactAdapter(
        context: Context,
        contacts: List<ContactItem>
    ): BaseAdapter {
        return createSimpleAdapter(context, contacts, R.layout.contact_item) { view, contact, position ->
            val nameText = view.findViewById<TextView>(R.id.nameText)
            val phoneText = view.findViewById<TextView>(R.id.phoneText)
            val emailText = view.findViewById<TextView>(R.id.emailText)
            
            nameText.text = contact.name
            phoneText.text = contact.phone
            emailText.text = contact.email
        }
    }
}
```

## 📋 总结

BaseAdapter 是 Android 开发中最灵活的适配器：

- **最大灵活性**：完全自定义列表项内容和样式
- **ViewHolder模式**：提高性能，减少findViewById调用
- **多类型支持**：支持不同类型的列表项
- **动态更新**：支持数据的动态添加、删除、修改
- **实际应用**：聊天消息、复杂列表、多类型数据等场景
- **最佳实践**：ViewHolder模式、工具类封装

掌握 BaseAdapter 的使用方法对于创建高度自定义的列表界面至关重要。
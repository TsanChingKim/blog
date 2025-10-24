---
title: Fragment 使用全解析
date: 2025-10-24
categories: ["Android"]
robots: all
summary: 详细介绍Android Fragment组件的生命周期、加载方式、数据传递和最佳实践
featureimage: images/android/16.jpg
---

# Fragment 使用全解析

Fragment 是 Android 3.0+ 引入的组件，用于构建灵活的用户界面，特别适合平板等大屏幕设备。

## Fragment 基本概念

### 什么是 Fragment

Fragment 是 Activity 的一个组成元素，可以理解为"片段"。一个 Activity 可以包含多个 Fragment，每个 Fragment 都有自己的生命周期和用户界面。

### Fragment vs Activity

| 特性 | Fragment | Activity |
|------|----------|----------|
| **生命周期** | 依赖 Activity | 独立 |
| **存在性** | 不能脱离 Activity | 可以独立存在 |
| **用途** | Activity 的组成元素 | 屏幕的主体 |
| **版本** | Android 3.0+ | Android 1.0+ |
| **数量** | 一个 Activity 可有多个 | 一个应用可有多个 |

## Fragment 生命周期

### 生命周期方法详解

```kotlin
class MyFragment : Fragment() {
    
    override fun onAttach(context: Context) {
        super.onAttach(context)
        Log.d("Fragment", "onAttach")
        // Fragment 与 Activity 关联
    }
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        Log.d("Fragment", "onCreate")
        // 初始化 Fragment
    }
    
    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        Log.d("Fragment", "onCreateView")
        // 创建 Fragment 的视图
        return inflater.inflate(R.layout.fragment_my, container, false)
    }
    
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        Log.d("Fragment", "onViewCreated")
        // 视图创建完成后的初始化
        initViews(view)
    }
    
    override fun onActivityCreated(savedInstanceState: Bundle?) {
        super.onActivityCreated(savedInstanceState)
        Log.d("Fragment", "onActivityCreated")
        // Activity 的 onCreate 完成后调用
    }
    
    override fun onStart() {
        super.onStart()
        Log.d("Fragment", "onStart")
        // Fragment 变为可见
    }
    
    override fun onResume() {
        super.onResume()
        Log.d("Fragment", "onResume")
        // Fragment 获得焦点
    }
    
    override fun onPause() {
        super.onPause()
        Log.d("Fragment", "onPause")
        // Fragment 失去焦点
    }
    
    override fun onStop() {
        super.onStop()
        Log.d("Fragment", "onStop")
        // Fragment 不可见
    }
    
    override fun onDestroyView() {
        super.onDestroyView()
        Log.d("Fragment", "onDestroyView")
        // 销毁 Fragment 的视图
    }
    
    override fun onDestroy() {
        super.onDestroy()
        Log.d("Fragment", "onDestroy")
        // 销毁 Fragment
    }
    
    override fun onDetach() {
        super.onDetach()
        Log.d("Fragment", "onDetach")
        // Fragment 与 Activity 解除关联
    }
    
    private fun initViews(view: View) {
        // 初始化视图控件
        val textView = view.findViewById<TextView>(R.id.textView)
        val button = view.findViewById<Button>(R.id.button)
        
        textView.text = "Fragment 内容"
        button.setOnClickListener {
            Toast.makeText(context, "Fragment 按钮被点击", Toast.LENGTH_SHORT).show()
        }
    }
}
```

### 生命周期状态图

{{< mermaid >}}
graph TD
    A[onAttach] --> B[onCreate]
    B --> C[onCreateView]
    C --> D[onViewCreated]
    D --> E[onActivityCreated]
    E --> F[onStart]
    F --> G[onResume]
    
    G --> H[onPause]
    H --> I[onStop]
    I --> J[onDestroyView]
    J --> K[onDestroy]
    K --> L[onDetach]
    
    H --> G
    I --> F
{{< /mermaid >}}

## Fragment 加载方式

### 1. 静态加载

在 XML 布局文件中直接声明 Fragment：

```xml
<!-- activity_main.xml -->
<LinearLayout
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical">
    
    <TextView
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="Activity 内容"
        android:padding="16dp" />
    
    <fragment
        android:id="@+id/myFragment"
        android:name="com.example.MyFragment"
        android:layout_width="match_parent"
        android:layout_height="0dp"
        android:layout_weight="1" />
    
</LinearLayout>
```

```kotlin
class MainActivity : AppCompatActivity() {
    
    private lateinit var myFragment: MyFragment
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        
        // 获取静态加载的 Fragment
        myFragment = supportFragmentManager.findFragmentById(R.id.myFragment) as MyFragment
    }
}
```

### 2. 动态加载

通过代码动态添加 Fragment：

```kotlin
class MainActivity : AppCompatActivity() {
    
    private lateinit var fragmentContainer: FrameLayout
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        
        initViews()
        loadFragment()
    }
    
    private fun initViews() {
        fragmentContainer = findViewById(R.id.fragmentContainer)
    }
    
    private fun loadFragment() {
        val fragment = MyFragment()
        
        supportFragmentManager.beginTransaction()
            .add(R.id.fragmentContainer, fragment)
            .commit()
    }
}
```

### 3. 动态切换 Fragment

```kotlin
class MainActivity : AppCompatActivity() {
    
    private lateinit var fragmentContainer: FrameLayout
    private lateinit var homeButton: Button
    private lateinit var profileButton: Button
    
    private var currentFragment: Fragment? = null
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        
        initViews()
        setupClickListeners()
        
        // 默认显示首页 Fragment
        showFragment(HomeFragment())
    }
    
    private fun initViews() {
        fragmentContainer = findViewById(R.id.fragmentContainer)
        homeButton = findViewById(R.id.homeButton)
        profileButton = findViewById(R.id.profileButton)
    }
    
    private fun setupClickListeners() {
        homeButton.setOnClickListener {
            showFragment(HomeFragment())
        }
        
        profileButton.setOnClickListener {
            showFragment(ProfileFragment())
        }
    }
    
    private fun showFragment(fragment: Fragment) {
        if (currentFragment != fragment) {
            supportFragmentManager.beginTransaction()
                .replace(R.id.fragmentContainer, fragment)
                .commit()
            currentFragment = fragment
        }
    }
}
```

## Fragment 数据传递

### 1. Activity → Fragment 传值

#### 使用 setArguments

```kotlin
class MyFragment : Fragment() {
    
    companion object {
        private const val ARG_TITLE = "title"
        private const val ARG_CONTENT = "content"
        
        fun newInstance(title: String, content: String): MyFragment {
            val fragment = MyFragment()
            val args = Bundle().apply {
                putString(ARG_TITLE, title)
                putString(ARG_CONTENT, content)
            }
            fragment.arguments = args
            return fragment
        }
    }
    
    private var title: String? = null
    private var content: String? = null
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        arguments?.let {
            title = it.getString(ARG_TITLE)
            content = it.getString(ARG_CONTENT)
        }
    }
    
    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        return inflater.inflate(R.layout.fragment_my, container, false)
    }
    
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        
        view.findViewById<TextView>(R.id.titleText).text = title
        view.findViewById<TextView>(R.id.contentText).text = content
    }
}

// Activity 中使用
class MainActivity : AppCompatActivity() {
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        
        val fragment = MyFragment.newInstance("标题", "内容")
        supportFragmentManager.beginTransaction()
            .add(R.id.fragmentContainer, fragment)
            .commit()
    }
}
```

#### 直接调用方法

```kotlin
class MyFragment : Fragment() {
    
    private lateinit var textView: TextView
    
    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        return inflater.inflate(R.layout.fragment_my, container, false)
    }
    
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        textView = view.findViewById(R.id.textView)
    }
    
    fun updateContent(newContent: String) {
        textView.text = newContent
    }
}

// Activity 中使用
class MainActivity : AppCompatActivity() {
    
    private lateinit var myFragment: MyFragment
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        
        myFragment = MyFragment()
        supportFragmentManager.beginTransaction()
            .add(R.id.fragmentContainer, myFragment)
            .commit()
        
        // 延迟调用，确保 Fragment 已创建
        Handler(Looper.getMainLooper()).postDelayed({
            myFragment.updateContent("新的内容")
        }, 100)
    }
}
```

### 2. Fragment → Activity 传值

#### 使用回调接口

```kotlin
class MyFragment : Fragment() {
    
    // 定义回调接口
    interface OnFragmentInteractionListener {
        fun onButtonClicked(message: String)
    }
    
    private var listener: OnFragmentInteractionListener? = null
    
    override fun onAttach(context: Context) {
        super.onAttach(context)
        listener = context as? OnFragmentInteractionListener
    }
    
    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        return inflater.inflate(R.layout.fragment_my, container, false)
    }
    
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        
        view.findViewById<Button>(R.id.button).setOnClickListener {
            listener?.onButtonClicked("来自 Fragment 的消息")
        }
    }
    
    override fun onDetach() {
        super.onDetach()
        listener = null
    }
}

// Activity 中实现接口
class MainActivity : AppCompatActivity(), MyFragment.OnFragmentInteractionListener {
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        
        val fragment = MyFragment()
        supportFragmentManager.beginTransaction()
            .add(R.id.fragmentContainer, fragment)
            .commit()
    }
    
    override fun onButtonClicked(message: String) {
        Toast.makeText(this, message, Toast.LENGTH_SHORT).show()
    }
}
```

#### 使用 EventBus

```kotlin
// 添加依赖：implementation 'org.greenrobot:eventbus:3.3.1'

// 定义事件类
data class FragmentMessageEvent(val message: String)

class MyFragment : Fragment() {
    
    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        return inflater.inflate(R.layout.fragment_my, container, false)
    }
    
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        
        view.findViewById<Button>(R.id.button).setOnClickListener {
            // 发送事件
            EventBus.getDefault().post(FragmentMessageEvent("来自 Fragment 的消息"))
        }
    }
}

// Activity 中接收事件
class MainActivity : AppCompatActivity() {
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        
        val fragment = MyFragment()
        supportFragmentManager.beginTransaction()
            .add(R.id.fragmentContainer, fragment)
            .commit()
    }
    
    override fun onStart() {
        super.onStart()
        EventBus.getDefault().register(this)
    }
    
    override fun onStop() {
        super.onStop()
        EventBus.getDefault().unregister(this)
    }
    
    @Subscribe(threadMode = ThreadMode.MAIN)
    fun onMessageEvent(event: FragmentMessageEvent) {
        Toast.makeText(this, event.message, Toast.LENGTH_SHORT).show()
    }
}
```

## Fragment 最佳实践

### 1. Fragment 状态保存

```kotlin
class MyFragment : Fragment() {
    
    private lateinit var editText: EditText
    private var userInput: String = ""
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // 恢复保存的状态
        savedInstanceState?.let {
            userInput = it.getString("userInput", "")
        }
    }
    
    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        return inflater.inflate(R.layout.fragment_my, container, false)
    }
    
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        
        editText = view.findViewById(R.id.editText)
        editText.setText(userInput)
        
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

### 2. Fragment 通信

```kotlin
class FragmentCommunicationActivity : AppCompatActivity() {
    
    private lateinit var fragmentA: FragmentA
    private lateinit var fragmentB: FragmentB
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_fragment_communication)
        
        initFragments()
    }
    
    private fun initFragments() {
        fragmentA = FragmentA()
        fragmentB = FragmentB()
        
        supportFragmentManager.beginTransaction()
            .add(R.id.fragmentAContainer, fragmentA)
            .add(R.id.fragmentBContainer, fragmentB)
            .commit()
    }
    
    // Fragment A 调用此方法
    fun sendMessageToFragmentB(message: String) {
        fragmentB.receiveMessage(message)
    }
    
    // Fragment B 调用此方法
    fun sendMessageToFragmentA(message: String) {
        fragmentA.receiveMessage(message)
    }
}

class FragmentA : Fragment() {
    
    private lateinit var messageText: TextView
    private lateinit var sendButton: Button
    
    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        return inflater.inflate(R.layout.fragment_a, container, false)
    }
    
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        
        messageText = view.findViewById(R.id.messageText)
        sendButton = view.findViewById(R.id.sendButton)
        
        sendButton.setOnClickListener {
            (activity as? FragmentCommunicationActivity)?.sendMessageToFragmentB("来自 Fragment A")
        }
    }
    
    fun receiveMessage(message: String) {
        messageText.text = "收到: $message"
    }
}

class FragmentB : Fragment() {
    
    private lateinit var messageText: TextView
    private lateinit var sendButton: Button
    
    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        return inflater.inflate(R.layout.fragment_b, container, false)
    }
    
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        
        messageText = view.findViewById(R.id.messageText)
        sendButton = view.findViewById(R.id.sendButton)
        
        sendButton.setOnClickListener {
            (activity as? FragmentCommunicationActivity)?.sendMessageToFragmentA("来自 Fragment B")
        }
    }
    
    fun receiveMessage(message: String) {
        messageText.text = "收到: $message"
    }
}
```

### 3. ViewPager2 + Fragment

```kotlin
class ViewPagerFragmentActivity : AppCompatActivity() {
    
    private lateinit var viewPager2: ViewPager2
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_view_pager_fragment)
        
        initViews()
        setupViewPager()
    }
    
    private fun initViews() {
        viewPager2 = findViewById(R.id.viewPager2)
    }
    
    private fun setupViewPager() {
        val fragments = listOf(
            HomeFragment(),
            ProfileFragment(),
            SettingsFragment()
        )
        
        val adapter = FragmentAdapter(this, fragments)
        viewPager2.adapter = adapter
    }
}

class FragmentAdapter(
    fragmentActivity: FragmentActivity,
    private val fragments: List<Fragment>
) : FragmentStateAdapter(fragmentActivity) {
    
    override fun getItemCount(): Int = fragments.size
    
    override fun createFragment(position: Int): Fragment = fragments[position]
}

class HomeFragment : Fragment() {
    
    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        return inflater.inflate(R.layout.fragment_home, container, false)
    }
    
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        view.findViewById<TextView>(R.id.titleText).text = "首页"
    }
}

class ProfileFragment : Fragment() {
    
    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        return inflater.inflate(R.layout.fragment_profile, container, false)
    }
    
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        view.findViewById<TextView>(R.id.titleText).text = "个人资料"
    }
}

class SettingsFragment : Fragment() {
    
    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        return inflater.inflate(R.layout.fragment_settings, container, false)
    }
    
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        view.findViewById<TextView>(R.id.titleText).text = "设置"
    }
}
```

## 📋 总结

Fragment 是 Android 开发中的重要组件：

- **生命周期管理**：理解 Fragment 的完整生命周期
- **加载方式**：静态加载和动态加载两种方式
- **数据传递**：Activity 与 Fragment 之间的数据传递
- **通信机制**：Fragment 之间的通信方法
- **最佳实践**：状态保存、内存管理、性能优化

掌握 Fragment 的使用方法对于构建灵活的用户界面至关重要，特别是在适配不同屏幕尺寸时。
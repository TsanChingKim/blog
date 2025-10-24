---
title: CheckBox 选择控件
date: 2025-10-24
categories: ["Android"]
robots: all
summary: 详细介绍Android选择控件的使用方法，包括CheckBox、RadioButton、ToggleButton和SeekBar
featureimage: images/android/10.jpg
---

# CheckBox 选择控件

Android 提供了多种选择控件，用于不同的用户交互场景。本文将详细介绍各种选择控件的使用方法。

## CheckBox 复选框

CheckBox 是系统封装的复选控件，支持两种状态：选中和未选中。

### 基本属性

| 属性 | 说明 | 示例值 |
|------|------|--------|
| `android:checked` | 初始选中状态 | `true`, `false` |
| `android:text` | 显示文本 | `"同意条款"` |
| `android:textOn` | 选中时显示文本 | `"已选中"` |
| `android:textOff` | 未选中时显示文本 | `"未选中"` |

### 基本使用

```xml
<CheckBox
    android:id="@+id/checkBox"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:text="同意用户协议"
    android:checked="false" />
```

### Kotlin 代码示例

```kotlin
class CheckBoxActivity : AppCompatActivity() {
    
    private lateinit var checkBox: CheckBox
    private lateinit var submitButton: Button
    private lateinit var statusText: TextView
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_checkbox)
        
        initViews()
        setupCheckBox()
        setupSubmitButton()
    }
    
    private fun initViews() {
        checkBox = findViewById(R.id.checkBox)
        submitButton = findViewById(R.id.submitButton)
        statusText = findViewById(R.id.statusText)
    }
    
    private fun setupCheckBox() {
        // 设置选中状态变化监听器
        checkBox.setOnCheckedChangeListener { _, isChecked ->
            statusText.text = if (isChecked) "已选中" else "未选中"
            submitButton.isEnabled = isChecked
        }
    }
    
    private fun setupSubmitButton() {
        submitButton.isEnabled = false
        submitButton.setOnClickListener {
            if (checkBox.isChecked) {
                Toast.makeText(this, "提交成功", Toast.LENGTH_SHORT).show()
            }
        }
    }
    
    // 程序控制选中状态
    private fun setCheckBoxChecked(checked: Boolean) {
        checkBox.isChecked = checked
    }
    
    // 获取选中状态
    private fun isCheckBoxChecked(): Boolean {
        return checkBox.isChecked
    }
}
```

### 多选示例

```kotlin
class MultiCheckBoxActivity : AppCompatActivity() {
    
    private lateinit var checkBoxes: List<CheckBox>
    private lateinit var selectAllButton: Button
    private lateinit var clearAllButton: Button
    private lateinit var submitButton: Button
    private lateinit var selectedCountText: TextView
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_multi_checkbox)
        
        initViews()
        setupCheckBoxes()
        setupButtons()
    }
    
    private fun initViews() {
        checkBoxes = listOf(
            findViewById(R.id.checkBox1),
            findViewById(R.id.checkBox2),
            findViewById(R.id.checkBox3),
            findViewById(R.id.checkBox4)
        )
        selectAllButton = findViewById(R.id.selectAllButton)
        clearAllButton = findViewById(R.id.clearAllButton)
        submitButton = findViewById(R.id.submitButton)
        selectedCountText = findViewById(R.id.selectedCountText)
    }
    
    private fun setupCheckBoxes() {
        val options = listOf("选项1", "选项2", "选项3", "选项4")
        
        checkBoxes.forEachIndexed { index, checkBox ->
            checkBox.text = options[index]
            checkBox.setOnCheckedChangeListener { _, _ ->
                updateSelectedCount()
            }
        }
        
        updateSelectedCount()
    }
    
    private fun setupButtons() {
        selectAllButton.setOnClickListener {
            selectAll(true)
        }
        
        clearAllButton.setOnClickListener {
            selectAll(false)
        }
        
        submitButton.setOnClickListener {
            submitSelectedOptions()
        }
    }
    
    private fun selectAll(select: Boolean) {
        checkBoxes.forEach { checkBox ->
            checkBox.isChecked = select
        }
        updateSelectedCount()
    }
    
    private fun updateSelectedCount() {
        val selectedCount = checkBoxes.count { it.isChecked }
        selectedCountText.text = "已选择: $selectedCount 项"
        submitButton.isEnabled = selectedCount > 0
    }
    
    private fun submitSelectedOptions() {
        val selectedOptions = checkBoxes
            .filter { it.isChecked }
            .map { it.text.toString() }
        
        val message = "已选择: ${selectedOptions.joinToString(", ")}"
        Toast.makeText(this, message, Toast.LENGTH_LONG).show()
    }
}
```

## RadioButton 单选框

RadioButton 是单选控件，通常与 RadioGroup 一起使用，确保一组中只能选择一个选项。

### 基本属性

| 属性 | 说明 | 示例值 |
|------|------|--------|
| `android:checked` | 初始选中状态 | `true`, `false` |
| `android:text` | 显示文本 | `"男"` |
| `android:button` | 自定义按钮样式 | `@drawable/custom_radio` |

### 基本使用

```xml
<RadioGroup
    android:id="@+id/radioGroup"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:orientation="vertical">
    
    <RadioButton
        android:id="@+id/radioButton1"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="男"
        android:checked="true" />
    
    <RadioButton
        android:id="@+id/radioButton2"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="女" />
    
    <RadioButton
        android:id="@+id/radioButton3"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="其他" />
    
</RadioGroup>
```

### Kotlin 代码示例

```kotlin
class RadioButtonActivity : AppCompatActivity() {
    
    private lateinit var radioGroup: RadioGroup
    private lateinit var submitButton: Button
    private lateinit var selectedText: TextView
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_radio_button)
        
        initViews()
        setupRadioGroup()
        setupSubmitButton()
    }
    
    private fun initViews() {
        radioGroup = findViewById(R.id.radioGroup)
        submitButton = findViewById(R.id.submitButton)
        selectedText = findViewById(R.id.selectedText)
    }
    
    private fun setupRadioGroup() {
        radioGroup.setOnCheckedChangeListener { _, checkedId ->
            val selectedRadioButton = findViewById<RadioButton>(checkedId)
            selectedText.text = "已选择: ${selectedRadioButton.text}"
        }
    }
    
    private fun setupSubmitButton() {
        submitButton.setOnClickListener {
            val checkedRadioButtonId = radioGroup.checkedRadioButtonId
            if (checkedRadioButtonId != -1) {
                val selectedRadioButton = findViewById<RadioButton>(checkedRadioButtonId)
                Toast.makeText(this, "提交: ${selectedRadioButton.text}", Toast.LENGTH_SHORT).show()
            } else {
                Toast.makeText(this, "请选择一个选项", Toast.LENGTH_SHORT).show()
            }
        }
    }
    
    // 程序控制选中状态
    private fun setRadioButtonChecked(radioButtonId: Int) {
        radioGroup.check(radioButtonId)
    }
    
    // 获取选中的 RadioButton
    private fun getSelectedRadioButton(): RadioButton? {
        val checkedId = radioGroup.checkedRadioButtonId
        return if (checkedId != -1) findViewById(checkedId) else null
    }
}
```

### 动态创建 RadioButton

```kotlin
class DynamicRadioButtonActivity : AppCompatActivity() {
    
    private lateinit var radioGroup: RadioGroup
    private lateinit var addOptionButton: Button
    private lateinit var submitButton: Button
    
    private val options = mutableListOf("选项1", "选项2", "选项3")
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_dynamic_radio_button)
        
        initViews()
        createRadioButtons()
        setupButtons()
    }
    
    private fun initViews() {
        radioGroup = findViewById(R.id.radioGroup)
        addOptionButton = findViewById(R.id.addOptionButton)
        submitButton = findViewById(R.id.submitButton)
    }
    
    private fun createRadioButtons() {
        options.forEachIndexed { index, optionText ->
            val radioButton = RadioButton(this).apply {
                id = View.generateViewId()
                text = optionText
                layoutParams = RadioGroup.LayoutParams(
                    RadioGroup.LayoutParams.WRAP_CONTENT,
                    RadioGroup.LayoutParams.WRAP_CONTENT
                )
            }
            radioGroup.addView(radioButton)
        }
    }
    
    private fun setupButtons() {
        addOptionButton.setOnClickListener {
            addNewOption()
        }
        
        submitButton.setOnClickListener {
            submitSelection()
        }
    }
    
    private fun addNewOption() {
        val newOptionText = "选项${options.size + 1}"
        options.add(newOptionText)
        
        val radioButton = RadioButton(this).apply {
            id = View.generateViewId()
            text = newOptionText
            layoutParams = RadioGroup.LayoutParams(
                RadioGroup.LayoutParams.WRAP_CONTENT,
                RadioGroup.LayoutParams.WRAP_CONTENT
            )
        }
        
        radioGroup.addView(radioButton)
        Toast.makeText(this, "添加了新选项: $newOptionText", Toast.LENGTH_SHORT).show()
    }
    
    private fun submitSelection() {
        val checkedId = radioGroup.checkedRadioButtonId
        if (checkedId != -1) {
            val selectedRadioButton = findViewById<RadioButton>(checkedId)
            Toast.makeText(this, "提交: ${selectedRadioButton.text}", Toast.LENGTH_SHORT).show()
        } else {
            Toast.makeText(this, "请选择一个选项", Toast.LENGTH_SHORT).show()
        }
    }
}
```

## ToggleButton 切换按钮

ToggleButton 是切换按钮，只有两种状态：开和关。

### 基本属性

| 属性 | 说明 | 示例值 |
|------|------|--------|
| `android:textOn` | 开启时显示文本 | `"开启"` |
| `android:textOff` | 关闭时显示文本 | `"关闭"` |
| `android:checked` | 初始状态 | `true`, `false` |

### 基本使用

```xml
<ToggleButton
    android:id="@+id/toggleButton"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:textOn="开启"
    android:textOff="关闭"
    android:checked="false" />
```

### Kotlin 代码示例

```kotlin
class ToggleButtonActivity : AppCompatActivity() {
    
    private lateinit var toggleButton: ToggleButton
    private lateinit var statusText: TextView
    private lateinit var actionButton: Button
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_toggle_button)
        
        initViews()
        setupToggleButton()
        setupActionButton()
    }
    
    private fun initViews() {
        toggleButton = findViewById(R.id.toggleButton)
        statusText = findViewById(R.id.statusText)
        actionButton = findViewById(R.id.actionButton)
    }
    
    private fun setupToggleButton() {
        toggleButton.setOnCheckedChangeListener { _, isChecked ->
            statusText.text = if (isChecked) "状态: 开启" else "状态: 关闭"
            actionButton.isEnabled = isChecked
        }
        
        // 初始状态
        statusText.text = "状态: 关闭"
        actionButton.isEnabled = false
    }
    
    private fun setupActionButton() {
        actionButton.setOnClickListener {
            if (toggleButton.isChecked) {
                Toast.makeText(this, "执行操作", Toast.LENGTH_SHORT).show()
            }
        }
    }
    
    // 程序控制状态
    private fun setToggleState(checked: Boolean) {
        toggleButton.isChecked = checked
    }
    
    // 获取当前状态
    private fun getToggleState(): Boolean {
        return toggleButton.isChecked
    }
}
```

## SeekBar 滑动条

SeekBar 是滑动条控件，常用于音量控制、进度调节等场景。

### 基本属性

| 属性 | 说明 | 示例值 |
|------|------|--------|
| `android:max` | 最大值 | `100` |
| `android:progress` | 当前值 | `50` |
| `android:progressTint` | 进度条颜色 | `@color/primary` |
| `android:thumbTint` | 滑块颜色 | `@color/accent` |

### 基本使用

```xml
<SeekBar
    android:id="@+id/seekBar"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:max="100"
    android:progress="50"
    android:progressTint="@color/primary"
    android:thumbTint="@color/accent" />
```

### Kotlin 代码示例

```kotlin
class SeekBarActivity : AppCompatActivity() {
    
    private lateinit var seekBar: SeekBar
    private lateinit var progressText: TextView
    private lateinit var resetButton: Button
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_seek_bar)
        
        initViews()
        setupSeekBar()
        setupResetButton()
    }
    
    private fun initViews() {
        seekBar = findViewById(R.id.seekBar)
        progressText = findViewById(R.id.progressText)
        resetButton = findViewById(R.id.resetButton)
    }
    
    private fun setupSeekBar() {
        seekBar.max = 100
        seekBar.progress = 50
        
        seekBar.setOnSeekBarChangeListener(object : SeekBar.OnSeekBarChangeListener {
            override fun onProgressChanged(seekBar: SeekBar?, progress: Int, fromUser: Boolean) {
                progressText.text = "进度: $progress%"
                
                // 根据进度改变背景色
                val backgroundColor = when {
                    progress < 30 -> Color.RED
                    progress < 70 -> Color.YELLOW
                    else -> Color.GREEN
                }
                progressText.setTextColor(backgroundColor)
            }
            
            override fun onStartTrackingTouch(seekBar: SeekBar?) {
                Toast.makeText(this@SeekBarActivity, "开始拖拽", Toast.LENGTH_SHORT).show()
            }
            
            override fun onStopTrackingTouch(seekBar: SeekBar?) {
                Toast.makeText(this@SeekBarActivity, "停止拖拽", Toast.LENGTH_SHORT).show()
            }
        })
        
        // 初始显示
        progressText.text = "进度: 50%"
    }
    
    private fun setupResetButton() {
        resetButton.setOnClickListener {
            seekBar.progress = 0
            progressText.text = "进度: 0%"
        }
    }
    
    // 程序控制进度
    private fun setProgress(progress: Int) {
        seekBar.progress = progress
    }
    
    // 获取当前进度
    private fun getProgress(): Int {
        return seekBar.progress
    }
}
```

### 音量控制示例

```kotlin
class VolumeControlActivity : AppCompatActivity() {
    
    private lateinit var volumeSeekBar: SeekBar
    private lateinit var volumeText: TextView
    private lateinit var muteButton: Button
    
    private var isMuted = false
    private var previousVolume = 50
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_volume_control)
        
        initViews()
        setupVolumeControl()
        setupMuteButton()
    }
    
    private fun initViews() {
        volumeSeekBar = findViewById(R.id.volumeSeekBar)
        volumeText = findViewById(R.id.volumeText)
        muteButton = findViewById(R.id.muteButton)
    }
    
    private fun setupVolumeControl() {
        volumeSeekBar.max = 100
        volumeSeekBar.progress = 50
        
        volumeSeekBar.setOnSeekBarChangeListener(object : SeekBar.OnSeekBarChangeListener {
            override fun onProgressChanged(seekBar: SeekBar?, progress: Int, fromUser: Boolean) {
                if (!isMuted) {
                    updateVolumeDisplay(progress)
                }
            }
            
            override fun onStartTrackingTouch(seekBar: SeekBar?) {
                // 开始拖拽
            }
            
            override fun onStopTrackingTouch(seekBar: SeekBar?) {
                // 停止拖拽
            }
        })
        
        updateVolumeDisplay(50)
    }
    
    private fun setupMuteButton() {
        muteButton.setOnClickListener {
            toggleMute()
        }
    }
    
    private fun toggleMute() {
        if (isMuted) {
            // 取消静音
            volumeSeekBar.progress = previousVolume
            muteButton.text = "静音"
            isMuted = false
            updateVolumeDisplay(previousVolume)
        } else {
            // 静音
            previousVolume = volumeSeekBar.progress
            volumeSeekBar.progress = 0
            muteButton.text = "取消静音"
            isMuted = true
            volumeText.text = "音量: 静音"
        }
    }
    
    private fun updateVolumeDisplay(volume: Int) {
        val volumeText = when {
            volume == 0 -> "音量: 静音"
            volume < 30 -> "音量: 低 ($volume%)"
            volume < 70 -> "音量: 中 ($volume%)"
            else -> "音量: 高 ($volume%)"
        }
        
        this.volumeText.text = volumeText
        
        // 模拟音量变化
        simulateVolumeChange(volume)
    }
    
    private fun simulateVolumeChange(volume: Int) {
        // 这里可以添加实际的音量控制逻辑
        Log.d("VolumeControl", "音量设置为: $volume%")
    }
}
```

## 实际应用场景

### 1. 设置页面

```xml
<ScrollView
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:padding="16dp">
    
    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="vertical">
        
        <!-- 通知设置 -->
        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="通知设置"
            android:textSize="18sp"
            android:textStyle="bold"
            android:layout_marginBottom="16dp" />
        
        <CheckBox
            android:id="@+id/pushNotificationCheckBox"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="推送通知"
            android:checked="true" />
        
        <CheckBox
            android:id="@+id/emailNotificationCheckBox"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="邮件通知"
            android:checked="false" />
        
        <!-- 主题设置 -->
        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="主题设置"
            android:textSize="18sp"
            android:textStyle="bold"
            android:layout_marginTop="32dp"
            android:layout_marginBottom="16dp" />
        
        <RadioGroup
            android:id="@+id/themeRadioGroup"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:orientation="vertical">
            
            <RadioButton
                android:id="@+id/lightThemeRadio"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="浅色主题"
                android:checked="true" />
            
            <RadioButton
                android:id="@+id/darkThemeRadio"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="深色主题" />
            
            <RadioButton
                android:id="@+id/autoThemeRadio"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="跟随系统" />
            
        </RadioGroup>
        
        <!-- 音量设置 -->
        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="音量设置"
            android:textSize="18sp"
            android:textStyle="bold"
            android:layout_marginTop="32dp"
            android:layout_marginBottom="16dp" />
        
        <SeekBar
            android:id="@+id/volumeSeekBar"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:max="100"
            android:progress="50" />
        
        <TextView
            android:id="@+id/volumeText"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="音量: 50%"
            android:layout_marginTop="8dp" />
        
    </LinearLayout>
    
</ScrollView>
```

### 2. 表单验证

```kotlin
class FormValidationActivity : AppCompatActivity() {
    
    private lateinit var agreementCheckBox: CheckBox
    private lateinit var genderRadioGroup: RadioGroup
    private lateinit var submitButton: Button
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_form_validation)
        
        initViews()
        setupValidation()
    }
    
    private fun initViews() {
        agreementCheckBox = findViewById(R.id.agreementCheckBox)
        genderRadioGroup = findViewById(R.id.genderRadioGroup)
        submitButton = findViewById(R.id.submitButton)
    }
    
    private fun setupValidation() {
        submitButton.setOnClickListener {
            if (validateForm()) {
                submitForm()
            }
        }
    }
    
    private fun validateForm(): Boolean {
        var isValid = true
        
        // 验证协议勾选
        if (!agreementCheckBox.isChecked) {
            Toast.makeText(this, "请同意用户协议", Toast.LENGTH_SHORT).show()
            isValid = false
        }
        
        // 验证性别选择
        if (genderRadioGroup.checkedRadioButtonId == -1) {
            Toast.makeText(this, "请选择性别", Toast.LENGTH_SHORT).show()
            isValid = false
        }
        
        return isValid
    }
    
    private fun submitForm() {
        val selectedGender = findViewById<RadioButton>(genderRadioGroup.checkedRadioButtonId)
        val message = "提交成功！\n性别: ${selectedGender.text}\n协议: 已同意"
        Toast.makeText(this, message, Toast.LENGTH_LONG).show()
    }
}
```

## 📋 总结

Android 选择控件提供了丰富的用户交互方式：

- **CheckBox**：多选场景，支持选中状态监听
- **RadioButton**：单选场景，与 RadioGroup 配合使用
- **ToggleButton**：开关状态，适合设置类功能
- **SeekBar**：数值调节，常用于音量、进度控制
- **实际应用**：设置页面、表单验证、用户偏好等场景

掌握这些选择控件的使用方法对于创建良好的用户交互体验至关重要。

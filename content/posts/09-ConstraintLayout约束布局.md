---
title: "ConstraintLayout约束布局"
date: 2025-10-22
categories: ["Android布局"]
description: "详细介绍Android ConstraintLayout约束布局的使用方法和属性配置，包括约束关系和偏移量设置"
featureimage: "/images/constraint-layout.jpg"
featureimagecaption: "ConstraintLayout约束布局示意图"
draft: false
---

# ConstraintLayout 约束布局

当前控件的某个方位和另一个参照物的某个方位对齐

- `app:layout_constraintLeft_toleftOf`： 相当于RelativeLayout的alignLeft属性
- `app:layout_constraintRight_toRightOf`： 相当于RelativeLayout的alignRight属性
- `app:layout_constraintTop_toTopOf`：相当于RelativeLayout的alignTop属性
- `app:layout_constraintBottom_toBottomOf`：相当于RelativeLayout的alignBottom属性
- `app:layout_constraintStart_toStartOf`：同Left_toLeft0f
- `app:layout_constraintEnd_toEndOf`：同Right_toRight0f

当前控件的A侧会在参照物的B侧
- `app:layout_constraintLeft_toRightOf`： 相当于RelativeLayout的toRight0
- `app:layout_constraintRight_toleftOf`：相当于RelativeLayout的toLeft0f
- `app:layout_constraintTop_toBottomOf`： 相当于RelativeLayout的below
- `app:layout_constraintBottom_toTopOf`： 相当于RelativeLayout的above
- `app:layout_constraintStart_toEndOf`： 同Left_toRightof
- `app:layout_constraintEnd_toStartOf`： 同Right_toleftof

- `app:layout_constraintVertical_bias="0.443"`：垂直偏移量，0.5在正中间
- `app:layout_constraintHorizontal_bias="0.443"`：水平偏移量，0.5在正中间

---
title: Chapter-1-引论
date: 2025-11-04
categories: ["DataStructure"]
robots: all
summary: 本文主要介绍了数据结构所需要的基础数学知识以及java类型的几个性质
featureimage: images/data-structure/chapter1back.jpg
---

{{< katex >}}

# 1.1 本书讨论的内容

设由一组 \(N\) 个数而要确定其中第 \(k\) 个最大者，我们称之为**选择问题(selection problem)**。
在解决这个问题时，有两种方法，第一种方法就是将 \(N\) 个数读进一个数组种，再通过某种简单的算法，比如冒泡排序，以递减的顺序将数组排序，然后返回位置 \(k\) 上的元素

稍微好一点的算法可以先将数组读入一个数组并以递减的顺序对其排列。接着逐个读入剩下的元素进行排序

这两种算法必然能够实现该需求，但是问题是，哪一种方法花费的时间更少、更好、更重要？

# 1.2 数学知识复习

## 1.2.1 指数
$$\begin{aligned}
X^AX^B & =X^{A+B}\\ \\
X^A/X^B & =X^{A-B}\\ \\
(X^A)^B & =X^{AB}\\ \\
X^N+X^N &=2X^N\neq X^{2N}\\ \\
2^N+2^N &=2^{N+1}
\end{aligned}$$

## 1.2.2 对数
**定义 1.1**
$$
X^A=B\ 当且仅当 \log_{X}B=A
$$
**定理1.1**
$$
\begin{aligned}
  \log_A B &= \frac{\log_C B}{\log_C A}, A,B>0 \\ \\
  \log \frac{A}{B} &= \log A - \log B \\ \\
  \log X &< X,  (\text{对所有 } X>0) \\ \\
  \log 1 &= 0,\log 2 = 1,\log 1024 = 10,\log 1048576 = 20
\end{aligned}
$$
## 1.2.3 级数
最容易记的公式是
$$
\sum_{i=0}^{N} 2^i = 2^{N+1}-1
$$
和
$$
\sum_{i=0}^{N}A^i=\frac{A^{N+1}-1}{A-1}
$$
在第二个公式中，如果 \(0<A<1\) 则
$$
\sum_{i=0}^{N}A^i \leq \frac{1}{1-A}
$$
当 \(N\) 趋向于 \(\infty\) 时该和趋向于 \(\frac{1}{1-A}\) ，这些公式是"几何级数"的公式。
分析中另一个常用的类型的级数是算数级数。任何这样的级数都可以从基本公式计算其值。
$$
\sum_{i=1}^{N}i=\frac{n(N+1)}{2} \approx \frac{N^2}2
$$
现在介绍其他两个公式，不过它们就没那么常见了
$$\begin{aligned}
\sum_{i=1}^{N}i^2=&\frac{N(N+1(2N+1))}{6}\approx \frac{N^3}3 \\
\sum_{i=1}^{N}i^k &\approx \frac{N^{k+1}}{|k+1|}\quad k \neq -1
\end{aligned}$$

当 \(k=-1\) 时，后一个公式不成立。此时我们需要下面的公式，在计科中经常使用，\(H_N\) 叫做调和数，其和焦作调和和。下面的近似式中的误差趋向于 \(y\approx 0.57721566\) ，称为**欧拉常数**（Euler's constant)
$$
H_N=\sum_{i=1}^{N}\frac1i \approx \log_eN
$$
## 1.2.4 模运算
如果A和B被N去除所得的余数都是相同的就叫同模 \(A\equiv B(mod N)\) ，在满足这个条件的情况下也可以得出 \(A+C\equiv B+C(modN)\) 以及 \(AD\equiv BD(mod N)\)    
## 1.2.5 证明方法
### 归纳法证明
归纳法有两个标准的步骤，第一步是证明**基准情形**（base case）。接着进行**归纳假设**（inductive hypothesis）。
### 通过反例证明
在斐波那契数列中 \(F_k \leq k^2\) 不成立。证明这个结论最容易的方法就是计算 \(F_{11}=144 > 11^2\) 
### 反证法证明
反证法证明是通过架设定理不成立，然后证明该架设导致某个已知的性质不成立，从而原假设是错误的
# 1.3 递归简论
递归的本质就是使用Java方法实现数学的函数。
如斐波那契数列
$$
f(x)=f(x-1)+f(x-2)
$$
我们将其分为两种情况一种是**基准情况**：\(f(0)=0，f(1)=1\) ，还有一种情况就是不断推进的情况，就是上面写的函数。在考虑这两种情况后编写递归
```java
public static int f(int x){
	if(x=0)
		return 0;
	else if(x=1)
		return 1;
	else
		return f(x-1)+f(x-2)
}
```
### 递归和归纳
1. 基准情形：必须总要有某些基准情形，它无需递归就能解出。
2. 不断推进：对于那些需要递归求解的情形，每一次递归调用都必须要使状态朝向一种基准情形推进。
3. 设计法则：假设所有的递归调用都能运行
4. 合成效益法则：在求解一个问题的同一个实例时，切勿在不同的递归调用中做重复性的工作
# 1.4 实现泛型构件 pre-Java 5
**泛型机制**：如果除去对象的基本类型外，实现方法时相通的，那么我们就可以使用**泛型实现**（generic implementation）来描述这种基本的功能。
## 1.4.1 使用 Object 表示泛型
Java中的基本事项就是可以通过使用像 Object 这样适当的超类来实现泛型类。
```java
// MemoryCell class
// Object read()
// void write(Object x)
public class MemoryCell{
	//private 
	private Object storedValue;
	public Object read(){
		return storedValue;
	}
	public void write(Object x){
		storedValue = x;
	}
}
```
## 1.4.2 基本类型的包装
当我们实现算法的时候，常常遇到语言定型的问题：我们已有一种类型的对象，可是语言语法却需要一种不同类型的对象。
这种技巧阐释了**包装类**（wrapper class）的基本主题。一种典型的用法是存储一个基本的类型，并添加一些这种基本类型不支持或不能正确支持的操作。
每一个包装对象都是不可变的，它存储一种当该对象被构建时所设置的原值，并提供一种方法以重新得到该值。包装类也包含不少的静态实用方法。
### 1.4.3 使用该接口类型表示泛型
只有在使用 Object 类中已有的那些方法能够表示执行的操作的时候，才能使用 Object 作为泛型来工作。
我们可以定义一个Comparable接口，让要比较的对象来实现Comparable接口，并实现其compareTo方法，这样就可以用来做比较。
{{< alert >}} 
- 只有实现 Comparable 接口的那些对象才能勾作为Comparable的数组的元素被传递
- 如果 Comoparable 数组有两个不相容的对象（例如，一个 String 和一个 Shape ）那么coompareTo方法将抛出异常 ClassCastExceptiion。这是我们期望的性质
- 如前所属基本类型不能作为 Comparable 传递，但是包装类则可以，因为它们实现了 Comparable 接口
- 这个方案不是总能行得通的，因为有时宣称一个类实现所需的接口是不可能的。如被 final 修饰的类
{{< /alert >}}
## 1.4.4 数组类型的兼容性
如何处理集合类型的继承问题：设`Employee`和`Student`都继承了`Person`类
```java
Person[] arr = new Employee[5];
arr[0] = new Student();
```
在java中数组是类型兼容的。这叫做**协变数组类型**（convariant array type）。如果将一个不兼容的类型插入到数组中，那么虚拟机将抛出一个 `ArrayStoreException` 异常。
# 1.5 利用 Java5 泛型特性实现泛型构件
## 1.5.1 简单的泛型类和接口
当指定一个泛型类时，类的生命则包含一个活多个类型参数，这些参数被放在类名后面的一对尖括号内。
也可以生命接口时泛型的，Java5之前无法指定接口是泛型的。
## 1.5.2 自动装箱/拆箱
当将int类型赋值给`Integer`对象时，编译器在幕后插入一个对 `Integer` 的构造方法的调用。这就叫做**自动装箱**。而如果`Integer`对象被放到需要`int`型量的地方，则编译器将在幕后插入一个对`intValue`方法的调用，这就叫做自动拆箱。
## 1.5.3 棱形运算符
创建泛型对象时，省略尖括号中间的类型
```Java
GenericMemoryCell<Integer> m = new GenericMemoryCell<>();
```
## 1.5.4 带有限制的通配符
当前有个场景，我们写了一个类：`Shape`，还有几个类继承了这个类：`Square`,`Rectangle`,`Circle`等。
我们写了一个方法要将一个`Shape`类型的数组中的元素提取出来之后进行面积求和
```java
public static double totalArea(Collection<Shape> arr){
	double total = 0;
	for(Shape s : arr){
		if(s != null){
			total += s.area();
		}
	}
	return total;
}
```
但是如果数组中有`Square`或`Rectangle`等类型的元素，则会导致程序报错。
这时候就需要用到**通配符**。
```java
public static double totalArea(Collection<? extends Shape> arr){
	double total = 0;
	for(Shape s : arr){
		if(s != null){
			total += s.area();
		}
	}
	return total;
}
```
## 1.5.5 泛型 static 方法
在下列场景下，我们需要限制其类型
1. 该特定类型用作返回类型
2. 该类型用在多雨一个的参数类型中
3. 该类型用于声明一个局部变量
```java
public static <AnyType> boolean contains(AnyType[] arr, AnyType x){
	for(AnyType val : arr)
		if(x.eauals(val))
			return true;
	return false;
}
```
## 1.5.6 泛型界限
```java
public static <AnyType> AnyType findMax(AnyType[] arr){
	int maxIndex = 0
	for(int i = 1; i < arr.length; i++){
		if(arr[i].coompareTo(arr[maxIndex]) > 0)
			maxIndex = i;
	}
	return arr[maxIndex];
}
```
在上述代码中我们并不能保证`AnyType`是继承了`Comparable`，所以我们就不能保证传入的参数是继承了`Comparable`，所以就会导致该参数中并没有`compareTo`方法
```java
public static <AnyType extends Comparable<AnyType>> AnyType findMax(AnyType[] arr){
	int maxIndex = 0
	for(int i = 1; i < arr.length; i++){
		if(arr[i].coompareTo(arr[maxIndex]) > 0)
			maxIndex = i;
	}
	return arr[maxIndex];
}
```
## 1.5.7 类型擦除
泛型类可以由编译器通过**类型擦除**（type erasure)来将泛型类转换为非泛型类。这样，编译器就生成一种与泛型类同名的**原始类**（raw class），但是类型参数都被删去了。类型变量由它们的类型限界来代替，当一个具有擦除返回类型的泛型方法被调用的时候，一些特性被自动地插入。如果使用一个泛型类而不带类型参数，那么使用的是原始类。
## 1.5.8 对于泛型的限制
### 基本类型
基本类型不能用作类型参数。因此，在尖括号中指定的类型不能是基本类型
### instanceof 检测
例如在将一个Object值赋值给一个String类型的值时，如果不进行强制类型转换就会发生一个运行时错误
### static 的语境
在一个泛型类中，static方法和static域均不可引用类的类型变量，因为在类型擦除后，类型变量就不存在了。
### 泛型类型的实例化
不能创建一个泛型类型的实例。如果T是一个类型变量，则语句
```java
T obj = new T(); // 右边是非法的
```
## 泛型数组对象
也不能创建一个泛型类的数组。如果T是一个类型变量，则语句
```java
T [] arr = new T[10]; // 右边是非法的
```
### 参数话类型的数组
```java
GenericMemoryCell<String>[] arr1 = new GenericMemoryCell<>[10];
GenericMemoryCell<Double> cell = new GenericMemoryCell<>();
cell.write(4.5);
Object[] arr2 = arr1;
arr2[0]=cell;
String s = arr1[0].read
```
正常情况下，我们认为第四行会报错，但是在类型擦除之后，两者的类型一致就会正常赋值
# 1.6 函数对象
定一个一个没有数据而只有一个方法的类，并传递该类的一个实例。一个函数通过将其放在一个对象内部而被传递。这样的对象通常叫做**函数对象**（function object）
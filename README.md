---
MPDA-DE	
---

# MPDA-DE
MPDA-DE

参考[DE的网址](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.differential_evolution.html)







---

### 工作计划

- [ ] 完成DE 算法 （DE 算法应该借鉴 scipy 的DE 编程技巧）

- [ ] 完成解码方案

- [ ] 

- [ ] 算例采用什么呢？ 

  > 以前生成的算例嘛

---

### 代码结构

#### 编程语言 all in Python

1. MPDA
   1. 
2. DE 





---

### 编程中没有搞懂的问题

1. ~~f~~un~~c : callable~~~~
          ~~The objective function to be minimized.  Must be in the form~~
          ~~``f(x, *args)``, where ``x`` is the argument in the form of a 1-D array~~
          ~~and ``args`` is a  tuple of any additional fixed parameters needed to~~
          completely specify the function.~~~~

2. ​        print('??? = =',self.population[[0, 2], :])

3. trial = np.where(crossovers, bprime, trial)

4. ```python
          while (i < self.parameter_count and
                 rng.rand() < self.cross_over_probability):
              trial[fill_point] = bprime[fill_point]
              fill_point = (fill_point + 1) % self.parameter_count
              i += 1
          return trial
      ```

5. ```
      _calActionSeq 这个函数 应该分为三种可能性，在完成时间为无穷的情况下， 行动序列的时间应该为 非无穷的最大到达时间。
      ```
---



### 存在的问题

1. 采用新的编码机制 -  编码空间的冗余性 减少了编码本身存在的意义

   > 拟采用的解决方案，是进行对比，证明我们这个新的解码方案可以产生更好的解

2. 对比算法 应该选什么呢？

   > 1. 每一个操作算子 都应该证明其有效性。
   > 2. PSO 算法？

3. 在网上是不是存在一些高级的连续优化算法的源代码？ 现在高级的连续优化的代码是什么呢？

    

---



### 单词

1. [Dithering](v.犹豫不决;踌躇)
2. 







---



### 库

1.  多目标优化的库 Platypus 
2.  优化的库 NiaPy

## 拟采用的对比方法

1. **JADE (必须要对比的方法)**
2. SADE
3. JDE

在多排列编码模式下的**MPDA-GENTIC ALGORITHM**

MPDA - GENTIC ALGORITHMS 是否可以参考郭博士的 GA 





最终解 应该是一套行动序列

那么 我存储的也应该是一套行动序列

行动序列的表示方法 与朱 的表示方法一致吗？

每一个行动序列 都可以是一个完整的解

行动序列是与instance的值想对应



**任务点的状态变化序列** 也可以表示整个解

**任务点状态的表示方法和行动序列的表示方法 应该可以相互 *表示转换***



浅拷贝和深拷贝 为什么还是存在问题？？？


### 编程中可以优化的部分

1. actionSeq 在调用ACTIONtime 的时候 没有必要每次都进行计算 = =
2. task 的线性模型 也应该表现出来
3. 



## 一些想法

1. 连续变量的编码模式更方便 我们利用知识吗？
2. 


？？？
类内变量 类变量
继承之后的情况是什么样子的？？

super 函数 是super 自己啦







>>> class A(object):
>>>         def foo1(self):
>>>             print "Hello",self
>>>         @staticmethod
>>>         def foo2():
>>>             print "hello"
>>>         @classmethod
>>>         def foo3(cls):
>>>             print "hello",cls


>>> a = A()

>>> a.foo1()          #最常见的调用方式，但与下面的方式相同
>>> Hello <__main__.A object at 0x9f6abec>

>>> A.foo1(a)         #这里传入实例a，相当于普通方法的self
>>> Hello <__main__.A object at 0x9f6abec>

>>> A.foo2()          #这里，由于静态方法没有参数，故可以不传东西
>>> hello

>>> A.foo3()          #这里，由于是类方法，因此，它的第一个参数为类本身。
>>> hello <class '__main__.A'>

>>> A                 #可以看到，直接输入A，与上面那种调用返回同样的信息。
>>> <class '__main__.A'>
---------------------
作者：daijiguo 
来源：CSDN 
原文：https://blog.csdn.net/daijiguo/article/details/78499422 
版权声明：本文为博主原创文章，转载请附上博文链接！


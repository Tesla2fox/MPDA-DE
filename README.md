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
5. 
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







---



### 库

1.  多目标优化的库 Platypus 
2.  优化的库 NiaPy
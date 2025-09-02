# Python包与模块学习笔记

### 1.模块（Module）

- __定义：__模块就是一个```.py```文件，里面可以包含变量、函数、类等。

- __作用：__便于代码复用和维护

- __导入方式：__

  ``` python
  import module_name
  import module_name as alias #给模块起别名
  from module_name import func_name,var_name
  from module_name import * #不推荐，容易命名冲突
  ```

### 示列

```python
# my_module.py
def greet(name):
    return f"Hello,{name}!"
```

```python
# main.py
import my_module
print(my_module.greet("Alice"))
```

---

### 2.包（Package）

- __定义：__包是一个包含多个模块的目录，必须有一个``__init__.py``文件

- __结构：__

  ```
  my_package/
  ├── __init__.py
  ├── module1.py
  └── module2.py
  ```

- __导入方式：__

  ```python
  import my_package.module1
  from my_package import module2
  from my_package.module1 import func_name
  ```

---

### 3.常用内置模块

- **math：**数学函数
- **OS：**操作系统接口
- **sys：**Python解释器相关
- **random：**随机数
- **datetime：**日期和时间

### 实例

```python
import math, random, datetime

print(math.sqrt(16))          # 4.0
print(random.randint(1, 10))  # 随机数
print(datetime.datetime.now())
```

---

### 4.自定义模块与包

- 将常用的函数写在``.py``文件中，作为模块导入。
- 使用``__init.py``管理包的导出内容：

```python
# __init__.py
from .module1 import func1
from .module2 import func2
```

----

### 作业题目

### 基础作业

1. 创建一个 `math_utils.py` 模块，写一个 `factorial(n)` 函数，返回 n 的阶乘，并在 `main.py` 中导入使用。
2. 使用 `random` 模块生成一个 1~100 的随机数，写一个猜数字小游戏。

### 进阶作业

3. 创建一个包 `string_tools`，里面包含：

- `reverse.py`：写一个 `reverse_string(s)` 函数。
- `count.py`：写一个 `count_vowels(s)` 函数，统计字符串中元音字母数量。
- 在 `main.py` 中调用这两个函数。

4. 使用 `datetime` 模块，写一个函数 `days_until(date_str)`，输入日期（格式如 `"2025-09-10"`），返回今天到该日期的天数。
# Python __init__.py文件的作用

> 许多项目的文件下都有__init__.py文件，其中都是注释信息，但是删除了这个文件程序却运行不了，尤其是被import的时候会出问题

## 作用
1. 表示该目录是python的一个模块包

    ```
    .
    └── mypackage
        ├── subpackage_1
        │   ├── test11.py
        │   └── test12.py
        ├── subpackage_2
        │   ├── test21.py
        │   └── test22.py
        └── subpackage_3
            ├── test31.py
            └── test32.py

    from mypackage.subpackage_1 import test11
    from mypackage.subpackage_1 import test12
    from mypackage.subpackage_2 import test21
    from mypackage.subpackage_2 import test22
    from mypackage.subpackage_3 import test31
    from mypackage.subpackage_3 import test32
    ```
    > 比如上面的文件结构，如果需要import所有py文件时，需要挨个import

    ```
    .
    └── mypackage
        ├── __init__.py
        ├── subpackage_1
        │   ├── test11.py
        │   └── test12.py
        ├── subpackage_2
        │   ├── test21.py
        │   └── test22.py
        └── subpackage_3
            ├── test31.py
            └── test32.py
    import mypackage
    ```
    > 加入__init__.py后只需import这个目录，就会自动执行__init__.py文件的代码（通常全是注释信息）


## 常见应用
1. 指定默认导入的模块

    `from mypackage.subpackage_1 import test11`

   
2. `from module import *`实现
    - 需要在__init__.py中设置变量__all__，这样import *就等于import __all__变量中的全部模块
        ```
        __all__ = ['subpackage_1', 'subpackage_2']
        ```


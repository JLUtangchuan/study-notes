# Tensorflow 2.1 安装
- 2020.02.24

**问题** 总是报错找不到DLL
`ImportError: DLL load failed: The specified module could not be found.`

错误的尝试：
1. 环境变量问题
2. CUDA cuDNN版本问题，重装了好几次
3. Anaconda问题，创建了虚拟环境


最终解决：[参考博客](https://blog.csdn.net/qq_29159273/article/details/103996055)

在Github上找到了解决方法：https://github.com/tensorflow/tensorflow/issues/35749

> 方法一：TensorFlow降到2.0.0 【O__O "…】
> 
> **方法二：下载并安装：https://support.microsoft.com/en-us/help/2977003/the-latest-supported-visual-c-downloads**

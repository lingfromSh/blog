---
title: OpenGL - What is OpenGL?
date: 2022-08-07 15:32:29
tags:
  - ComputerGraphics
  - OpenGL
  - C++
---

# What is OpenGL?

OpenGL is mainly considered an API (an Application Programming Interface) that provides us with a large set of functions that we can use to manipulate graphics and images. However, OpenGL by itself is not an API, but merely a specification, developed and maintained by the Khronos Group.

## What is Khronos Group?

Khronos Group团队成立于 2000 年 1 月，由包括 3Dlabs, ATI, Discreet, Evans & Sutherland, Intel, Nvidia, SGI 和 Sun Microsystems 在内的多家国际知名多媒体行业领导者创立，致力于发展开放标准的应用程序接口 API ，以实现在多种平台和终端设备上的富媒体创作、加速和回放。

## Core-profile vs Immediate mode

> 摘录自[Opengl的核心模式与立即渲染模式](https://blog.csdn.net/weixin_42887343/article/details/122681819)

早期的OpenGL使用立即渲染模式（Immediate mode，也就是固定渲染管线），这个模式下绘制图形很方便。
OpenGL的大多数功能都被库隐藏起来，开发者很少有控制OpenGL如何进行计算的自由。而开发者迫切希望能有更多的灵活性。随着时间推移，规范越来越灵活，开发者对绘图细节有了更多的掌控。

立即渲染模式确实容易使用和理解，但是效率太低。因此从OpenGL3.2开始，规范文档开始废弃立即渲染模式，并鼓励开发者在OpenGL的核心模式(Core-profile)下进行开发，这个分支的规范完全移除了旧的特性。
当使用OpenGL的核心模式时，OpenGL迫使我们使用现代的函数。当我们试图使用一个已废弃的函数时，OpenGL会抛出一个错误并终止绘图。现代函数的优势是更高的灵活性和效率，然而也更难于学习。立即渲染模式从OpenGL实际运作中抽象掉了很多细节，因此它在易于学习的同时，也很难让人去把握OpenGL具体是如何运作的。现代函数要求使用者真正理解OpenGL和图形编程，它有一些难度，然而提供了更多的灵活性，更高的效率，更重要的是可以更深入的理解图形编程。

## Extensions

OpenGL支持直接使用拓展，有时候图形厂商可能在驱动中提供了新特性(更高效或便捷)，而这些特性不存在现有OpenGL中。但是照样可以通过拓展方式去使用他们，这样就无需等待OpenGL的新版本支持。
如果此类特性足够流行好用，OpenGL也会在新版本中支持他们。

```cpp
if(GL_ARB_extension_name)   // 拓展名
{
    // Do cool new and modern stuff supported by hardware
}
else
{
    // Extension not supported: do it the old way
}
```

## State Machine

OpenGL采用状态机编程。用一系列变量描述OpenGL当前状态，通常这些状态集合，我们称为OpenGL上下文。

## Objects

OpenGL库是由C编写，同时有其他语言的派生版本。但是其核心仍然是C编写的，由于C无法很好地转换为其他语言，所以在OpenGL中抽象了很多结构来应对这个问题。 Objects就是其中一种抽象结构。
一个object就是一系列OpenGL状态的集合

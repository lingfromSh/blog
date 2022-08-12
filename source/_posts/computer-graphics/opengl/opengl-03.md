---
title: OpenGL - Creating a window
date: 2022-08-07 16:46:26
tags:
  - ComputerGraphics
  - OpenGL
  - C++
---

# Creating a window

创建窗口是第一步，然而OpenGL仅仅是定义了一系列关于窗口的操作api，而这些操作api实际执行和操作系统和硬件都有很大关系。这也意味着开发者必须自己处理这些问题。

不过，幸运的是我们可以使用一些库来避免自己处理这些问题。例如GLUT,GLFW,SDL,SFML等。

## GLFW

Ubuntu下安装

```shell
# 安装opengl、glfw、glew库
sudo apt install libglfw3 libglfw3-dev libopengl-dev libglew2.2 libglew-dev
```


## GLAD

除了GLFW来帮助解决窗口外，还需要使用GLAD解决函数指针问题。OpenGL仅仅是一套标准，有大量需要使用的函数在写代码时候是不确定其实际位置的(和驱动相关)，所以需要通过查找函数名的方式来确定其运行时地址。


打开[glad官网](https://glad.dav1d.de/)

![img](computer-graphics/opengl/opengl-03/2022-08-07_17-04.png)

将下载好的glad.c文件拷贝到项目目录, glad和KHR文件夹复制到/usr/local/include/目录下

## 编写代码

```cpp
#include <glad/glad.h>
#include <GLFW/glfw3.h>

#include <iostream>

void framebuffer_size_callback(GLFWwindow *window, int width, int height);
void process_keyboard_input(GLFWwindow *window);

int main(void)
{

    // 初始化glfw
    GLFWwindow *window;
    int w_width = 1920, w_height = 1080;

    if (!glfwInit())
    {
        std::cout << "failed to init glfw" << std::endl;
        return -1;
    }

    window = glfwCreateWindow(1920, 1080, "cube", NULL, NULL);
    if (!window)
    {
        std::cout << "failed to create window" << std::endl;
        glfwTerminate();
        return -1;
    }

    // 创建上下文
    glfwMakeContextCurrent(window);

    if (!gladLoadGLLoader((GLADloadproc)glfwGetProcAddress))
    {
        std::cout << "failed to init glad" << std::endl;
        return -1;
    }

    glfwSetFramebufferSizeCallback(window, framebuffer_size_callback);

    while (!glfwWindowShouldClose(window))
    {
        // 处理键盘事件
        process_keyboard_input(window);

        glClearColor(0.2, 0.4, 0.6, 1.0);

        glClear(GL_COLOR_BUFFER_BIT);

        // 设置点信息
        glPointSize(10);
        glColor3ub(125, 255, 255);
        
        // 画三个点,平面坐标范围是(-1, 1)
        glBegin(GL_POINTS);
        glVertex3f(0, 0, 0);
        glVertex3f(0.5, 0, 0);
        glVertex3f(-0.5, 0, 0);
        glEnd();

        glfwSwapBuffers(window);

        glfwPollEvents();
    }

    glfwTerminate();
    return 0;
}

void framebuffer_size_callback(GLFWwindow *window, int width, int height)
{
    // 改变绘图区域
    glfwMakeContextCurrent(window);
    glViewport(0, 0, width, height);
}

void process_keyboard_input(GLFWwindow *window) {
    // 检测到esc就关闭窗口
    if(glfwGetKey(window, GLFW_KEY_ESCAPE) == GLFW_PRESS) {
        glfwSetWindowShouldClose(window, GL_TRUE);
    }
}
```

## 验证

```shell
c++ main.cpp glad.c -o main -lgl -lglfw 
./main
```

## 结果截图

![img](computer-graphics/opengl/opengl-03/result.png)
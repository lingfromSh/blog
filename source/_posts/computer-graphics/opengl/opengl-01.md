---
title: OpenGL - setting up
tags:
  - ComputerGraphics
  - OpenGL
  - C++
categories:
  - computer-graphics
  - opengl
date: 2022-07-26 22:37:56
---

# OpenGL - setting up

platform: Ubuntu 22.04

## Installing GLFW + OpenGL + GLEW

```shell
# 安装opengl、glfw、glew库
sudo apt install libglfw3 libglfw3-dev libopengl-dev libglew2.2 libglew-dev
```

### Validating installation

```cpp
/*
 * @Author: shiyun.ling shiyun.ling@flexiv.com
 * @Date: 2022-07-26 23:27:12
 * @LastEditors: shiyun.ling
 * @LastEditTime: 2022-07-26 23:27:29
 * @Description: file content
 */

#include <GLFW/glfw3.h>

int main(void)
{
    GLFWwindow* window;

    /* Initialize the library */
    if (!glfwInit())
        return -1;

    /* Create a windowed mode window and its OpenGL context */
    window = glfwCreateWindow(640, 480, "Hello World", NULL, NULL);
    if (!window)
    {
        glfwTerminate();
        return -1;
    }

    /* Make the window's context current */
    glfwMakeContextCurrent(window);

    /* Loop until the user closes the window */
    while (!glfwWindowShouldClose(window))
    {
        /* Render here */
        glClear(GL_COLOR_BUFFER_BIT);

        /* Swap front and back buffers */
        glfwSwapBuffers(window);

        /* Poll for and process events */
        glfwPollEvents();
    }

    glfwTerminate();
    return 0;
}
```
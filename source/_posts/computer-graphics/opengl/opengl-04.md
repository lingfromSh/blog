---
title: OpenGL - Hello, Triangle
date: 2022-08-07 21:37:47
tags:
  - ComputerGraphics
  - OpenGL
  - C++
---

# OpenGL - Hello, Triangle

所有东西在OpenGL内都是三维的, 但是屏幕或窗口是2d的。所以所有坐标都需要由3D转为2D坐标。这个转换过程成为管线(pipeline)。这里面分为两大步，第一步坐标转换，第二步将坐标转为像素点绘图。

这些步骤都是高度分化的，所以很容易并行执行。GPU有很多的小单元所以很适合去并行执行这些任务，这些小单元上运行的程序则称为shader(着色器)。

着色器用GLSL控制。

## Pipelines

Vertex Data -> Shape Assembly -> Geometry Shader -> Rasterization(光栅化) -> Fragment Shader -> Test and Blending

## 编写代码

```cpp

#include <glad/glad.h>
#include <GLFW/glfw3.h>

#include <iostream>

void framebuffer_size_callback(GLFWwindow *window, int width, int height);
void process_keyboard_input(GLFWwindow *window);

// shader written in GLSL
const char *vertexShaderSource = "#version 330 core\n"
                                 "layout (location = 0) in vec3 aPos;\n"
                                 "void main()\n"
                                 "{\n"
                                 "   gl_Position = vec4(aPos.x, aPos.y, aPos.z, 1.0);\n"
                                 "}\0";

const char *fragmentShaderSource = "#version 330 core\n"
                                   "out vec4 FragColor;\n"
                                   "void main()\n"
                                   "{\n"
                                   "    FragColor = vec4(1.0f, 0.5f, 0.2f, 1.0f);\n"
                                   "}\0";

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

    /******************************
              shader part
    *******************************/ 

    // vertex shader
    unsigned int vertexShader;
    vertexShader = glCreateShader(GL_VERTEX_SHADER);
    // 编译Vertex shader
    glShaderSource(vertexShader, 1, &vertexShaderSource, NULL);
    glCompileShader(vertexShader);

    // fragment shader
    unsigned int fragmentShader;
    fragmentShader = glCreateShader(GL_FRAGMENT_SHADER);
    // 编译Fragment shader
    glShaderSource(fragmentShader, 1, &fragmentShaderSource, NULL);
    glCompileShader(fragmentShader);

    // shader
    unsigned int shaderProgram;
    shaderProgram = glCreateProgram();
    glAttachShader(shaderProgram, vertexShader);
    glAttachShader(shaderProgram, fragmentShader);
    glLinkProgram(shaderProgram);
    glDeleteShader(vertexShader);
    glDeleteShader(fragmentShader);

    /***********************
          triangle part
    ***********************/

    // 定义三角形顶点
    float vertexArray[] = {
        0.5, -0.5, 0,
        -0.5, -0.5, 0,
        0, 0.5, 0,
    };

    // 存储分配到的id
    unsigned int VBO, VAO;
    glGenVertexArrays(1, &VAO);
    glGenBuffers(1, &VBO);

    glBindVertexArray(VAO);
    glBindBuffer(GL_ARRAY_BUFFER, VBO);
    glBufferData(GL_ARRAY_BUFFER, sizeof(vertexArray), vertexArray, GL_STATIC_DRAW);

    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(float), (void*)0);
    glEnableVertexAttribArray(0);

    glBindBuffer(GL_ARRAY_BUFFER, 0);
    glBindVertexArray(0); 

    glfwSetFramebufferSizeCallback(window, framebuffer_size_callback);

    while (!glfwWindowShouldClose(window))
    {
        // 处理键盘事件
        process_keyboard_input(window);

        glClearColor(0.2, 0.4, 0.6, 1.0);

        glClear(GL_COLOR_BUFFER_BIT);

        // use our shader program when we want to render an object
        glUseProgram(shaderProgram); // 不使用，则上默认色
        glBindVertexArray(VAO);
        glDrawArrays(GL_TRIANGLES, 0, 3);

        glfwSwapBuffers(window);

        glfwPollEvents();
    }

    glDeleteVertexArrays(1, &VAO);
    glDeleteBuffers(1, &VBO);
    glDeleteProgram(shaderProgram);

    glfwTerminate();
    return 0;
}

void framebuffer_size_callback(GLFWwindow *window, int width, int height)
{
    glfwMakeContextCurrent(window);
    glViewport(0, 0, width, height);
}

void process_keyboard_input(GLFWwindow *window)
{
    if (glfwGetKey(window, GLFW_KEY_ESCAPE) == GLFW_PRESS)
    {
        glfwSetWindowShouldClose(window, GL_TRUE);
    }
}
```

## 结果截图

![img](computer-graphics/opengl/opengl-04/result.png)
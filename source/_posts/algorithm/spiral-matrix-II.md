---
title: 螺旋矩阵II
date: 2022-10-11 10:30:43
tags:
    - algorithm
    - leetcode
    - array
    - iteration
---

# 螺旋矩阵II

给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。

 
示例 1：


输入：n = 3
输出：[[1,2,3],[8,9,4],[7,6,5]]
示例 2：

输入：n = 1
输出：[[1]]


来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/spiral-matrix-ii

## 解题思路

模拟填充

```rust
impl Solution {
    pub fn generate_matrix(n: i32) -> Vec<Vec<i32>> {

        // 初始化数组
        let mut matrix = vec![];
        let mut i: i32 = 0;
        while i < n {
            let row = vec![0;n as usize];
            matrix.push(row);
            i += 1;
        }

        // 模拟填充
        let mut score = 1;
        let mut pos_x = 0;
        let mut pos_y = 0;
        let mut direction = "r";
        let mut border_top: usize = 0;
        let mut border_bottom: usize = (n - 1) as usize;
        let mut border_left: usize = 0;
        let mut border_right: usize = (n - 1) as usize;
        while score <= n * n {
            // 注意下标，别弄错了
            matrix[pos_y][pos_x] = score;

            // 计算下次填充的位置和朝向
            match direction {
                "r" => {
                    if pos_x < border_right {
                        pos_x += 1;
                    }else {
                        direction = "d";
                        pos_y += 1;
                        border_top += 1;
                    }
                },
                "l" => {
                    if pos_x > border_left {
                        pos_x -= 1;
                    }else {
                        direction = "u";
                        pos_y -= 1;
                        border_bottom -= 1;
                    }
                },
                "u" => {
                    if pos_y > border_top {
                        pos_y -= 1;
                    }else {
                        direction = "r";
                        pos_x += 1;
                        border_left += 1;
                    }
                },
                "d" => {
                    if pos_y < border_bottom {
                        pos_y += 1;
                    }else {
                        direction = "l";
                        pos_x -= 1;
                        border_right -= 1;
                    }
                },
                _ => break,
            }

            score += 1;
        }

        matrix.clone()
    }
}
```
---
title: 最小长度子数组
date: 2022-10-10 23:45:43
tags:
    - algorithm
    - leetcode
    - array
    - binary-search
    - sliding-window
---

# 最小长度子数组

给定一个含有 n 个正整数的数组和一个正整数 target 。

找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。

链接：https://leetcode.cn/problems/minimum-size-subarray-sum
## 解决思路

### 滑动窗口

    ```rust
    impl Solution {
        pub fn min_sub_array_len(target: i32, nums: Vec<i32>) -> i32 {
            let mut start = 0;  // 窗口起始
            let mut end = 0; // 窗口截止
            let mut min_length: i32 = nums.len() as i32 + 1;
            let mut ans = 0;

            // 先包含进足够多的数，再减去多余的数，如果小了，end ++ 否则 start ++。
            // 直到不存在满足条件的情况

            while start < nums.len() && end < nums.len() {
                ans += nums[end];
                while ans >= target {
                    let length = end as i32 - start as i32 + 1;
                    if min_length >= length {
                        min_length = length;
                    }
                    ans -= nums[start];
                    start += 1;
                }
                end += 1;
            }

            if min_length == nums.len() as i32 + 1 {
                return 0;
            }
            min_length
        }
    }
    ```

### 前缀和+二分查找(Optional)

    略
---
title: Leetcode - is palindrome
date: 2022-09-25 11:00:56
tags:
    - algorithm
    - leetcode
---

# Is Palindrome

如果在将所有大写字符转换为小写字符、并移除所有非字母数字字符之后，短语正着读和反着读都一样。则可以认为该短语是一个 回文串 。

字母和数字都属于字母数字字符。

给你一个字符串 s，如果它是 回文串 ，返回 true ；否则，返回 false 。

## Python

1. 遍历
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = "".join([i.lower() for i in s if i.lower() in "0123456789abcdefghijklmnopqrstuvwxyz"])

        return s == s[::-1]
```

2. 双指针
```python
import string 

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        characters = set(string.digits + string.ascii_lowercase)
        left, right = 0, len(s) - 1

        while left < right:
            lower_left = s[left].lower()
            lower_right = s[right].lower()
            
            if lower_left not in characters:
                left += 1
                continue            

            if lower_right not in characters:
                right -= 1
                continue

            if lower_left != lower_right:
                return False

            left += 1
            right -= 1

        return True
```

## C++

1. 双指针
    ```cpp
    class Solution {
    public:
        bool isPalindrome(string s) {

            string newString;
            for (char ch: s) {
                if (isalnum(ch)) {
                    newString += toLower(ch);
                }
            }
            
            int n = newString.size();
            int left = 0, right = n - 1;
            while (left < right) {
                if (newString[left] != newString[right]) {
                    return false;
                }
                left++;
                right--;
            }
            return true;
        }
    };
    ``` 

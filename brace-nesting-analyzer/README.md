# 🔍 Brace Nesting Depth Analyzer

## 📊 Project Overview

This project analyzes the nesting depth of curly braces `{}` in Java-like code while **ignoring** braces inside strings, single-line comments (`//`), and block comments (`/* */`). It was developed in Python as part of a Programming Languages lab assignment.

---

## 📄 Features

- Tracks opening `{` and closing `}` brace nesting
- Ignores braces inside:
  - Strings: `"example { here }"`
  - Single-line comments: `// like this }`
  - Block comments: `/* example { block */`
- Detects unmatched closing braces and extra `{`
- Outputs nesting level per line

---

## 🧠 What I Did

- Parsed code line by line using character indexing
- Managed flags to track when inside comments or strings
- Applied conditionals to count braces only outside comments/strings

---

## 🧪 Sample Input
```java
class Example {
    public static void main(String[] args) {
        System.out.println("Hello {world}"); // brace inside string
        /* opening {
           inside comment
        */
        {
            int x = 10;
            if (x > 0) {
                System.out.println(x);
            }
        }
    }
}

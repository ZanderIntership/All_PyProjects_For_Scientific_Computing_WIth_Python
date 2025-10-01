# 🧮 Arithmetic Arranger

A Python function that takes a list of arithmetic problems ➕➖ and arranges them **vertically** and **side-by-side**, just like how students solve problems on paper in school 📚✏️.  

This project is part of the **FreeCodeCamp Scientific Computing with Python curriculum** 🚀🐍.

---

## ✨ Features

✅ Accepts up to **5 problems** at a time  
✅ Supports **addition (`+`)** and **subtraction (`-`)** only  
✅ Optionally displays the **answers** 🎯  
✅ Automatically formats problems with:
- ➡️ Right-aligned numbers  
- 📏 Proper spacing  
- 📉 Dashes under each problem  
- 🔄 Four spaces between problems  

---

## ⚠️ Error Handling

The function returns clear error messages if something goes wrong 🚫:

- ❌ Too many problems:  
  `"Error: Too many problems."` (limit is 5)

- ❌ Invalid operator (only `+` or `-` allowed):  
  `"Error: Operator must be '+' or '-'."`

- ❌ Non-digit numbers:  
  `"Error: Numbers must only contain digits."`

- ❌ Numbers longer than 4 digits:  
  `"Error: Numbers cannot be more than four digits."`

---

## 🛠 Usage

### 🔹 Function Signature
```python
def arithmetic_arranger(problems, solve=False):
    ...

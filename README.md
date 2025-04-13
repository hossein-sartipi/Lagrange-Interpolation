# 🧮 Lagrange Interpolation Calculator

This Python script calculates the **Lagrange Interpolation Polynomial** for a given set of points.  
It's a step-by-step, interactive CLI tool that helps you compute the interpolation and visualize the resulting simplified polynomial.

---

## 📌 Features

- Interactive input of (x, y) points  
- Eliminates duplicate entries  
- Constructs the Lagrange basis polynomials  
- Outputs the final simplified interpolation polynomial in human-readable math format using SymPy

---

## 🛠️ Requirements

- Python 3.6+
- `sympy` library

Install with:

```bash
pip install sympy
```
## 🚀 How to Use

Run the script:
```bash
python lagrange_interpolation.py
```
Then enter your data points interactively:
```text
x_0: 1
y_0: 2
x_1: 2
y_1: 3
x_2:
wanna break?Y/N: Y
```
The result will be printed in a simplified algebraic form, such as:
```diff
x+1
```











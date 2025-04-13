🧮 Lagrange Interpolation Calculator

This Python script calculates the Lagrange Interpolation Polynomial for a given set of points. It's a step-by-step, interactive CLI tool that helps you compute the interpolation and visualize the resulting simplified polynomial.

📌 Features

Interactive input of (x, y) points
Eliminates duplicate entries
Constructs the Lagrange basis polynomials
Outputs the final simplified interpolation polynomial in human-readable math format using SymPy
🛠️ Requirements

Python 3.6+
sympy library
Install with:

pip install sympy
🚀 How to Use

Run the script:

python lagrange_interpolation.py
Then enter your data points interactively:

x_0: 1
y_0: 2
x_1: 2
y_1: 3
x_2:
wanna break?Y/N: Y
The result will be printed in a simplified algebraic form, like:

   1   1     
- ──⋅x + ──
   2   2
📚 How It Works

The script includes 3 main functions:

Lagranje_1(): Parses and formats points for interpolation
Lagranje_2(): Constructs the numerator and denominator of each Lagrange basis term
Lagranje_3(): Combines all terms and prints the final simplified polynomial
📝 Notes

Input stops when you enter a blank value for x_i or y_i and confirm with Y.
Only numeric inputs are accepted. Any invalid input will ask for re-entry.
📄 License

MIT License. Feel free to use, modify, and share!

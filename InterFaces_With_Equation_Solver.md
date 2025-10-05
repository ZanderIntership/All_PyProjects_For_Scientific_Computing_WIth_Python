🧮 Equation Solver

A Python module that provides a clean, object-oriented approach to solving and analyzing linear and quadratic equations.
It uses an abstract base class to define common equation behavior and supports automatic equation formatting, solving, and analysis.

📘 Features

Abstract base class Equation to enforce structure for all equation types

Subclasses for:

Linear equations (degree 1)

Quadratic equations (degree 2)

Input validation:

Ensures correct number of coefficients

Ensures coefficients are numeric

Prevents zero as the leading coefficient

Automatically formats equation strings (e.g., 1x**2 + 2x + 1 = 0 → x**2 + 2x + 1 = 0)

Provides detailed analysis:

For linear equations → slope and intercept

For quadratic equations → vertex, concavity, and extrema

Unified solver() function for formatted output

🧱 Class Structure
Equation (Abstract Base Class)

Defines the interface and shared behavior for all equations.

Attributes

degree: Degree of the polynomial (int)

type: Human-readable type (str)

coefficients: Dictionary mapping power → coefficient

Abstract Methods

solve() → returns list of roots

analyze() → returns dict of analysis data

LinearEquation

Represents a first-degree equation of the form:

𝑎
𝑥
+
𝑏
=
0
ax+b=0

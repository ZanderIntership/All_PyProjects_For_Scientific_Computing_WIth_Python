🚀 Projectile Trajectory Calculator

A simple Python utility that models and visualizes the motion of a projectile under gravity 🌍.
It calculates displacement, coordinates, and even plots a rough ASCII trajectory in your terminal 🖥️.

📦 Features

✅ Object-Oriented Design — Clean, modular classes for physics and visualization.
✅ Mathematical Accuracy — Uses projectile motion equations with customizable speed, angle, and height.
✅ ASCII Graph Rendering — See your projectile’s path in the terminal using dots and axis symbols.
✅ Utility Helper — Run simulations easily with the projectile_helper() function.

⚙️ How It Works

The program uses physics equations to compute projectile motion:

𝑦
=
ℎ
+
𝑥
tan
⁡
(
𝜃
)
−
𝑔
𝑥
2
2
𝑣
2
cos
⁡
2
(
𝜃
)
y=h+xtan(θ)−
2v
2
cos
2
(θ)
gx
2
	​


Then it generates:

📋 A table of (x, y) coordinates

🧭 A trajectory graph using text characters

🧠 Classes Overview
🎯 Projectile

Handles the motion equations and stores:

speed (m/s)

height (m)

angle (°)

Calculates:

Displacement

All (x, y) coordinates of the trajectory

📊 Graph

Takes the list of coordinates and:

Prints a neat table of values

Draws a text-based trajectory graph with:

∙ = projectile path

⊣ = y-axis

T = x-axis

🧩 The Helper Function
🪄 projectile_helper(speed, height, angle)

Creates a projectile, computes all its motion data, and prints:

Projectile details 🧾

Coordinate table 📋

ASCII trajectory graph 🎨

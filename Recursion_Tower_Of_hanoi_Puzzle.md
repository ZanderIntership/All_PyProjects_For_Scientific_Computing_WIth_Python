Tower of Hanoi (Python Implementation)

This project demonstrates a simple recursive solution to the classic Tower of Hanoi puzzle using Python.

📖 Problem Description

The Tower of Hanoi is a mathematical puzzle consisting of three rods and a number of disks of different sizes that can slide onto any rod. The puzzle starts with the disks stacked in ascending order of size on one rod (largest at the bottom, smallest at the top).

The objective is to move the entire stack to another rod, obeying the following rules:

Only one disk can be moved at a time.

Each move consists of taking the upper disk from one stack and placing it on top of another stack.

No disk may be placed on top of a smaller disk.

🛠️ Implementation Details

NUMBER_OF_DISKS: Controls how many disks the puzzle starts with (default = 5).

Rods are represented as Python lists:

A → Source rod

B → Auxiliary rod

C → Target rod

The recursive function move(n, source, auxiliary, target) performs the steps to solve the puzzle.

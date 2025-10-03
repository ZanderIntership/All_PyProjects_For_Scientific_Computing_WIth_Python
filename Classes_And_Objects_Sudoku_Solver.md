🧩 Sudoku Solver

A simple backtracking Sudoku solver in Python! This script can take an unsolved Sudoku board and fill it in according to the rules of Sudoku.

✨ Features

🔍 Finds empty cells in the Sudoku grid

✅ Validates rows, columns, and 3×3 squares

🌀 Uses backtracking recursion to solve puzzles

🎯 Detects unsolvable puzzles

📦 How It Works

📋 Input your Sudoku puzzle as a 2D list (9×9 grid).

0 or None = empty cell

🧮 The algorithm checks possible numbers (1–9).

🔄 It recursively tries valid numbers until the board is complete.

🏆 If solvable → prints the solved board.
❌ If not → notifies that the puzzle is unsolvable.

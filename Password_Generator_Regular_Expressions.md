Password Generator 🔑

This project is a secure password generator written in Python. It uses the secrets module (which is cryptographically secure) to generate random passwords that satisfy common security requirements such as including numbers, special characters, uppercase, and lowercase letters.

Features ✨

Generates strong, random passwords using secrets.choice().

Ensures the password includes:

At least one digit (0–9).

At least one special character (punctuation).

At least one uppercase letter (A–Z).

At least one lowercase letter (a–z).

Customizable length and constraints.

Defaults to a 16-character secure password.

Requirements ⚙️

Python 3.6+ (for the secrets module and f-strings).

No external dependencies are required.

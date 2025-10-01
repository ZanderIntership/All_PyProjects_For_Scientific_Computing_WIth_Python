Credit Card Validator

This Python program verifies whether a given credit card number is valid using the Luhn algorithm (a checksum formula commonly used for validating credit card numbers).

📌 Features

Implements the Luhn algorithm for card number verification.

Automatically removes spaces and dashes from the input.

Prints VALID! if the card number passes the check, otherwise prints INVALID!.

🛠️ How It Works

The program reverses the card number and separates digits into odd and even positions.

Odd-position digits are summed directly.

Even-position digits are doubled:

If the result is greater than or equal to 10, the digits of the result are summed.

Example: 7 × 2 = 14 → 1 + 4 = 5.

The final sum is calculated.

If the total sum modulo 10 is 0, the card number is valid.

📂 Code Structure

verify_card_number(card_number): Implements the Luhn algorithm.

main():

Defines a sample card number.

Removes hyphens (-) and spaces.

Calls verify_card_number() and prints the result.

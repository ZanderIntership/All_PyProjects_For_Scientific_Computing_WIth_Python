🔐 Vigenère Cipher – Encrypt & Decrypt

This Python script demonstrates the Vigenère cipher, a classical encryption method that uses a keyword to shift letters in a message.

📌 Features

Encrypt and decrypt text using a custom key.

Preserves spaces and non-alphabetic characters.

Simple implementation for learning cryptography basics.

🛠️ How It Works

Each letter of the message is shifted by the alphabetical index of the corresponding key letter.

Example: If the message letter is h and the key letter is a (a = 0), the result is still h.

If the key letter is c (c = 2), then h → j.

Non-alphabet characters (spaces, punctuation) remain unchanged.

The process can be reversed (decrypt) by subtracting the key shift instead of adding.

📂 Code Structure

vigenere(message, key, direction): Core function for both encryption & decryption.

encrypt(message, key): Encrypts using the Vigenère cipher.

decrypt(message, key): Decrypts the message back to plain text.

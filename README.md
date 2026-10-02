# DES (Data Encryption Standard) in Pure Python

A lightweight, dependency-free implementation of the **DES (Data Encryption Standard)** algorithm written from scratch using only Python's built-in tools. 

This project demonstrates the core mechanics of symmetric key cryptography, working directly with 64-bit blocks, bitwise operations, permutations, and Feistel function rounds.

## 🚀 Features

* **Pure Python:** Zero external dependencies (no `pip install` required).
* **Standard Library Only:** Utilizes built-in modules (like `base64` / `struct`) for data formatting and handling 64-bit blocks.
* **Educational & Clean:** Step-by-step implementation of Key Scheduling, Initial/Final Permutations, and S-Boxes.

## ⚙️ How It Works

The implementation strictly follows the original DES specification:
1. **Key Generation:** Derives 16 subkeys (48-bit each) from the initial 64-bit key.
2. **IP & FP:** Processes data through Initial and Final Permutations.
3. **Feistel Cipher:** Executes 16 rounds of encryption using Expansion, XOR, S-Box substitution, and Straight Permutation.

## ⚠️ Disclaimer

This repository is created strictly for **educational and research purposes**. 
The DES algorithm is cryptographically broken and vulnerable to brute-force attacks due to its short 56-bit effective key length. **Do not use this code to secure sensitive production data.** For real-world applications, use modern standards like **AES (Advanced Encryption Standard)**.



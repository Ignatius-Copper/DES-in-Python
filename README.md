# Custom DES Encryption Algorithm in Python

This repository contains a custom software implementation of the **DES (Data Encryption Standard)** symmetric block cipher written in Python. 

The script allows you to encrypt arbitrary text using a secret key, outputs the encrypted result in **Base64** format, and then correctly decrypts it back to the original string.

---

## 🚀 Features

* **Block Padding:** Automatically pads the input text and key with null bytes (`\x00`) to align them to 8-byte (64-bit) blocks.
* **Feistel Network:** A full 16-round encryption and decryption cycle.
* **The f Function:** Includes E-box expansion, XOR with the round key, non-linear substitution via 8 S-boxes, and a final P-box permutation.
* **Key Schedule:** Generates round keys using a byte-level cyclic shift (2 bytes per round).
* **Base64 Encoding:** Encodes binary ciphertext into a printable Base64 string for easy transmission.

---

## 🛠 Prerequisites

To run this script, you need **Python 3.x**. No external libraries or third-party dependencies are required.


---

## 💻 Usage

### Example Run

```text
Введите текст для шифрованием DES: Hello World
Введите ключ шифрования DES: my_secret_key

[Base64 Output]: 4aDq8Z... (encrypted string)
[Binary Ciphertext]: b'\xe2\xa0\xea...'
[Decrypted Text]: Hello World
```

---

## 🔍 Code Architecture

The implementation relies on three core functions:

1. **`f(right, round_key)`** – The core Feistel round function. It takes the right half of the block and the current round key, applies expansion, runs it through the S-boxes, performs the P-box permutation, and returns a 32-bit result.
2. **`Des_encode(text, keyword)`** – Splits the input string into 64-bit blocks, coordinates the 16 encryption rounds, prints the Base64 representation, and returns the raw encrypted bytes.
3. **`Des_decode(bites, keyword)`** – Reverses the Feistel network process by applying the round keys in reverse order, rearranges block halves, and strips the trailing padding bytes (`\x00`) to recover the original string.

⚠️ **Disclaimer:** This project is designed purely for **educational and demonstration purposes**. Because it shifts keys at the byte level (rather than bitwise per the official DES standard) and omits initial/final permutations (IP/FP), it is not cryptographically secure and should not be used to protect production data.




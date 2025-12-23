# SHA256 Dictionary Cracker

A lightweight Python utility designed to perform dictionary attacks against SHA256 hashes. This tool was developed to deconstruct the mechanics of cryptographic hash comparisons and iterative adversarial logic.

## Technical Overview
In offensive security, understanding the transition from plaintext to ciphertext is fundamental. This project implements a dictionary attack—a technique that leverages pre-computed wordlists to identify the original plaintext behind a SHA256 hash. 

Unlike a brute-force attack which tries every possible combination, this script focuses on efficiency by testing likely candidates from a provided passlist.



## Key Features
- **Real-time Progress Tracking:** Leverages the `pwntools` logging library to provide live status updates on attempt counts and current hash comparisons.
- **Input Validation:** Pre-verifies that the target hash adheres to the 64-character SHA256 standard before initializing the crack.
- **Robust Error Handling:** Implements `try-except` blocks to handle `FileNotFound` errors gracefully, ensuring the tool exits cleanly rather than crashing on bad user input.
- **Encoding Safety:** Uses `latin-1` encoding to handle common wordlists (like `rockyou.txt`) that often contain non-UTF-8 characters.

## How it Works
The script follows a standard cryptographic auditing pipeline:
1. **Ingest:** Accepts a target SHA256 hash and a path to a password file.
2. **Normalize:** Strips whitespace and encodes the wordlist entries into bytes.
3. **Compute:** Generates a SHA256 hash for each entry using the adversarial logic.
4. **Compare:** Performs a bitwise comparison between the target and the generated hash.
5. **Report:** Displays a success message upon a match or a failure message if the list is exhausted.

## Prerequisites
This tool requires **Python 3.x** and the **Pwntools** library. 

```bash
pip install pwntools
```
## Usage
Run the script by providing the target hash and the path to your wordlist.
Bash
```bash
python3 cracker.py
```
**Note**: Ensure you have a valid wordlist (e.g., rockyou.txt) available in your directory or referenced path.
## Disclaimer
*This tool is intended for educational purposes and authorized security testing only. The author is not responsible for any misuse or damage caused by this program. Always ensure you have permission to test the targets you are auditing.*

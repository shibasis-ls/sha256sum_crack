from pwn import *
import sys

target_hash = input("Enter the SHA256 hash: ").strip()
if len(target_hash) != 64:
    print("Error: That is not a valid SHA256 hash (must be 64 characters).")
    sys.exit(1)
passfile = input("Enter the path to passlist: ").strip()
attempts = 0

try:
    with log.progress("Attempting to crack:") as p:
        with open(passfile, "r", encoding='latin-1') as passlist:
            for password in passlist:
                password = password.strip("\n").encode('latin-1')
                passhash = sha256sumhex(password)
                
                p.status(f"[{attempts}] {password.decode('latin-1', errors='ignore')}")
                
                if passhash == target_hash:
                    p.success(f"\nPassword found after {attempts} attempts: {password.decode('latin-1')} hashes to {target_hash}")
                    sys.exit(0)
                
                attempts += 1
            
            p.failure("Password not found in the provided list.")

except FileNotFoundError:
    print(f"\n[!] ERROR: The file '{passfile}' was not found. Please check the path and try again.")
    sys.exit(1)
except Exception as e:
    print(f"\n[!] AN UNEXPECTED ERROR OCCURRED: {e}")
    sys.exit(1)

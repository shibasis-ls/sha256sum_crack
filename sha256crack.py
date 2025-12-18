from pwn import *
import sys

if len(sys.argv) !=2:
    print("invalid argument")
    print(f">> {sys.argv[0]} <sha256sum>")
    exit()
hash = sys.argv[1]
print(hash)
passfile = "common.txt" 
attempts = 0

with log.progress (f"attempting to crack: {hash}") as p:
    with open(passfile,"r", encoding='latin-1') as passlist:
        for password in passlist:
            password = password.strip("\n").encode('latin-1')
            passhash= sha256sumhex(password)
            p.status(f"[{attempts}] {password.decode('latin-1')} = {passhash}")
            if passhash == hash:
                p.success(f"password hash found {attempts} attempts {password} hashes to {hash}")
                exit()
            attempts += 1
        p.failure("passhash not found")



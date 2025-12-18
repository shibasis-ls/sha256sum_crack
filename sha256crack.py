from pwn import *

hash = input("enter the hash: ")
print(hash)
passfile = input("enter the path to passlist: ") 
attempts = 0

with log.progress (f"attempting to crack:") as p:
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



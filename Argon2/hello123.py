import hashlib
from argon2 import PasswordHasher

password = b"hello123"
password_str = "hello123"

# MD5
md5_hash = hashlib.md5(password).hexdigest()
print(f"MD5: {md5_hash}")

# SHA256
sha256_hash = hashlib.sha256(password).hexdigest()
print(f"SHA256: {sha256_hash}")

# Argon2
ph = PasswordHasher(time_cost=2, memory_cost=8192, parallelism=2)
argon2_hash = ph.hash(password_str)
print(f"Argon2: {argon2_hash}")

# Save to files
with open("hashes_MD5.txt", "w") as f:
    f.write(md5_hash)

with open("hashes_SHA256.txt", "w") as f:
    f.write(sha256_hash)

with open("hashes_Argon2.txt", "w") as f:
    f.write(argon2_hash)
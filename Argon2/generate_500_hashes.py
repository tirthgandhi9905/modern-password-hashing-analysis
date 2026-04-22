import hashlib
from argon2 import PasswordHasher
import random

# Read passwords
with open("1000MostCommonPasswords.txt", "r") as f:
    all_passwords = [line.strip() for line in f.readlines() if line.strip()]

# Select 500 random passwords
selected_passwords = random.sample(all_passwords, min(500, len(all_passwords)))

# Initialize Argon2
ph = PasswordHasher(time_cost=2, memory_cost=8192, parallelism=2)

# Generate hashes
md5_hashes = []
sha256_hashes = []
argon2_hashes = []

print("Generating 500 hashes...")
for i, password in enumerate(selected_passwords):
    password_bytes = password.encode()
    
    # MD5
    md5_hash = hashlib.md5(password_bytes).hexdigest()
    md5_hashes.append(md5_hash)
    
    # SHA256
    sha256_hash = hashlib.sha256(password_bytes).hexdigest()
    sha256_hashes.append(sha256_hash)
    
    # Argon2
    argon2_hash = ph.hash(password)
    argon2_hashes.append(argon2_hash)
    
    if (i + 1) % 100 == 0:
        print(f"Generated {i + 1} hashes...")

# Save to files
with open("hashes_MD5.txt", "w") as f:
    f.write("\n".join(md5_hashes))

with open("hashes_SHA256.txt", "w") as f:
    f.write("\n".join(sha256_hashes))

with open("hashes_Argon2.txt", "w") as f:
    f.write("\n".join(argon2_hashes))

print(f"✓ Generated and saved 500 hashes!")
print(f"  - hashes_MD5.txt: {len(md5_hashes)} hashes")
print(f"  - hashes_SHA256.txt: {len(sha256_hashes)} hashes")
print(f"  - hashes_Argon2.txt: {len(argon2_hashes)} hashes")

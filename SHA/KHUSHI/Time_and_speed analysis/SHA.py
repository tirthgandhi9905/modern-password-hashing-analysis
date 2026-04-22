import hashlib
import os
import time

# ===============================
# CONFIG
# ===============================
INPUT_FILE = "passwords.txt"

files = {
    "sha1": "sha1.txt",
    "sha1_salted": "sha1_salted.txt",
    "sha256": "sha256.txt",
    "sha256_salted": "sha256_salted.txt",
    "sha3": "sha3.txt",
    "sha3_salted": "sha3_salted.txt"
}

# ===============================
# LOAD PASSWORDS
# ===============================
with open(INPUT_FILE, "r", encoding="utf-8", errors="ignore") as f:
    passwords = [line.strip() for line in f if line.strip()]

print(f"Loaded {len(passwords)} passwords\n")

# ===============================
# HASH FUNCTIONS
# ===============================
def sha1(p):
    return hashlib.sha1(p.encode()).hexdigest()

def sha256(p):
    return hashlib.sha256(p.encode()).hexdigest()

def sha3(p):
    return hashlib.sha3_256(p.encode()).hexdigest()

# ===============================
# SALTED HASH
# ===============================
def salted_hash(func, p, mode="append"):
    salt = os.urandom(8).hex()

    if mode == "append":
        h = func(p + salt)
    else:
        h = func(salt + p)

    return f"{h}:{salt}"

# ===============================
# GENERATE HASH FILES
# ===============================
def generate_file(filename, func, salted=False):
    start = time.time()

    with open(filename, "w") as f:
        for p in passwords:
            if salted:
                h = salted_hash(func, p)
            else:
                h = func(p)
            f.write(h + "\n")

    end = time.time()
    print(f"{filename} generated in {end - start:.4f} sec")

print("===== GENERATING HASH FILES =====\n")

generate_file(files["sha1"], sha1)
generate_file(files["sha1_salted"], sha1, salted=True)

generate_file(files["sha256"], sha256)
generate_file(files["sha256_salted"], sha256, salted=True)

generate_file(files["sha3"], sha3)
generate_file(files["sha3_salted"], sha3, salted=True)

# ===============================
# TIME + SPEED ANALYSIS
# ===============================
def measure_time(func, label, iterations=2000):
    total_hashes = iterations * len(passwords)

    start = time.time()
    for _ in range(iterations):
        for p in passwords:
            func(p)
    end = time.time()

    total_time = end - start
    speed = total_hashes / total_time

    print(f"{label}")
    print(f"Time: {total_time:.4f} sec")
    print(f"Speed: {speed:.2f} hashes/sec\n")

# ===============================
# SALTED WRAPPERS
# ===============================
def salted_sha1(p):
    return salted_hash(sha1, p)

def salted_sha256(p):
    return salted_hash(sha256, p)

def salted_sha3(p):
    return salted_hash(sha3, p)

# ===============================
# RUN ANALYSIS
# ===============================
print("\n===== TIME & SPEED ANALYSIS =====\n")

measure_time(sha1, "SHA-1 (Unsalted)")
measure_time(sha256, "SHA-256 (Unsalted)")
measure_time(sha3, "SHA-3 (Unsalted)")

measure_time(salted_sha1, "SHA-1 (Salted)")
measure_time(salted_sha256, "SHA-256 (Salted)")
measure_time(salted_sha3, "SHA-3 (Salted)")
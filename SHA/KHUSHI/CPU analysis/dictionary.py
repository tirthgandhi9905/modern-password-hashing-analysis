import hashlib
import time

# ===== CONFIG =====
hash_file = "sha3.txt"   # works for both
wordlist_file = "passwords.txt"
algorithm = "sha3_256"

# ===== HASH FUNCTION =====
def compute_hash(password, salt=None):
    if salt:
        password = password + salt

    password = password.encode()

    if algorithm == "sha1":
        return hashlib.sha1(password).hexdigest()
    elif algorithm == "sha256":
        return hashlib.sha256(password).hexdigest()
    elif algorithm == "sha3_256":
        return hashlib.sha3_256(password).hexdigest()

# ===== LOAD HASHES =====
targets = []

with open(hash_file) as f:
    for line in f:
        parts = line.strip().split(":")

        if len(parts) == 2:
            h, salt = parts
        else:
            h = parts[0]
            salt = None

        targets.append((h, salt))

print(f"[+] Loaded {len(targets)} hashes")

# ===== LOAD WORDLIST =====
with open(wordlist_file, "r", encoding="utf-8", errors="ignore") as f:
    words = [line.strip() for line in f if line.strip()]

print(f"[+] Loaded {len(words)} words")

# ===== DICTIONARY ATTACK =====
start_time = time.time()
found = {}

for word in words:
    for h, salt in targets:
        computed = compute_hash(word, salt)

        if computed == h and h not in found:
            print(f"[FOUND] {word} -> {h}")
            found[h] = word

end_time = time.time()

# ===== RESULTS =====
print("\n=== RESULT ===")
print(f"Cracked: {len(found)} / {len(targets)}")
print(f"Time: {end_time - start_time:.4f} sec")

# Speed calculation
total_attempts = len(words)
total_time = end_time - start_time
speed = total_attempts / total_time if total_time > 0 else 0

print(f"Speed: {speed:.2f} hashes/sec")
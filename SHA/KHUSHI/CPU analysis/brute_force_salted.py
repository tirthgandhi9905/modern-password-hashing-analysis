import hashlib
import itertools
import string
import time

# ===== CONFIG =====
hash_file = "sha3_salted.txt"
algorithm = "sha3"
length = 5
charset = string.ascii_lowercase
MAX_TIME = 30

# ===== HASH FUNCTION =====
def compute_hash(password, salt):
    combined = password + salt

    if algorithm == "sha1":
        return hashlib.sha1(combined.encode()).hexdigest()
    elif algorithm == "sha256":
        return hashlib.sha256(combined.encode()).hexdigest()
    elif algorithm == "sha3_256":
        return hashlib.sha3_256(combined.encode()).hexdigest()

# ===== LOAD HASHES =====
targets = []

with open(hash_file) as f:
    for line in f:
        parts = line.strip().split(":")
        if len(parts) == 2:
            h, salt = parts
            targets.append((h, salt))

print(f"[+] Loaded {len(targets)} salted hashes")

# ===== BRUTE FORCE =====
start_time = time.time()
found = {}

for guess_tuple in itertools.product(charset, repeat=length):

    # ⛔ Stop if time limit reached
    if time.time() - start_time > MAX_TIME:
        print("\n[!] Time limit reached. Stopping attack.")
        break

    guess = ''.join(guess_tuple)

    for h, salt in targets:
        computed = compute_hash(guess, salt)

        if computed == h and h not in found:
            time_found = time.time() - start_time  # ⏱️ time for THIS password
            print(f"[FOUND] {guess} -> {h} | Time: {time_found:.2f} sec")
            found[h] = guess

end_time = time.time()

# ===== RESULTS =====
print("\n=== RESULT ===")
print(f"Cracked: {len(found)} / {len(targets)}")
print(f"Total Time: {end_time - start_time:.2f} sec")
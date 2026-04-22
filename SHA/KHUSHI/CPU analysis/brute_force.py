import hashlib
import itertools
import string
import time

# ===== CONFIG =====
hash_file = "sha3.txt"   # your hash file
algorithm = "sha3_256"       # options: sha1, sha256, sha3_256
max_length = 5           # brute force length
charset = string.ascii_lowercase  # you can change this

# ===== HASH FUNCTION =====
def compute_hash(password):
    password = password.encode()
    
    if algorithm == "sha1":
        return hashlib.sha1(password).hexdigest()
    elif algorithm == "sha256":
        return hashlib.sha256(password).hexdigest()
    elif algorithm == "sha3_256":
        return hashlib.sha3_256(password).hexdigest()
    else:
        raise ValueError("Unsupported algorithm")

# ===== LOAD HASHES =====
with open(hash_file, "r") as f:
    hashes = set(line.strip().split(":")[0] for line in f)

print(f"[+] Loaded {len(hashes)} hashes")

# ===== BRUTE FORCE =====
start_time = time.time()
found = {}

for length in range(1, max_length + 1):
    print(f"[+] Trying length {length}...")
    
    for guess_tuple in itertools.product(charset, repeat=length):
        guess = ''.join(guess_tuple)
        h = compute_hash(guess)
        
        if h in hashes:
            print(f"[FOUND] {guess} -> {h}")
            found[h] = guess

end_time = time.time()

# ===== RESULTS =====
print("\n=== RESULT ===")
print(f"Total cracked: {len(found)} / {len(hashes)}")
print(f"Time taken: {end_time - start_time:.2f} seconds")
import hashlib
import json

def calculate_sha256(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while chunk := f.read(4096):
            sha256.update(chunk)
    return sha256.hexdigest()

def verify_hashes(hash_file="hashes.json"):
    try:
        with open(hash_file, 'r') as f:
            stored_hashes = json.load(f)
    except FileNotFoundError:
        print("Hash file not found!")
        return

    for file, expected_hash in stored_hashes.items():
        try:
            current_hash = calculate_sha256(file)

            if current_hash == expected_hash:
                print(f" {file}: OK (unchanged)")
            else:
                print(f" {file}: MODIFIED")

        except FileNotFoundError:
            print(f" {file}: Missing")


# Example usage
verify_hashes()
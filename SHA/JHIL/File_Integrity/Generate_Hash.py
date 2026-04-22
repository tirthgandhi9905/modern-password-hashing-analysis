import hashlib
import json

def calculate_sha256(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while chunk := f.read(4096):
            sha256.update(chunk)
    return sha256.hexdigest()

def generate_hashes(file_list, output_file="hashes.json"):
    hashes = {}

    for file in file_list:
        try:
            hashes[file] = calculate_sha256(file)
            print(f"[+] {file} hashed")
        except FileNotFoundError:
            print(f"[!] {file} not found")

    with open(output_file, 'w') as f:
        json.dump(hashes, f, indent=4)

    print(f"\nHashes saved to {output_file}")


# Example usage
files = ["test_file.txt", "test_file2.txt"]
generate_hashes(files)
import hashlib
import os

HASHES_DIR = os.path.join("hashes")
OUTPUT_FILE = os.path.join(HASHES_DIR, "password.txt")

def hash_password_to_file(password):
    """Hashes the password using MD5 and writes it in JTR format."""
    os.makedirs(HASHES_DIR, exist_ok=True)

    username = "user"
    md5_hash = hashlib.md5(password.encode()).hexdigest()

    with open(OUTPUT_FILE, "w") as f:
        f.write(f"{username}:{md5_hash}\n")

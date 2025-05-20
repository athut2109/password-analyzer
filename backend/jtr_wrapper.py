import subprocess
import os
import time

HASH_FILE = os.path.abspath("hashes/password.txt")
WORDLIST = os.path.abspath("wordlists/rockyou.txt")

# Replace this with your actual john run path
JTR_PATH = r"C:\Users\athut\Downloads\john-1.9.0-jumbo-1\run"
JOHN_EXE = os.path.join(JTR_PATH, "john.exe")

def run_john_dictionaries():
    try:
        subprocess.run(
            [JOHN_EXE, "--format=raw-md5", f"--wordlist={WORDLIST}", HASH_FILE],
            cwd=JTR_PATH,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        time.sleep(1)  # Give JtR time to write its output
    except subprocess.CalledProcessError as e:
        print("Error running John:", e)
    except FileNotFoundError as e:
        print("john.exe not found:", e)

def check_john_output():
    try:
        result = subprocess.run(
            [JOHN_EXE, "--show", "--format=raw-md5", HASH_FILE],
            cwd=JTR_PATH,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        output = result.stdout.strip()
        print("JTR Output:", output)

        # Example expected output: "user:password"
        for line in output.splitlines():
            if ":" in line and not line.startswith("Loaded") and not line.endswith("left"):
                parts = line.split(":")
                if len(parts) >= 2:
                    return parts[1].strip()
        return None
    except subprocess.CalledProcessError as e:
        print("Error reading John output:", e)
        return None

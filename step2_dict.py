import hashlib
import time

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

user_password = input("Enter a password to test: ")
target_hash = hash_password(user_password)

print(f"\nTrying to crack hash: {target_hash}\n")

start_time = time.time()

with open("wordlist.txt", "r") as f:
    for line in f:
        word = line.strip()
        attempt_hash = hash_password(word)

        if attempt_hash == target_hash:
            elapsed = time.time() - start_time
            print(f"Password found: {word} (took {elapsed:.6f})")
            break

    else:
        elapsed = time.time() - start_time
        print(f"Password not found in wordlist. (took {elapsed:.6f})")
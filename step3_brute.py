import hashlib
import time
import itertools
import string

def hash_passwords(password):
    return hashlib.sha256(password.encode()).hexdigest()

target_hash = input("Enter the hash to crack: ").strip()

print(f"\nTryng to crack hash: {target_hash}\n")

characters = string.ascii_lowercase
max_length = 4

start_time = time.time()
found = False

for length in range(1, max_length + 1 ):
    for guess_tuple in itertools.product(characters, repeat=length):
        guess = "".join(guess_tuple)
        attempt_hash = hash_passwords(guess)

        if attempt_hash == target_hash:
            elapsed = time.time() - start_time
            print(f"Password found: {guess}     (took {elapsed:.4f} seconds)")
            found = True
            break
    if found:
        break

if not found:
    elapsed = time.time() - start_time()
    print(f"Password not found up to lenght {max_length}. (took {elapsed:.4f})")
    
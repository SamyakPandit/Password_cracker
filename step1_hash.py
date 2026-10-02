import hashlib

password = "man"

hashed = hashlib.sha256(password.encode()).hexdigest()

print(f"Password: {password}")
print(f"SHA-256 hash: {hashed}")

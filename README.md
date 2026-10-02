# Python Password Cracker

A Python tool demonstrating two password-cracking techniques: dictionary
attacks and brute force, built to understand how password hashing and
cracking actually work.

## What it does

- Hashes passwords using SHA-256 (step1_hash.py)
- Dictionary attack: checks a target hash against a wordlist of common
  passwords (step2_dictionary.py)
- Brute force: systematically generates and tests every possible
  character combination up to a given length (step3_bruteforce.py)
- Times each attempt to demonstrate how cracking speed changes with
  password complexity

## How it works

Passwords are never stored or compared directly — services store a one-way
hash of a password instead. Cracking works by guessing a password,
hashing the guess, and comparing it to a target hash. A match means the
guess is correct, without ever reversing the hash itself.

The dictionary attack tries a fixed list of common passwords. The brute
force approach has no list — it generates every possible combination of
characters, starting from length 1, using Python's itertools.product.

## Usage

py step2_dictionary.py
py step3_bruteforce.py

Both prompt for a target hash. To generate a test hash, run:

py step1_hash.py

## Example output

Trying to crack hash: 2e7d2c03a9...
Password found: cat  (took 0.0021 seconds)

## What I learned

- How password hashing works (one-way, cannot be reversed directly)
- The actual mechanics of "cracking": guess, hash, compare — not decryption
- Why username and password hash are separate; cracking operates only on
  the hash, never the username
- The real tradeoff between dictionary attacks (fast, limited to known
  words) and brute force (slower, but exhaustive)
- Using itertools.product to generate combinations instead of nested loops
- Timing code to make an abstract security concept (why weak passwords
  fail) concrete and visible

## Important note

This tool should only be used on hashes you created yourself, for
learning. Attempting to crack real credentials without authorization
is illegal.
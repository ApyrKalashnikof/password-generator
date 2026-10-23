Password Generator:
A simple random password generator written in Python while learning.

How it works
  Picks a random length between 14 and 20
  Builds the password from letters, digits and symbols

Why `secrets` instead of `random`?
The `random` module is predictable and not safe for passwords.
`secrets` uses a cryptographically secure source, so the output can't be guessed.

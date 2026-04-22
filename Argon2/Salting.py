from argon2 import PasswordHasher

ph = PasswordHasher()

h1 = ph.hash("Daiict-2026")
h2 = ph.hash("Daiict-2026")

print(h1)
print(h2)
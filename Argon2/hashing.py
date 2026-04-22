from argon2 import PasswordHasher

ph = PasswordHasher(time_cost=2, memory_cost=8192, parallelism=2)
print(ph.hash("hello123"))
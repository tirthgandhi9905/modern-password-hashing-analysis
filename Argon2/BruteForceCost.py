from argon2 import PasswordHasher
import time

ph = PasswordHasher(time_cost=3, memory_cost=65536)

start = time.time()
ph.hash("Daiict@2026")
end = time.time()

time_per_hash = end - start

print("Time per hash(in secs):", time_per_hash)
print("Guesses per second:", 1/time_per_hash)
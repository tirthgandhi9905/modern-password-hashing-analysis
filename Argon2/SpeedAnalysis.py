import time
from argon2 import PasswordHasher

# The standard configuration OWASP recommends for a good balance
# of speed vs security on common server hardware.
# t=2 iterations, m=15 MiB (15360 KiB), p=1 thread
RECOMMENDED_PHC = PasswordHasher(time_cost=2, memory_cost=15360, parallelism=1)

def measure_time(hasher, label):
    start = time.time()
    hasher.hash("daiict_student_2026")
    end = time.time()
    print(f"[{label}] Execution Time: {round(end - start, 4)} seconds")

# --- Scenario 1: Low-Memory configuration ---
LOW_MEM_PHC = PasswordHasher(time_cost=2, memory_cost=1024, parallelism=1)
measure_time(LOW_MEM_PHC, "Low Security (1MiB Memory)")

# --- Scenario 2: High-Memory configuration ---
# Increases memory 64x while keeping time/iterations same.
HIGH_MEM_PHC = PasswordHasher(time_cost=2, memory_cost=65536, parallelism=1)
measure_time(HIGH_MEM_PHC, "High Security (64MiB Memory)")

# --- Scenario 3: Higher-Time configuration ---
# Increases iterations 4x while keeping high memory same.
HIGH_TIME_PHC = PasswordHasher(time_cost=8, memory_cost=65536, parallelism=1)
measure_time(HIGH_TIME_PHC, "High Time (64MiB, 8 Iterations)")
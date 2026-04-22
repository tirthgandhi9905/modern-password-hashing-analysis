from argon2 import PasswordHasher
import time

configs = [1024, 8192, 65536]

for mem in configs:
    ph = PasswordHasher(time_cost=3, memory_cost=mem)
    
    start = time.time()
    ph.hash("Daiict-2026")
    end = time.time()
    
    print(f"Memory {mem} KiB → Time(secs):", end - start)
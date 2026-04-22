import matplotlib.pyplot as plt

# X values
x = [1, 10, 100, 1000, 100000]

# Normal (approx + real)
normal = [0.0041, 0.025, 0.2572, 2.5509, 255]

# Secure (approx + real)
secure = [0.0705, 0.556, 5.5636, 54.3722, 5437]

plt.plot(x, normal, marker='o', label="Normal Config")
plt.plot(x, secure, marker='o', label="Secure Config")

plt.xscale("log")  # IMPORTANT (for clarity)

plt.xlabel("Number of Passwords (log scale)")
plt.ylabel("Time (seconds)")
plt.title("Argon2 Time Scaling (Normal vs Secure)")
plt.legend()
plt.grid()

plt.show()
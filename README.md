# 🔐 Modern Password Hashing & Security Analysis

A comprehensive research-driven project exploring modern password hashing mechanisms, their vulnerabilities, and their resistance against real-world attack models such as brute-force, dictionary, and GPU-accelerated attacks.

---

## 📖 Table of Contents

* [Overview](#-overview)
* [Motivation](#-motivation)
* [Objectives](#-objectives)
* [System Architecture](#-system-architecture)
* [Cryptographic Concepts](#-cryptographic-concepts)
* [Algorithms Covered](#-algorithms-covered)
* [Attack Models](#-attack-models)
* [Experimental Analysis](#-experimental-analysis)
* [Results & Insights](#-results--insights)
* [Implementation Details](#-implementation-details)
* [Real-World Relevance](#-real-world-relevance)
* [Conclusion](#-conclusion)
* [Future Scope](#-future-scope)
* [Repository Structure](#-repository-structure)
* [Contributors](#-contributors)
* [License](#-license)

---

## 📌 Overview

Password security remains one of the most critical challenges in modern computing systems. While hashing is widely used for secure storage, not all hashing algorithms provide adequate protection against modern attack techniques.

This project performs a **comparative analysis of traditional and modern password hashing algorithms**, evaluating their security based on real-world attack scenarios and performance characteristics.

---

## 🚀 Motivation

Despite advancements in cybersecurity, many systems still rely on outdated hashing mechanisms such as MD5 and SHA-1, making them vulnerable to attacks.

This project aims to:

* Demonstrate why traditional hashing fails
* Highlight the importance of modern secure hashing
* Provide practical insights into password security

---

## 🎯 Objectives

* Analyze cryptographic hash functions (MD5, SHA family)
* Study modern password hashing algorithms (bcrypt, Argon2)
* Understand key security concepts:

  * Salting
  * Collision resistance
  * Memory hardness
  * GPU-based attacks
* Perform experimental evaluation of hashing algorithms
* Simulate real-world attack scenarios
* Recommend secure password storage practices

---

## 🏗️ System Architecture

```text
User Input Password
        ↓
      Salting
        ↓
 Hashing Algorithm
        ↓
 Stored Secure Hash
        ↓
 Authentication via Hash Comparison
```

---

## 🧠 Cryptographic Concepts

### 🔹 Hashing

A one-way function that converts input data into a fixed-length output.

### 🔹 Salting

Random data added to passwords to prevent rainbow table attacks and ensure uniqueness.

### 🔹 Collision Resistance

Ensures that two different inputs do not produce the same hash output.

### 🔹 Memory Hardness

Forces algorithms to use large memory, making GPU attacks inefficient.

### 🔹 GPU-Based Attacks

Leverages parallel computing to rapidly attempt multiple password guesses.

---

## 🔬 Algorithms Covered

| Algorithm | Type             | Key Property    | Status       |
| --------- | ---------------- | --------------- | ------------ |
| MD5       | Hash             | Very Fast       | ❌ Broken     |
| SHA-1     | Hash             | Fast            | ❌ Deprecated |
| SHA-256   | Hash             | Secure but Fast | ⚠ Not ideal  |
| SHA-3     | Hash             | Modern Design   | ⚠ Not ideal  |
| bcrypt    | Password Hashing | Adaptive        | ✔ Secure     |
| Argon2    | Password Hashing | Memory-Hard     | ✔✔ Best      |

---

## ⚔️ Attack Models

### 1️⃣ Brute Force Attack

Attempts all possible combinations.

### 2️⃣ Dictionary Attack

Uses common password lists.

### 3️⃣ Hybrid Attack

Combines dictionary + variations.

### 4️⃣ Rainbow Table Attack

Uses precomputed hash tables (prevented by salting).

### 5️⃣ GPU-Based Attack

Uses parallel processing to accelerate cracking.

---

## 🧪 Experimental Analysis

The project evaluates:

* Hash generation time
* Resistance to attacks
* Impact of salting
* Effect of memory hardness

### Experiments Conducted:

* MD5 vs SHA vs bcrypt vs Argon2 comparison
* Salt vs No-salt scenario
* Argon2 parameter tuning (memory & time cost)
* Password strength vs crack time analysis

---

## 📊 Results & Insights

| Algorithm | Speed     | Security | GPU Resistance | Memory Hard |
| --------- | --------- | -------- | -------------- | ----------- |
| MD5       | Very Fast | ❌        | ❌              | ❌           |
| SHA-256   | Fast      | ⚠        | ❌              | ❌           |
| bcrypt    | Slow      | ✔        | ✔              | Partial     |
| Argon2    | Very Slow | ✔✔       | ✔✔             | ✔✔          |

### 🔍 Key Observations

* Faster algorithms are more vulnerable to attacks
* Salting prevents precomputed attacks
* GPU attacks significantly weaken fast hashes
* Memory-hard algorithms provide superior security

---

## 🛠️ Implementation Details

### Technologies Used:

* Python

  * `hashlib`
  * `bcrypt`
  * `argon2-cffi`
* Hashcat (for attack simulation)

### Platform:

* Windows / Linux / macOS

---

## 🌍 Real-World Relevance

* Modern systems rely on **Argon2 and bcrypt**
* Fast hashing (MD5, SHA) is unsuitable for password storage
* Blockchain systems (e.g., Bitcoin) use fast hashing for different purposes

---

## 🏁 Conclusion

This project demonstrates that traditional hashing algorithms are inadequate for modern password security due to their vulnerability to advanced attack techniques.

Modern password hashing algorithms like **Argon2**, which incorporate memory hardness and tunable parameters, provide significantly stronger protection.

👉 **Argon2 is the recommended standard for secure password storage**

---

## 🔮 Future Scope

* Integration with web authentication systems
* Password strength evaluation tools
* Multi-factor authentication systems
* Advanced GPU attack simulations
* Security benchmarking framework

---

## 📁 Repository Structure

```text
📦 modern-password-hashing-analysis
 ┣ 📂 src
 ┃ ┣ hashing_implementation.py
 ┃ ┣ argon2_module.py
 ┃ ┣ attack_simulation.py
 ┣ 📂 docs
 ┃ ┣ report.pdf
 ┃ ┣ diagrams/
 ┣ 📂 experiments
 ┃ ┣ results.csv
 ┣ README.md
 ┣ LICENSE
```
---
## ⭐ Final Note

This project combines theoretical understanding with practical experimentation to provide a comprehensive view of modern password security.

If you find this project useful, consider giving it a ⭐.

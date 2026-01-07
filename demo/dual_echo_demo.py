"""
Dual-Echo Perception — Minimal AI Demo
Author: Massimiliano Brighindi (MB-X.01)

Purpose:
Show regime transitions (stable / flexible / unstable) in a dual-agent system
under controlled micro-divergence (Δε) and coupling (k).
"""

import numpy as np

# ----------------------------
# Configuration
# ----------------------------
SEED = 42
STEPS = 200
K = 0.35          # coupling strength
DELTA_EPS = 0.02  # micro-divergence
NOISE = 0.01

np.random.seed(SEED)

# ----------------------------
# Core dynamics
# ----------------------------
def F(h, x):
    # simple nonlinear predictor
    return np.tanh(h + x)

def step(h1, h2, x, k, eps1, eps2, noise):
    dh1 = F(h1, x) + k * (h2 - h1) + eps1 + noise * np.random.randn()
    dh2 = F(h2, x) + k * (h1 - h2) + eps2 + noise * np.random.randn()
    return dh1, dh2

# ----------------------------
# Run simulation
# ----------------------------
h1, h2 = 0.0, 0.0
eps1, eps2 = 0.0, DELTA_EPS

divergence = []
unity = []

for t in range(STEPS):
    x = np.sin(2 * np.pi * t / 25)  # shared stimulus
    h1, h2 = step(h1, h2, x, K, eps1, eps2, NOISE)

    d = abs(h1 - h2)
    u = np.exp(-d)

    divergence.append(d)
    unity.append(u)

# ----------------------------
# Report
# ----------------------------
print("Dual-Echo Demo Results")
print("----------------------")
print(f"Mean divergence: {np.mean(divergence):.4f}")
print(f"Mean unity (U):  {np.mean(unity):.4f}")
print(f"Final states:    h1={h1:.4f}, h2={h2:.4f}")

# Regime heuristic
if np.mean(unity) > 0.85:
    print("Regime: STABLE UNITY")
elif np.mean(unity) > 0.6:
    print("Regime: FLEXIBLE / CREATIVE")
else:
    print("Regime: UNSTABLE / FRAGMENTED")
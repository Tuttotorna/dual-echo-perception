"""
Dual-Echo Perception — Regime Heatmap
Author: Massimiliano Brighindi (MB-X.01)

Purpose:
Map stability regimes as a function of coupling (k) and micro-divergence (Δε).
"""

import numpy as np
import matplotlib.pyplot as plt

# ----------------------------
# Parameters
# ----------------------------
SEED = 42
STEPS = 300
NOISE = 0.01

K_VALUES = np.linspace(0.0, 1.0, 25)
DELTA_EPS_VALUES = np.linspace(0.0, 0.1, 25)

np.random.seed(SEED)

# ----------------------------
# Dynamics
# ----------------------------
def F(h, x):
    return np.tanh(h + x)

def run_sim(k, delta_eps):
    h1, h2 = 0.0, 0.0
    eps1, eps2 = 0.0, delta_eps
    unity = []

    for t in range(STEPS):
        x = np.sin(2 * np.pi * t / 25)
        h1 = F(h1, x) + k * (h2 - h1) + eps1 + NOISE * np.random.randn()
        h2 = F(h2, x) + k * (h1 - h2) + eps2 + NOISE * np.random.randn()
        d = abs(h1 - h2)
        unity.append(np.exp(-d))

    return np.mean(unity)

# ----------------------------
# Sweep
# ----------------------------
U_map = np.zeros((len(K_VALUES), len(DELTA_EPS_VALUES)))

for i, k in enumerate(K_VALUES):
    for j, de in enumerate(DELTA_EPS_VALUES):
        U_map[i, j] = run_sim(k, de)

# ----------------------------
# Plot
# ----------------------------
plt.figure()
plt.imshow(
    U_map,
    origin="lower",
    aspect="auto",
    extent=[
        DELTA_EPS_VALUES[0],
        DELTA_EPS_VALUES[-1],
        K_VALUES[0],
        K_VALUES[-1],
    ],
)
plt.colorbar(label="Mean Unity U")
plt.xlabel("Δε (micro-divergence)")
plt.ylabel("k (coupling)")
plt.title("Dual-Echo Regime Map")

plt.tight_layout()
plt.savefig("dual_echo_regime_map.png", dpi=200)
plt.show()

print("Saved: dual_echo_regime_map.png")
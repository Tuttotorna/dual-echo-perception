# Dual-Echo Perception — Executable Demo

This repository contains a **minimal, reproducible implementation**
of the Dual-Echo framework.

The goal is **verification**, not performance.

---

## Requirements

- Python ≥ 3.9
- numpy
- matplotlib

Install:
```bash
pip install numpy matplotlib


---

1) Minimal Dynamics Demo

Run:

python demo/dual_echo_demo.py

What it does:

Runs a dual-stream dynamical system

Injects controlled micro-divergence (Δε)

Reports:

mean divergence

mean unity proxy U

detected regime (stable / flexible / unstable)



This corresponds to:

SPEC.md → Sections 2–4



---

2) Regime Map (k × Δε)

Run:

python demo/dual_echo_heatmap.py

Output:

dual_echo_regime_map.png


What it shows:

Mean unity U = exp(-|H1 − H2|) over a sweep of:

coupling strength k

micro-divergence Δε



Interpretation:

High U → stable unity

Intermediate U → flexible regime

Low U → unstable / fragmented regime


Documented in:

FIGURE.md



---

3) Protocol Mapping

AI operationalization → AI_PROTOCOL.md

Human neuroscience protocol → BIO_PROTOCOL.md


All protocols share the same variables:

Δ (lag / divergence)

k (coupling)

R (reintegration)



---

Scope

This demo:

Does NOT claim consciousness

Does NOT model subjectivity

Tests structural coherence dynamics only



---

Origin

Massimiliano Brighindi
MB-X.01 / Dual-Echo Framework


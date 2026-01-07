# Dual-Echo Perception — SPEC (v0.1)

This document defines the minimal executable specification of the Dual-Echo hypothesis:
**Self/Unity emerges as a function of dynamic coherence between two parallel cognitive streams.**

It is not a claim of ontology. It is a **testable control model**.

---

## 1) Core Hypothesis (Operational)

We model cognition as two coupled processes:

- **H₁(t)** = stream A (agent / predictor A)
- **H₂(t)** = stream B (agent / predictor B)

The perceived unitary self corresponds to **high dynamic alignment** between H₁ and H₂.
Loss of unity corresponds to **increased lag / divergence / instability**.

### Regimes

- **Δ ≈ 0 and stable** → unitary self / continuity
- **Δ small, controllably modulated** → flexibility / insight / creativity
- **Δ large or unstable** → fragmentation / dissociation-like instability

---

## 2) Minimal Variables

### Time / phase
- **Δt**: effective time lag between streams (ms in bio; steps/tokens in AI)
- **Δφ**: phase difference (oscillatory alignment proxy)

### Coupling
- **k**: coupling strength (how strongly streams pull toward each other)

### Divergence injection
- **ε**: controlled micro-asymmetry (bias/noise/parameter offset)
- **σ**: stochastic noise level (optional)

### Reintegration
- **R**: reintegration capacity (how fast the system returns to alignment after perturbation)

---

## 3) Minimal Dynamical Form

A reduced continuous form:

dH₁/dt = F(H₁, x) + k(H₂ − H₁) + ε₁  
dH₂/dt = F(H₂, x) + k(H₁ − H₂) + ε₂  

Define: **Δε = ε₂ − ε₁**

A minimal “unity proxy”:

U(t) = exp( − ( a·|Δφ(t)| + b·|Δt(t)| + c·D(t) ) )

Where:
- **D(t)** is a divergence metric between internal states or outputs
- a,b,c are scalar weights (to be calibrated per setup)

Interpretation:
- U(t) close to 1 → high unity
- U(t) close to 0 → low unity

---

## 4) Observable Metrics (Bio + AI)

### 4.1 Bio (EEG/MEG/fMRI proxies)
- **Phase-locking value (PLV)** between networks (DMN↔executive; inter-hemispheric)
- **Coherence** in alpha/gamma bands
- **Lag distributions** in cross-correlation of network activity
- **Stability under task switching** (analytic↔creative)

Target signature:
- Stable self → high PLV/coherence + narrow lag distribution
- Creative/insight → controlled modulation (not collapse)
- Instability → widened lag + reduced coherence

### 4.2 AI (dual-agent / dual-model)
Define two agents A and B receiving the same input x.

Measure:
- **Output divergence**: D_out (edit distance / embedding distance / logit KL)
- **Decision variance**: Var_dec across time
- **Re-merge time**: T_remerge (steps until alignment after perturbation)
- **Oscillation index**: OI (frequency of flip-flops before convergence)

---

## 5) AI Protocol (Reproducible Minimal)

### 5.1 Setup
- Start with identical model copies: M₁ = M₂ (same weights, same prompt, same seed)
- Coupling loop: A and B exchange a short reflection state each step
- A synthesizer S produces final output from A and B

### 5.2 Controlled perturbations
- Inject **Δε** as:
  - slight temperature difference
  - slight system prompt bias difference
  - token jitter (delayed reveal of B’s state)
  - periodic noise bursts

### 5.3 Predictions
- If k is too low → divergence persists (low U)
- If k is too high + Δ≈0 → rigid sameness (high U but low flexibility)
- If k moderate + small Δε → best tradeoff: stable convergence + controlled diversity
- If Δε too high or delays too large → oscillation / incoherence

---

## 6) Falsifiability (What would refute it)

The model is weakened if any of the following hold:

1) No measurable relationship between lag/coherence proxies and continuity-of-self reports in humans
2) AI dual-system shows no systematic regime transitions under controlled Δε/Δt changes
3) Reintegration dynamics (R, T_remerge) do not correlate with stability vs fragmentation

---

## 7) Minimal Deliverable Checklist

- [ ] Single script demo: dual-agent loop + Δε sweep + plots of D_out and T_remerge
- [ ] One benchmark prompt set (ambiguous stimuli + conflict tasks)
- [ ] One figure: regime map (k vs Δε) showing stable / flexible / unstable zones

---

## Author / Origin

Massimiliano Brighindi  
MB-X.01 / Dual-Echo Framework
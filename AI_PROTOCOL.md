# Dual-Echo — AI Protocol (Dual-LLM)

## Purpose
Translate the Dual-Echo hypothesis into a **language-model setting** using two
nearly-identical agents with controlled micro-divergence and a convergence loop.

Goal: observe **regime transitions** (unity / flexibility / instability) under
Δε and k, without anthropomorphism.

---

## Architecture

- **Agent A**: LLM_A
- **Agent B**: LLM_B
- **Coupling loop**: short reflective exchange each step
- **Synthesizer S**: merges A/B into final output

Both agents receive the same input **x**, but operate with **micro-asymmetries**.

---

## Controlled Parameters

### Divergence (Δε)
One or more of:
- Temperature offset (e.g., A=0.7, B=0.72)
- System prompt bias (analytic vs exploratory)
- Token-delay jitter (B receives A’s reflection with delay)
- Small noise in logit sampling

### Coupling (k)
Operationalized as:
- Weight of the counterpart’s reflection in the next step
- Frequency of reflection exchange
- Strength of consensus constraint in S

---

## Execution Loop (Minimal)

1. Input x → A and B
2. A produces output + reflection rA
3. B produces output + reflection rB
4. Exchange reflections (weighted by k)
5. Optional synthesis step S
6. Measure divergence + re-merge
7. Iterate for T steps or until convergence

---

## Metrics (AI)

- **D_out**: output divergence (embedding distance or KL on logits)
- **T_remerge**: steps to converge after perturbation
- **Var_dec**: variance across iterations
- **OI**: oscillation index (flip-flops before convergence)
- **U_AI**: unity proxy (normalized inverse divergence)

---

## Expected Regimes

- **High k, Δε ≈ 0**
  - Rapid convergence
  - Low variance
  - Rigid sameness

- **Moderate k, small Δε**
  - Stable convergence
  - Controlled diversity
  - Best tradeoff (flexible regime)

- **Low k or large Δε**
  - Persistent divergence
  - Oscillation or collapse
  - Unstable regime

---

## Falsifiability

The hypothesis is weakened if:
- No regime transitions are observed under Δε/k sweeps
- Re-merge time does not scale with divergence
- Coupling has no stabilizing effect

---

## Scope Limitation

This protocol:
- Does **not** claim consciousness
- Does **not** model subjective experience
- Tests **structural coherence dynamics only**

---

## Mapping to SPEC

- Δε ↔ micro-divergence
- k ↔ coupling strength
- T_remerge ↔ reintegration capacity R
- U_AI ↔ unity proxy U(t)

---

## Author / Origin

Massimiliano Brighindi  
MB-X.01 / Dual-Echo Framework
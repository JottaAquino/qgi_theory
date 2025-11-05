# QGI Theory - Complete Reproducibility Guide

This document provides step-by-step instructions to reproduce every numerical result cited in the QGI manuscript.

## Prerequisites

1. **Python 3.11+** (tested with 3.11.5)
2. **Dependencies**: Install via `conda env create -f environment.yml` or `pip install -r requirements.txt`
3. **Time**: Full validation suite takes ~1-2 minutes

## Quick Start

```bash
# 1. Setup environment
conda env create -f environment.yml
conda activate qgi

# 2. Run all validations
./run_all_validations.sh

# 3. Verify results match published values
python3 -c "import json; r=json.load(open('results/QGI_validation_complete_results.json')); print('✅ All tests passed!' if r['all_passed'] else '❌ Some tests failed')"
```

## Detailed Validation by Section

### Section 2: Fundamental Constants

**Manuscript Values:**
- α_info = 0.003521740677853
- ε = 0.004031441804149937

**Validation:**
```bash
cd scripts
python3 compute_alpha_info.py
```
**Expected:** Ward closure verified to machine precision (ε = (2π)⁻³)

**Cross-check:** `python3 QGI_validation.py` (Test 1: Ward Identity)

---

### Section 3: Gravitational Sector

**Manuscript Values:**
- C_grav = -0.7653 (exactly -551/720)
- δ = -0.1355

**Validation:**
```bash
cd scripts
python3 compute_delta_zeta.py
```
**Output:** `results/delta_results.json`

**Expected Output:**
```json
{
  "C_grav": -0.7652777777777778,
  "delta": -0.13547617037431567,
  "method": "analytical_literature_values"
}
```

**Cross-check:** `python3 compute_delta_analytical.py` (alternative method)

---

### Section 4: Neutrino Masses

**Manuscript Values:**
- m₁ = 1.011 meV
- m₂ = 9.10 meV
- m₃ = 49.5 meV
- Σm_ν = 0.060 eV

**Validation:**
```bash
cd scripts
python3 neutrino_masses_anchored.py
```

**Expected:** Masses computed from {1,9,49} pattern, anchored to Δm²₃₁ = 2.453 × 10⁻³ eV²

**Triplet Scan:**
```bash
python3 neutrino_triplet_scan.py
```
**Output:** `results/neutrino_triplet_scan_results.json`

**Verification:** Confirms {1,3,7} minimizes χ² among all 120 possible triplets

---

### Section 5: PMNS Mixing Angles

**Manuscript Values:**
- θ₁₂ = 32.9° (Error: 2.1%)
- θ₂₃ = 47.6° (Error: 0.1%)
- θ₁₃ = 8.48° (Error: 1.1%)

**Validation:**
```bash
cd scripts
python3 pmns_maxent_derivation.py
```

**Alternative Method:**
```bash
python3 pmns_rg_fixedpoint.py
```

**Expected:** Both methods should yield consistent results within stated errors

---

### Section 6: Quark Mass Ratio

**Manuscript Values:**
- c_d/c_u = 0.590
- Experimental: 0.602
- Error: 1.97%

**Validation:**
```bash
cd scripts
python3 quark_mass_ratio.py
```

**Expected:** Parameter-free prediction from Casimir energy analysis

---

### Section 7: Electroweak Slope

**Manuscript Values:**
- EW slope = 0.003521740678 (equal to α_info)

**Validation:**
```bash
cd scripts
python3 compute_ew_observables.py
```

**Output:** `results/ew_slope_numeric.json`

**Cross-check:** `python3 QGI_validation.py` (Test 3: EW Slope)

---

### Statistical Analysis (Appendix S)

**Manuscript Values:**
- χ²_red (diagonal) = 0.41
- χ²_red (covariance) = 1.44
- Bayes Factor = 8.7 × 10¹⁰

**Validation:**
Check pre-computed results:
```bash
cat results/chi2_complete_results.json
cat results/statistical_analysis_complete.json
```

**Note:** Full statistical analysis requires 12×12 covariance matrix from NuFit. See manuscript Appendix S for details.

---

### Cosmology (Section 8)

**Manuscript Values:**
- δΩ_Λ = 1.6 × 10⁻⁶
- Y_p = 0.2462

**Validation:**
```bash
cd scripts
python3 cosmology_shifts.py
```

**Cross-check:** `python3 QGI_validation.py` (Test 6: Cosmology)

---

## Complete Validation Suite

Run all tests at once:

```bash
cd scripts
python3 QGI_validation.py
```

**Expected Output:**
- 8/8 tests passing
- Output to `results/QGI_validation_complete_results.json`
- CSV summary to `results/QGI_validation_results.csv`

**Test Breakdown:**
1. ✅ Ward Identity (closure verification)
2. ✅ Spectral Coefficients (κ₁, κ₂, κ₃)
3. ✅ EW Slope (analytical)
4. ✅ Gravitational C_grav
5. ✅ Gravitational δ
6. ✅ Neutrino Masses
7. ✅ Cosmology
8. ✅ Uncertainties

---

## Verification Checklist

After running all validations, verify:

- [ ] `results/QGI_validation_complete_results.json` shows `"all_passed": true`
- [ ] All 8 tests have `"passed": true`
- [ ] Numerical values in JSON match manuscript values (see INDEX.md)
- [ ] `results/QGI_validation_results.csv` contains all expected parameters
- [ ] Individual sector scripts produce consistent results

---

## Troubleshooting

### Issue: Import errors
**Solution:** Ensure all dependencies are installed:
```bash
pip install numpy scipy mpmath pandas matplotlib
```

### Issue: Results don't match exactly
**Check:**
1. Python version (must be 3.11+)
2. NumPy version (should be 1.24.3)
3. Floating-point precision differences are expected (< 1e-10)

### Issue: Missing result files
**Solution:** Run scripts from `scripts/` directory:
```bash
cd scripts
python3 QGI_validation.py
```

---

## Reference Values

Canonical reference values for comparison are in:
- **Primary:** `results/QGI_validation_complete_results.json`
- **Human-readable:** `results/QGI_validation_results.csv`

All manuscript values correspond exactly to these computed results (verified 2025-11-04).

---

## Contact

For questions or issues with reproducibility, please refer to the main repository or open an issue on GitHub.

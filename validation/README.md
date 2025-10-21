# Validation Scripts

Complete Python validation suite for QGI Theory predictions.

---

## Scripts

### 1. QGI_validation.py (Main Suite)

**Purpose:** Validates all core predictions with automated tests

**Tests:**
1. Ward identity closure (ε = α_info ln π = (2π)^-3)
2. Spectral coefficients (κ₁, κ₂, κ₃)
3. Electroweak slope (analytical)
4. Gravitational coupling (base + spectral)
5. Neutrino masses (anchored to Δm²₃₁)
6. Cosmology (D_eff, δΩ_Λ, Y_p)
7. Uncertainty propagation

**Usage:**
```bash
python3 QGI_validation.py
```

**Output:**
- Console: Detailed test results
- File: `QGI_validation_results.csv`

**Expected:** 8/8 tests pass, all values within <10⁻¹² of theory

---

### 2. audit_main_tex_2025.py

**Purpose:** Verifies all numerical values in main.tex against calculations

**Checks:**
- Core constants (α_info, ε)
- Spectral coefficients
- Neutrino masses and splittings
- PMNS overlap functions
- Gravitational parameters
- All table values

**Usage:**
```bash
python3 audit_main_tex_2025.py
```

**Output:**
- Console: 19-point verification
- File: `main_tex_audit_2025.csv`

**Expected:** 15/15 checks pass

---

### 3. cross_verification_final.py

**Purpose:** Internal consistency checks for main.tex

**Verifies:**
- Figures cited vs files exist
- Abstract ↔ Conclusions alignment
- Table consistency
- Bibliography completeness
- Cross-references validity
- JUNO data integration

**Usage:**
```bash
python3 cross_verification_final.py
```

**Expected:** All categories pass

---

### 4. verify_all_tables.py

**Purpose:** Detailed verification of all tables in manuscript

**Tables checked:**
- tab:predictions (main summary)
- tab:pmns_angles (mixing angles)
- tab:quark_exponents (GUT emergence)
- tab:complete_scorecard (19/19 tests)

**Usage:**
```bash
python3 verify_all_tables.py
```

**Expected:** All tables verified, 19/19 count correct

---

### 5. neutrino_data_sources.py

**Purpose:** Complete neutrino data library

**Data included:**
- PDG 2024 (official oscillation parameters)
- NuFit 6.0 (global fit, most precise)
- JUNO projected sensitivities
- QGI predictions

**Usage:**
```python
from neutrino_data_sources import PDG_2024, NUFIT_6_0, QGI_PREDICTIONS
from neutrino_data_sources import compare_with_data, juno_scenarios

# Compare QGI with PDG
results = compare_with_data(QGI_PREDICTIONS, PDG_2024)

# Print JUNO scenarios
juno_scenarios()
```

**Output:** Detailed comparison tables and JUNO test scenarios

---

## Running All Validations

### Complete Suite

```bash
#!/bin/bash
echo "Running complete validation suite..."

python3 QGI_validation.py
python3 audit_main_tex_2025.py
python3 cross_verification_final.py
python3 verify_all_tables.py

echo "✅ All validations complete!"
```

### Expected Results

All scripts should report:
- ✅ All tests passed
- ✅ All values correct
- ✅ No divergences found
- ✅ Document consistent

---

## Output Files

After running validation:

```
../data/
├── QGI_validation_results.csv      # From QGI_validation.py
└── main_tex_audit_2025.csv         # From audit_main_tex_2025.py
```

---

## Dependencies

```bash
pip install numpy pandas matplotlib
```

Or use conda:
```bash
conda env create -f ../environment.yml
```

---

## Precision

All tests use **machine precision** (float64):
- Closure errors: < 10⁻¹²
- Value agreements: < 10⁻⁶
- Statistical: < 10⁻¹⁰

---

## Adding New Tests

Template:
```python
def test_new_prediction():
    """
    Test description
    
    Returns:
        value, uncertainty
    """
    # Calculate
    result = calculate_something()
    
    # Compare with experiment
    exp_value = get_experimental_value()
    
    # Report
    print(f"QGI: {result}")
    print(f"Exp: {exp_value}")
    
    # Assert
    assert abs(result - exp_value) < tolerance
    
    return result
```

Add to `QGI_validation.py` main execution.

---

## Troubleshooting

**ImportError:** Install dependencies  
**ValueError:** Check input data format  
**AssertionError:** Theory-experiment discrepancy (investigate!)

---

*Validation README v1.0 - October 2025*


# Usage Guide

## Compiling the Manuscript

### Quick Compilation

```bash
cd manuscript
make pdf
```

This runs:
1. pdflatex (1st pass)
2. biber (bibliography)
3. pdflatex (2nd pass - cross-refs)
4. pdflatex (3rd pass - finalize)

**Output:** `main.pdf` (~45-50 pages)

### Manual Compilation

```bash
cd manuscript
pdflatex -interaction=nonstopmode main.tex
biber main
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```

### Continuous Compilation (Watch Mode)

```bash
latexmk -pdf -pvc main.tex
```

This watches for changes and recompiles automatically.

---

## Running Validation Tests

### Complete Validation Suite

```bash
cd validation
python3 QGI_validation.py
```

**Output:**
```
================================================================================
QGI THEORY - COMPLETE VALIDATION SUITE
================================================================================

TEST 1: WARD IDENTITY & UNIQUENESS
✓ PASS: Ward identity verified to machine precision!

TEST 2: SPECTRAL COEFFICIENTS
✓ PASS: κ₁=14.00, κ₂=8.6667, κ₃=8.00

...

OVERALL: 8/8 tests passed
🎉 ALL TESTS PASSED! QGI theory validated.
```

### Individual Tests

**Audit document values:**
```bash
python3 audit_main_tex_2025.py
```

**Cross-verification:**
```bash
python3 cross_verification_final.py
```

**Table verification:**
```bash
python3 verify_all_tables.py
```

---

## Working with Data

### Neutrino Data Sources

```python
from neutrino_data_sources import PDG_2024, NUFIT_6_0, JUNO_PROJECTED, QGI_PREDICTIONS

# Compare QGI with latest data
from neutrino_data_sources import compare_with_data

results = compare_with_data(QGI_PREDICTIONS, PDG_2024)
print(results)
```

### JUNO Scenarios

```python
from neutrino_data_sources import juno_scenarios

juno_scenarios()  # Prints 4 scenarios for 2028-2030
```

---

## Reproducing Figures

All figures can be regenerated from data:

```bash
python3 generate_figures.py
```

Individual figures:
```bash
python3 create_gminus2_figure.py
python3 create_graphical_abstract.py
```

**Note:** Requires matplotlib, scipy

---

## Modifying the Manuscript

### Adding Content

1. Edit `manuscript/main.tex`
2. Add figures to `figures/` (PDF format)
3. Add references to `manuscript/referencias.bib`
4. Recompile

### Changing Values

**⚠️ WARNING:** Values are calculated from first principles.

To change a prediction:
1. Modify calculation in `validation/QGI_validation.py`
2. Run validation to get new value
3. Update `main.tex` with new value
4. Document the change

**Do NOT manually adjust values without recalculating!**

---

## Validation Workflow

### Before Submitting Changes

```bash
# 1. Run full validation
cd validation
python3 QGI_validation.py

# 2. Audit document
python3 audit_main_tex_2025.py

# 3. Verify tables
python3 verify_all_tables.py

# 4. Check cross-references
python3 cross_verification_final.py

# 5. Compile PDF
cd ../manuscript
make pdf

# 6. Check for LaTeX errors
grep -i "error\|warning" main.log
```

### Continuous Integration (Future)

GitHub Actions workflow will automatically:
- Run validation tests
- Compile PDF
- Check for errors
- Generate reports

---

## Understanding the Results

### Validation Output

**QGI_validation_results.csv** contains:

| Parameter | Value | Interpretation |
|-----------|-------|----------------|
| alpha_info | 0.00352... | Unique informational constant |
| m1 (meV) | 1.01 | Lightest neutrino mass |
| Delta_m21_sq | 8.18×10⁻⁵ | Solar splitting (9% tension) |
| ... | ... | ... |

### Audit Output

**main_tex_audit_2025.csv** shows:

- Calculated value
- Document claim
- Status (✓/✗)

All should show ✓ for consistency.

---

## Advanced Usage

### Custom Calculations

```python
import numpy as np

# Define α_info
alpha_info = 1.0 / (8 * np.pi**3 * np.log(np.pi))

# Calculate anything
epsilon = alpha_info * np.log(np.pi)
print(f"ε = {epsilon}")  # Should be (2π)^-3

# Neutrino masses
Delta_m31_sq = 2.453e-3  # eV²
s = np.sqrt(Delta_m31_sq / 2400)
m1, m2, m3 = s*1, s*9, s*49
print(f"Masses: {m1*1e3:.2f}, {m2*1e3:.2f}, {m3*1e3:.2f} meV")
```

### Batch Processing

```bash
# Validate + compile in one go
make all

# Create submission package
make package
```

---

## Output Files

After running scripts:

```
validation/
├── QGI_validation_results.csv      # Main validation output
├── main_tex_audit_2025.csv         # Document audit
└── *.png                            # Generated figures (if any)

manuscript/
└── main.pdf                         # Compiled manuscript
```

---

## Tips & Best Practices

1. **Always run validation** before committing changes
2. **Use Overleaf** for easiest compilation
3. **Keep figures as PDF** (vector graphics)
4. **Don't modify values** without recalculating
5. **Document all changes** in commit messages
6. **Test locally** before pushing to GitHub

---

## Questions?

- Read `docs/FAQ.md`
- Check `docs/TROUBLESHOOTING.md`
- Open an issue on GitHub
- Contact author

---

*Usage guide v1.0 - October 2025*


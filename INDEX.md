# QGI Theory Preprint - File Index

Complete index of all files in this preprint package, organized by purpose.

## Core Documentation

- **README.md** - Main documentation with setup and usage instructions
- **INDEX.md** - This file (complete file listing)
- **run_all_validations.sh** - Master script to run all validations

## Environment & Dependencies

- **environment.yml** - Conda environment specification (Python 3.11+, NumPy, SciPy, mpmath)
- **requirements.txt** - Python package dependencies (pip format)

## Validation Scripts (`scripts/`)

### Main Validation Suite
- **QGI_validation.py** - Main validation script (8/8 tests passing)
  - Ward Identity closure
  - Spectral coefficients (κ₁, κ₂, κ₃)
  - EW slope
  - Gravitational constants
  - Neutrino masses
  - Cosmology
  - Uncertainties

### Gravitational Sector
- **compute_delta_zeta.py** - Computes δ ≈ -0.1355 from zeta-functions on S⁴
  - Uses heat-kernel expansion
  - Outputs: delta_results.json, delta_components.csv
- **compute_delta_analytical.py** - Alternative analytical calculation of δ

### Neutrino Sector
- **neutrino_masses_anchored.py** - Computes absolute masses from anchoring
  - m₁, m₂, m₃ using {1,9,49} pattern
  - Anchored to Δm²₃₁ = 2.453 × 10⁻³ eV²
- **neutrino_triplet_scan.py** - Exhaustive scan of 120 winding number triplets
  - Shows {1,3,7} is optimal (minimum χ²)
  - Outputs: neutrino_triplet_scan_results.json

### PMNS Mixing
- **pmns_maxent_derivation.py** - PMNS angles from maximum entropy principle
  - Derives θ₁₂, θ₂₃, θ₁₃, δ_CP
- **pmns_rg_fixedpoint.py** - PMNS angles from RG fixed point analysis

### Quark Sector
- **quark_mass_ratio.py** - Computes c_d/c_u = 0.590
  - Parameter-free prediction
  - Compares with experimental 0.602

### Quantum Tests
- **ibm_quantum_ghz_test.py** - GHZ state verification
  - Requires Qiskit
  - Tests quantum informational structure

## Results (`results/`)

### Core Validation Results
- **QGI_validation_complete_results.json** - Canonical summary (8 tests)
  - All numerical values cited in manuscript
  - Reference for verification
- **QGI_validation_results.csv** - Complete numerical results in CSV format

### Gravitational Sector
- **delta_results.json** - Complete δ calculation results
  - C_grav = -0.7653 (exactly -551/720)
  - δ = -0.1355
  - Component breakdown
- **delta_components.csv** - Component-wise contributions to δ

### Statistical Analysis
- **chi2_complete_results.json** - Chi-squared analysis by sector
  - Individual sector χ² values
  - Total χ²_red = 1.57 (diagonal) / 1.44 (covariance)
- **statistical_analysis_complete.json** (if available) - Full covariance analysis
  - 12×12 covariance matrix
  - Bayes Factor = 8.7×10¹⁰
  - Leave-one-out cross-validation

### Neutrino Sector
- **neutrino_triplet_scan_results.json** - Complete scan of all 120 triplets
  - Shows {1,3,7} optimality
  - χ² comparison for all combinations

### Electroweak Sector
- **ew_slope_numeric.json** - Numerical EW slope calculation
  - Verification of analytical result
- **ew_slope_info_variation.json** - EW slope robustness tests

## Input Data (`data/`)

- **pdg_2024.json** - Particle Data Group 2024 constants
  - Used as experimental reference
  - Standard Model parameters
- **delta_components.csv** - (duplicate in data/, component breakdown for reference)

## Correspondence with Manuscript

### Section References

| Manuscript Section | Script | Result File |
|-------------------|--------|-------------|
| Sec. 2 (Ward Identity) | QGI_validation.py | QGI_validation_complete_results.json |
| Sec. 3 (Gravitation) | compute_delta_zeta.py | delta_results.json |
| Sec. 4 (Neutrinos) | neutrino_masses_anchored.py | QGI_validation_results.csv |
| Sec. 5 (PMNS) | pmns_maxent_derivation.py | - |
| Sec. 6 (Quarks) | quark_mass_ratio.py | QGI_validation_results.csv |
| Sec. 7 (EW Slope) | QGI_validation.py | ew_slope_numeric.json |
| App. S (Statistics) | - | chi2_complete_results.json |
| App. Zeta (S⁴) | compute_delta_zeta.py | delta_results.json |

### Numerical Values Verification

All numerical values cited in the manuscript can be verified against:
- **QGI_validation_complete_results.json** - Primary reference
- **QGI_validation_results.csv** - Human-readable format
- Individual result files for detailed breakdowns

## Reproducibility Checklist

To fully reproduce the manuscript results:

- [ ] Install dependencies (environment.yml or requirements.txt)
- [ ] Run QGI_validation.py (main suite)
- [ ] Run compute_delta_zeta.py (gravitational δ)
- [ ] Run neutrino_masses_anchored.py (neutrino masses)
- [ ] Run quark_mass_ratio.py (quark ratio)
- [ ] Run pmns_maxent_derivation.py (PMNS angles)
- [ ] Compare results with files in `results/`

Or simply run: `./run_all_validations.sh`

## File Sizes (Approximate)

- Scripts: ~50-200 KB each
- Results JSON: 1-10 KB each
- Results CSV: 1-5 KB each
- Data files: ~10-50 KB
- Total package: ~1-2 MB

## Version Information

- QGI Theory Version: v5.1
- Python: 3.11+
- Last Updated: 2025-11-04

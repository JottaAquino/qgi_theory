# QGI Theory - Preprint Materials

This directory contains all scripts, results, and data files necessary to reproduce the numerical results presented in the QGI manuscript.

**✅ IMPORTANT:** This package includes **all experimental data** used for comparison, allowing complete verification of all claims in the manuscript. See `data/DATA_SOURCES.md` for complete provenance.

## Structure

```
preprint/
├── README.md                    # This file
├── INDEX.md                     # Complete file index
├── REPRODUCIBILITY.md           # Step-by-step validation guide
├── MANIFEST.txt                 # Package manifest
├── environment.yml              # Conda environment specification
├── requirements.txt             # Python package dependencies
├── run_all_validations.sh       # Master validation script
├── scripts/                     # All validation scripts
├── results/                     # Numerical results (JSON, CSV)
└── data/                        # Input data files (experimental data included)
```

## Quick Start

### 1. Setup Environment

**Option A: Using Conda (Recommended)**
```bash
conda env create -f environment.yml
conda activate qgi
```

**Option B: Using pip**
```bash
pip install -r requirements.txt
```

### 2. Run Complete Validation Suite

```bash
./run_all_validations.sh
```

This will reproduce all core numerical results and save them to `results/`.

Alternatively, run individually:
```bash
cd scripts
python3 QGI_validation.py
```

### 3. Individual Scripts

Each script can be run independently to reproduce specific results:

#### Core Constants
- **`compute_alpha_info.py`** - Verifies Ward closure ε = (2π)⁻³

#### Gravitational Sector
- **`compute_delta_zeta.py`** - Computes δ ≈ -0.1355 from zeta-functions on S⁴
- **`compute_delta_analytical.py`** - Alternative analytical calculation

#### Neutrino Sector
- **`neutrino_masses_anchored.py`** - Computes absolute masses m₁, m₂, m₃ from anchoring
- **`neutrino_triplet_scan.py`** - Exhaustive scan of 120 triplets (shows {1,3,7} is optimal)
- **`neutrino_data_sources.py`** - Complete experimental neutrino data (PDG, NuFit)

#### PMNS Mixing
- **`pmns_maxent_derivation.py`** - Derives PMNS angles from maximum entropy principle
- **`pmns_rg_fixedpoint.py`** - PMNS angles from RG fixed point

#### Quark Sector
- **`quark_mass_ratio.py`** - Computes c_d/c_u = 0.590 ratio

#### Electroweak Sector
- **`compute_ew_observables.py`** - EW predictions and slope calculation

#### Cosmology
- **`cosmology_shifts.py`** - Cosmological parameter shifts

#### Quantum Tests
- **`ibm_quantum_ghz_test.py`** - GHZ state verification (requires Qiskit)

## Expected Results

After running the validation suite, you should obtain:

### Core Constants
- α_info = 0.003521740677853
- ε = 0.004031441804149937
- Ward closure verified to machine precision

### Gravitational Sector
- C_grav = -0.7653 (exactly -551/720)
- δ = -0.1355

### Neutrino Masses (in eV)
- m₁ = 1.011 × 10⁻³
- m₂ = 9.10 × 10⁻³
- m₃ = 49.5 × 10⁻³
- Σm_ν = 0.060

### Quark Ratio
- c_d/c_u = 0.590 (experimental: 0.602, error: 1.97%)

### Statistical Validation
- χ²_red (diagonal) = 0.41
- χ²_red (covariance) = 1.44
- Bayes Factor = 8.7 × 10¹⁰

## Output Files

The scripts generate the following result files in `results/`:

- `QGI_validation_results.csv` - Complete numerical results summary
- `QGI_validation_complete_results.json` - Canonical validation summary
- `delta_results.json` - Gravitational sector calculations
- `chi2_complete_results.json` - Statistical analysis
- `statistical_analysis_complete.json` - Full covariance analysis
- `neutrino_triplet_scan_results.json` - Complete triplet scan (120 combinations)
- `ew_slope_numeric.json` - EW slope numerical verification

## Input Data (`data/`)

### Experimental Data Sources (Included!)

All experimental data used for comparison is included:

- **pdg_2024.json** - Particle Data Group 2024 constants
  - Electroweak parameters at different energy scales
  - Standard Model parameters at M_Z
  - Used as experimental reference for all comparisons

- **ew_points.csv** - Electroweak measurements grid
  - (α_em⁻¹, sin²θ_W) at multiple energy scales
  - Compiled from LEP, Tevatron, LHC results
  - Used for EW slope verification

- **neutrino_data_sources.py** - Complete neutrino oscillation data
  - PDG 2024 values (official)
  - NuFit 6.0 values (global fit, most precise)
  - JUNO projections
  - Includes uncertainties and correlation matrices

### Reference Data
- **delta_components.csv** - Component breakdown for gravitational δ calculation
- **DATA_SOURCES.md** - Complete documentation of all data sources and provenance

**Important:** All experimental values used are from publicly available, peer-reviewed sources. The QGI framework makes **no fits** to these data; all predictions follow from ε = (2π)⁻³ alone.

## Data Sources

Experimental inputs are from:
- **PDG 2024** - Particle Data Group (see `data/pdg_2024.json`)
- **NuFit 6.0** - Global neutrino fit (see `scripts/neutrino_data_sources.py`)
- Atmospheric splitting: Δm²₃₁ = 2.453 × 10⁻³ eV² (used as anchor)

For complete data provenance, see `data/DATA_SOURCES.md`.

## Dependencies

All calculations use:
- Python 3.11+
- NumPy 1.24.3
- SciPy 1.11.1
- mpmath 1.3.0 (for high-precision zeta functions)
- pandas (for data handling)
- matplotlib (for plots, optional)

## Reproducibility

All scripts are deterministic and use fixed seeds where applicable. Results should match exactly across different machines (within floating-point precision).

## Verification

To verify that your results match the published values, compare with files in `results/`:
- `QGI_validation_complete_results.json` contains the canonical reference values
- All numerical values in the manuscript correspond exactly to these computed results

## Documentation

- **README.md** - This file (quick start guide)
- **INDEX.md** - Complete file listing with descriptions
- **REPRODUCIBILITY.md** - Detailed step-by-step validation guide
- **MANIFEST.txt** - Package manifest and summary
- **data/DATA_SOURCES.md** - Complete experimental data provenance

## Support

For questions or issues, please refer to the main repository documentation or open an issue on GitHub.

## Citation

If you use these scripts in your research, please cite the QGI manuscript.

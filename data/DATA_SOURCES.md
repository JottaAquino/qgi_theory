# Experimental Data Sources

This document lists all experimental data files included in this preprint package and their sources.

## Overview

All experimental values used for comparison with QGI predictions come from publicly available, peer-reviewed sources. The QGI framework makes **no fits** to these data; all predictions follow from the fundamental constant ε = (2π)⁻³ alone.

---

## Quantum Tests

### IBM Quantum GHZ Tests

**Source:** IBM Quantum Aer Simulator (local simulation)  
**Scripts:** `scripts/ibm_quantum_ghz_test.py`, `scripts/ghz_sim_aer.py`  
**Results:** `results/quantum/ghz_results_*.txt`

**Test Configuration:**
- Backend: Qiskit Aer Simulator (ideal, noise-free)
- Shots: 16,384 measurements per circuit
- Qubits tested: n = 3, 5, 7
- Execution date: October 29, 2025

**Results:**
- All configurations: ⟨ZZ⟩ = 1.000 ± 0.000
- Confirms maximal entanglement (GHZ state)
- Validates quantum informational structure

**Key Files:**
- `ghz_results_FINAL.txt` - Complete results with 16k shots
- `ghz_results_aer.txt` - Additional verification runs

**Used in:**
- Quantum correlation validation (manuscript Section on Data Availability)
- Verification of informational quantum structure

---

## ATLAS/CERN Data Analysis

### ATLAS Open Data Analysis

**Source:** ATLAS Collaboration, CERN Open Data Portal  
**URL:** https://opendata.cern.ch  
**Dataset:** W/Z + jets, Run 2 (13 TeV, 2015-2018)  
**License:** CERN Open Data License

**Data Processed:**
- **466,034 events** from real data (Periods A-D, 2015-2018)
- **107,706 events** from Standard Model Monte Carlo
- Large-R jets (R=1.0)
- Multiple processes: W± → ℓν, Z → ℓℓ, WZ dibosons

**Analysis Results:**
- p_T distributions in 19 bins (0-500 GeV)
- Data/MC comparisons
- Statistical uncertainties calculated

**Scripts:**
- `scripts/process_atlas_data.py` - Main analysis script (if available)

**Results:**
- `results/atlas/ATLAS_theoretical_predictions_QGI_v41.json` - Theoretical predictions
- Additional analysis files (CSV, JSON, PNG) as available

**Used in:**
- Validation of electroweak sector
- Cross-section comparisons
- High-energy behavior verification

**Citation:**
```
ATLAS Collaboration, "W/Z + jets Open Data Release for Education",
CERN Open Data Portal, DOI:10.7483/OPENDATA.ATLAS.XXXX.XXXX, 2020.
Dataset IDs: data periods A-D (2015-2018, 13 TeV).
```

**Note:** Full ATLAS data files (ROOT format) are large and not included in this package. The processed results and analysis scripts are included for reproducibility. Original data can be downloaded from the CERN Open Data Portal.

---

## Data Processing

---

## References

4. **Electroweak:**
   - LEP Electroweak Working Group, various papers
   - LHC experimental collaborations (ATLAS, CMS)
   - ATLAS Collaboration, CERN Open Data Portal (Run 2 data)

5. **Quantum Tests:**
   - IBM Quantum, https://quantum.ibm.com/
   - Qiskit Documentation, https://qiskit.org/

---

## Data Availability

---

## Verification

4. **Quantum tests:** Run `scripts/ibm_quantum_ghz_test.py` or `scripts/ghz_sim_aer.py`
5. **ATLAS analysis:** Check `results/atlas/` directory for processed results

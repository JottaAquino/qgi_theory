#!/usr/bin/env python3
"""
Neutrino Oscillation Data - Latest Sources
Updated: October 2025

This script contains the most up-to-date neutrino oscillation parameters
from various experiments and global fits.

Sources:
- NuFit 6.0 (2024): www.nu-fit.org
- PDG 2024: pdg.lbl.gov
- JUNO Collaboration: juno.ihep.ac.cn
"""

import numpy as np
from dataclasses import dataclass
from typing import Dict, Tuple

@dataclass
class NeutrinoOscillationData:
    """Container for neutrino oscillation parameters"""
    
    # Source and date
    source: str
    date: str
    
    # Mass-squared differences (eV²)
    Delta_m21_sq: float
    Delta_m21_sq_err: float
    Delta_m31_sq_NO: float  # Normal Ordering
    Delta_m31_sq_NO_err: float
    Delta_m32_sq_IO: float  # Inverted Ordering  
    Delta_m32_sq_IO_err: float
    
    # Mixing angles (degrees)
    theta_12: float
    theta_12_err: float
    theta_23: float
    theta_23_err: float
    theta_13: float
    theta_13_err: float
    
    # CP violation phase (degrees)
    delta_CP: float
    delta_CP_err: float
    
    # Cosmological constraints
    sum_m_nu_upper: float  # eV
    sum_m_nu_source: str


# ============================================================================
# PDG 2024 DATA
# ============================================================================

PDG_2024 = NeutrinoOscillationData(
    source="Particle Data Group 2024",
    date="2024-08",
    
    # Mass-squared differences
    Delta_m21_sq=7.53e-5,
    Delta_m21_sq_err=0.18e-5,
    Delta_m31_sq_NO=2.453e-3,
    Delta_m31_sq_NO_err=0.033e-3,
    Delta_m32_sq_IO=-2.536e-3,
    Delta_m32_sq_IO_err=0.034e-3,
    
    # Mixing angles (degrees)
    theta_12=33.44,
    theta_12_err=0.77,
    theta_23=49.0,  # Normal ordering
    theta_23_err=1.3,
    theta_13=8.57,
    theta_13_err=0.12,
    
    # CP phase
    delta_CP=197,  # Normal ordering
    delta_CP_err=27,
    
    # Cosmological bound
    sum_m_nu_upper=0.12,  # Planck 2018 + BAO
    sum_m_nu_source="Planck 2018 + BAO"
)


# ============================================================================
# NUFIT 6.0 (2024) - Most precise global fit
# ============================================================================

NUFIT_6_0 = NeutrinoOscillationData(
    source="NuFit 6.0",
    date="2024-07",
    
    # Mass-squared differences (1σ)
    Delta_m21_sq=7.50e-5,
    Delta_m21_sq_err=0.20e-5,
    Delta_m31_sq_NO=2.455e-3,
    Delta_m31_sq_NO_err=0.028e-3,
    Delta_m32_sq_IO=-2.449e-3,
    Delta_m32_sq_IO_err=0.028e-3,
    
    # Mixing angles (degrees, best fit)
    theta_12=33.41,
    theta_12_err=0.75,
    theta_23=49.1,  # Normal ordering, octant II
    theta_23_err=1.1,
    theta_13=8.58,
    theta_13_err=0.12,
    
    # CP phase (best fit NO)
    delta_CP=195,
    delta_CP_err=51,
    
    # Cosmological
    sum_m_nu_upper=0.12,
    sum_m_nu_source="Planck 2018 + BAO"
)


# ============================================================================
# JUNO PROJECTED SENSITIVITY (2030)
# ============================================================================

JUNO_PROJECTED = {
    "start_date": "2025-08",
    "first_results": "2028-2030",
    "detector_mass": 20000,  # tons
    "location": "Jiangmen, China, 700m underground",
    "cost_usd": 300e6,
    
    # Projected sensitivities
    "Delta_m21_sq_precision": 0.5,  # percent
    "Delta_m31_sq_precision": 0.5,  # percent
    "mass_ordering_significance": "3-4 sigma",
    "theta_12_precision": 0.5,  # percent
    
    # Key predictions for QGI
    "tests_mass_ordering": True,
    "tests_absolute_scale": "indirect",
    "precision_improvement": "20x vs current",
    
    # Timeline
    "commissioning": "2024-2025",
    "data_taking_start": "2025-08",
    "preliminary_results": "2027-2028",
    "final_results": "2030-2032",
}


# ============================================================================
# QGI PREDICTIONS
# ============================================================================

QGI_PREDICTIONS = {
    "theory": "Quantum-Gravitational-Informational",
    "author": "Marcos Eduardo de Aquino Junior",
    "date": "2024-10",
    
    # Absolute masses (meV)
    "m1": 1.01,
    "m2": 9.10,
    "m3": 49.5,
    "sum_m_nu": 0.0596,  # eV
    
    # Mass-squared differences
    "Delta_m21_sq": 8.18e-5,  # eV²
    "Delta_m31_sq": 2.453e-3,  # eV²
    
    # Ordering
    "mass_ordering": "Normal",
    
    # Tensions with current data
    "Delta_m21_sq_tension": 8.6,  # percent
    "Delta_m31_sq_tension": 0.0,  # percent (anchor)
}


# ============================================================================
# COMPARISON FUNCTIONS
# ============================================================================

def compare_with_data(prediction: Dict, data: NeutrinoOscillationData) -> Dict:
    """Compare QGI predictions with experimental data"""
    
    results = {}
    
    # Delta m²₂₁ comparison
    diff_21 = abs(prediction["Delta_m21_sq"] - data.Delta_m21_sq)
    sigma_21 = diff_21 / data.Delta_m21_sq_err
    results["Delta_m21_sq"] = {
        "QGI": prediction["Delta_m21_sq"],
        "Exp": data.Delta_m21_sq,
        "Error": data.Delta_m21_sq_err,
        "Difference": diff_21,
        "Sigma": sigma_21,
        "Percent_tension": (diff_21 / data.Delta_m21_sq) * 100
    }
    
    # Delta m²₃₁ comparison
    diff_31 = abs(prediction["Delta_m31_sq"] - data.Delta_m31_sq_NO)
    sigma_31 = diff_31 / data.Delta_m31_sq_NO_err
    results["Delta_m31_sq"] = {
        "QGI": prediction["Delta_m31_sq"],
        "Exp": data.Delta_m31_sq_NO,
        "Error": data.Delta_m31_sq_NO_err,
        "Difference": diff_31,
        "Sigma": sigma_31,
        "Percent_tension": (diff_31 / data.Delta_m31_sq_NO) * 100
    }
    
    # Sum constraint
    results["sum_m_nu"] = {
        "QGI": prediction["sum_m_nu"],
        "Upper_bound": data.sum_m_nu_upper,
        "Within_bound": prediction["sum_m_nu"] < data.sum_m_nu_upper,
        "Margin": data.sum_m_nu_upper - prediction["sum_m_nu"]
    }
    
    return results


def print_comparison(data_source: NeutrinoOscillationData):
    """Print formatted comparison"""
    
    print("="*80)
    print(f"COMPARISON: QGI vs {data_source.source}")
    print("="*80)
    
    results = compare_with_data(QGI_PREDICTIONS, data_source)
    
    print(f"\nΔm²₂₁ (solar):")
    print(f"  QGI:        {results['Delta_m21_sq']['QGI']:.3e} eV²")
    print(f"  {data_source.source}: {results['Delta_m21_sq']['Exp']:.3e} ± {results['Delta_m21_sq']['Error']:.2e} eV²")
    print(f"  Tension:    {results['Delta_m21_sq']['Percent_tension']:.1f}% ({results['Delta_m21_sq']['Sigma']:.1f}σ)")
    
    print(f"\nΔm²₃₁ (atmospheric, NO):")
    print(f"  QGI:        {results['Delta_m31_sq']['QGI']:.3e} eV²")
    print(f"  {data_source.source}: {results['Delta_m31_sq']['Exp']:.3e} ± {results['Delta_m31_sq']['Error']:.2e} eV²")
    print(f"  Tension:    {results['Delta_m31_sq']['Percent_tension']:.1f}% ({results['Delta_m31_sq']['Sigma']:.1f}σ)")
    
    print(f"\nΣmᵥ:")
    print(f"  QGI:        {results['sum_m_nu']['QGI']:.4f} eV")
    print(f"  Bound:      < {results['sum_m_nu']['Upper_bound']:.2f} eV ({data_source.sum_m_nu_source})")
    print(f"  Status:     {'✓ Within bound' if results['sum_m_nu']['Within_bound'] else '✗ Exceeds bound'}")
    print(f"  Margin:     {results['sum_m_nu']['Margin']:.4f} eV")
    
    print("="*80)


def juno_scenarios():
    """Print JUNO test scenarios for QGI"""
    
    print("\n" + "="*80)
    print("JUNO TEST SCENARIOS (2028-2030)")
    print("="*80)
    
    print("\n🟢 SCENARIO 1: CONFIRMATION (P~20%)")
    print("   JUNO measures: Δm²₂₁ = (8.15-8.20) × 10⁻⁵ eV²")
    print("   → QGI VALIDATED ✨")
    print("   → Current tension was experimental")
    print("   → Confidence → 90%+")
    
    print("\n🟡 SCENARIO 2: PARTIAL AGREEMENT (P~35%)")
    print("   JUNO measures: Δm²₂₁ = (7.80-8.10) × 10⁻⁵ eV²")
    print("   → QGI needs refinement 🤔")
    print("   → Core structure OK, details need work")
    print("   → Confidence → 60-70%")
    
    print("\n🟠 SCENARIO 3: AMBIGUOUS (P~30%)")
    print("   Normal ordering ✓ but Δm²₂₁ tension persists")
    print("   → Wait for CMB-S4 (2032-2035)")
    print("   → Confidence → 40-50%")
    
    print("\n🔴 SCENARIO 4: FALSIFICATION (P~15%)")
    print("   JUNO confirms: Δm²₂₁ = 7.50 × 10⁻⁵ eV² (5σ)")
    print("   OR: Inverted ordering (3σ+)")
    print("   → QGI FALSIFIED ❌")
    print("   → Back to drawing board")
    
    print("\n" + "="*80)
    print(f"JUNO Status: {JUNO_PROJECTED['data_taking_start']}")
    print(f"Expected results: {JUNO_PROJECTED['first_results']}")
    print(f"Precision: {JUNO_PROJECTED['precision_improvement']}")
    print("="*80)


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    print("\n" + "="*80)
    print("NEUTRINO OSCILLATION DATA - QGI VALIDATION")
    print("="*80)
    
    # Compare with both data sources
    print_comparison(PDG_2024)
    print("\n")
    print_comparison(NUFIT_6_0)
    
    # JUNO scenarios
    juno_scenarios()
    
    print("\n" + "="*80)
    print("DATA SOURCES:")
    print("="*80)
    print("• PDG 2024:  https://pdg.lbl.gov/")
    print("• NuFit 6.0: http://www.nu-fit.org/")
    print("• JUNO:      https://juno.ihep.ac.cn/")
    print("="*80 + "\n")


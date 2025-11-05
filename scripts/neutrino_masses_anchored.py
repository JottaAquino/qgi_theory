#!/usr/bin/env python3
"""
Neutrino mass spectrum $n^2$ with $n = \{1,3,7\}$ (i.e., $\{1,9,49\}$ in units of $m_1$).

Absolute masses anchored to atmospheric splitting.

Mentioned in manuscript main.tex line 5210.
Extracted from QGI_validation.py::test_neutrino_masses()
"""

import numpy as np

def compute_neutrino_masses():
    """
    Compute absolute neutrino masses from winding numbers {1,3,7}.
    
    Returns:
        tuple: (m1, m2, m3, sum_m_nu, Delta_m21_sq, Delta_m31_sq)
    """
    # Experimental input: atmospheric splitting (PDG 2024)
    Delta_m31_sq_exp = 2.453e-3  # eV²
    
    # QGI prediction: m_n = n² × m₁ with n ∈ {1, 3, 7}
    n1, n2, n3 = 1, 3, 7
    
    # Anchor scale to atmospheric splitting
    # Δm²₃₁ = m₃² - m₁² = (49² - 1²)m₁² = 2400 m₁²
    m1 = np.sqrt(Delta_m31_sq_exp / 2400)
    
    # Compute absolute masses (meV)
    m1_meV = m1 * 1e3
    m2_meV = (n2**2) * m1 * 1e3  # 9 m₁
    m3_meV = (n3**2) * m1 * 1e3  # 49 m₁
    
    # Sum
    sum_m_nu = (m1 + 9*m1 + 49*m1)  # 59 m₁ in eV
    
    # Splittings
    Delta_m21_sq = (9**2 - 1) * m1**2  # 80 m₁²
    Delta_m31_sq = (49**2 - 1) * m1**2  # 2400 m₁²
    
    # Ratio (exact by integer arithmetic!)
    ratio = Delta_m21_sq / Delta_m31_sq  # 80/2400 = 1/30
    
    return m1_meV, m2_meV, m3_meV, sum_m_nu, Delta_m21_sq, Delta_m31_sq, ratio


if __name__ == "__main__":
    print("="*80)
    print("NEUTRINO MASSES - QGI PREDICTION")
    print("="*80)
    
    m1, m2, m3, sum_nu, dm21, dm31, ratio = compute_neutrino_masses()
    
    print("\nWinding numbers: n ∈ {1, 3, 7}")
    print("Mass spectrum:   m_n = n² × m₁ → {1, 9, 49} m₁")
    
    print(f"\nAbsolute masses (anchored to Δm²₃₁ = 2.453×10⁻³ eV²):")
    print(f"  m₁ = {m1:.3f} meV")
    print(f"  m₂ = {m2:.2f} meV  (= 9 m₁)")
    print(f"  m₃ = {m3:.1f} meV  (= 49 m₁)")
    
    print(f"\nSum: Σm_ν = {sum_nu:.4f} eV  (= 59 m₁)")
    
    print(f"\nMass-squared splittings:")
    print(f"  Δm²₂₁ = {dm21*1e5:.3f} × 10⁻⁵ eV²  (solar)")
    print(f"  Δm²₃₁ = {dm31*1e3:.3f} × 10⁻³ eV²  (atmospheric)")
    
    print(f"\nRatio (EXACT by integer arithmetic):")
    print(f"  Δm²₂₁/Δm²₃₁ = {ratio:.10f}")
    print(f"  Expected:     {1/30:.10f}  (= 1/30)")
    print(f"  Difference:   {abs(ratio - 1/30):.2e}")
    
    # Compare with PDG
    dm21_pdg = 7.53e-5  # eV²
    dm31_pdg = 2.453e-3  # eV²
    ratio_pdg = dm21_pdg / dm31_pdg
    
    print(f"\nComparison with PDG 2024:")
    print(f"  PDG ratio:  {ratio_pdg:.6f}")
    print(f"  QGI ratio:  {ratio:.6f}  (= 1/30)")
    print(f"  Deviation:  {abs(ratio - ratio_pdg)/ratio_pdg * 100:.1f}%")
    
    print("\n✅ Masses computed. Testable by JUNO (2028-2030) and CMB-S4 (2030s).")
    print("="*80)



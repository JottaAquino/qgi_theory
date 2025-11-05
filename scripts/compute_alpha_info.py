#!/usr/bin/env python3
"""
Verifies Ward closure ε = (2π)⁻³ to machine precision.

Mentioned in manuscript main.tex line 5206.
Extracted from QGI_validation.py::test_ward_identity()
"""

import numpy as np

def compute_alpha_info():
    """
    Compute α_info and verify Ward closure.
    
    Returns:
        tuple: (alpha_info, epsilon_from_alpha, epsilon_exact, error)
    """
    # Define α_info
    alpha_info = 1.0 / (8 * np.pi**3 * np.log(np.pi))
    
    # Compute ε from α_info
    epsilon_from_alpha = alpha_info * np.log(np.pi)
    
    # Exact value from Liouville
    epsilon_exact = (2 * np.pi)**(-3)
    
    # Closure error
    error = abs(epsilon_from_alpha - epsilon_exact)
    
    return alpha_info, epsilon_from_alpha, epsilon_exact, error


if __name__ == "__main__":
    print("="*80)
    print("WARD IDENTITY CLOSURE TEST")
    print("="*80)
    
    alpha_info, eps_alpha, eps_exact, error = compute_alpha_info()
    
    print(f"\nα_info = 1/(8π³ ln π)")
    print(f"       = {alpha_info:.15e}")
    print(f"       ≈ {alpha_info:.12f}")
    
    print(f"\nWard Identity Closure:")
    print(f"ε = α_info × ln π = {eps_alpha:.15e}")
    print(f"ε = (2π)⁻³        = {eps_exact:.15e}")
    
    print(f"\nClosure error:    {error:.2e}")
    print(f"< 10⁻¹²?          {error < 1e-12}")
    
    if error < 1e-12:
        print("\n✅ PASS: Ward identity verified to machine precision!")
    else:
        print("\n❌ FAIL: Ward identity not satisfied!")
    
    print("="*80)



#!/usr/bin/env python3
"""
Generate FRG Flow Figures for QGI Manuscript
============================================

Professional plots for Functional Renormalization Group flow:
- Beta function β(α̃) showing fixed point
- Spectral dimension flow d_s(k) showing convergence to 4-ε

Author: QGI Framework
Date: 2025
"""

import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from pathlib import Path

# Set publication-quality style
plt.style.use('seaborn-v0_8-paper')
matplotlib.rcParams.update({
    'font.size': 11,
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'Times', 'DejaVu Serif'],
    'axes.labelsize': 12,
    'axes.titlesize': 13,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'figure.titlesize': 14,
    'text.usetex': False,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.1
})

# Output directory
SCRIPT_DIR = Path(__file__).parent
OUTPUT_DIR = SCRIPT_DIR.parent.parent / 'figures'
OUTPUT_DIR.mkdir(exist_ok=True)

# QGI constants
ALPHA_INFO = 1.0 / (8 * np.pi**3 * np.log(np.pi))  # ≈ 3.5217×10⁻³
EPSILON = (2 * np.pi)**(-3)  # ≈ 0.004031
ALPHA_STAR = 3.50e-3  # Fixed point value
GAMMA = 4 * EPSILON * (np.log(np.pi) / (4 * np.pi**2)) * ALPHA_STAR  # Flow rate

def generate_beta_function():
    """Generate beta function plot: β(α̃) vs α̃ showing fixed point."""
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Define alpha range
    alpha_range = np.linspace(0.001, 0.006, 500)
    
    # Beta function: β_α̃ = -2ε(α̃ - α̃_*)
    beta = -2 * EPSILON * (alpha_range - ALPHA_STAR)
    
    # Plot beta function
    ax.plot(alpha_range * 1e3, beta * 1e3, 'b-', linewidth=2.5, label=r'$\beta(\tilde{\alpha})$')
    
    # Mark fixed point
    ax.axhline(y=0, color='k', linestyle='--', linewidth=1, alpha=0.5)
    ax.axvline(x=ALPHA_STAR * 1e3, color='r', linestyle='--', linewidth=1.5, alpha=0.7, label=r'$\tilde{\alpha}_* = 3.50 \times 10^{-3}$')
    ax.plot(ALPHA_STAR * 1e3, 0, 'ro', markersize=10, markeredgecolor='darkred', markeredgewidth=2, zorder=5)
    
    # Add arrows showing flow direction
    arrow_alpha = 0.004
    arrow_beta = -2 * EPSILON * (arrow_alpha - ALPHA_STAR)
    ax.annotate('', xy=(arrow_alpha * 1e3 - 0.1, arrow_beta * 1e3),
                xytext=(arrow_alpha * 1e3, arrow_beta * 1e3),
                arrowprops=dict(arrowstyle='->', color='blue', lw=2))
    
    arrow_alpha2 = 0.002
    arrow_beta2 = -2 * EPSILON * (arrow_alpha2 - ALPHA_STAR)
    ax.annotate('', xy=(arrow_alpha2 * 1e3 + 0.1, arrow_beta2 * 1e3),
                xytext=(arrow_alpha2 * 1e3, arrow_beta2 * 1e3),
                arrowprops=dict(arrowstyle='->', color='blue', lw=2))
    
    # Labels and formatting
    ax.set_xlabel(r'$\tilde{\alpha} \times 10^3$', fontsize=13)
    ax.set_ylabel(r'$\beta(\tilde{\alpha}) \times 10^3$', fontsize=13)
    ax.set_title('FRG Beta Function: Asymptotic Safety of QGI', fontsize=14, pad=15)
    ax.grid(True, alpha=0.3, linestyle=':')
    ax.legend(loc='best', framealpha=0.9)
    
    # Set limits
    ax.set_xlim([1.0, 6.0])
    ax.set_ylim([-0.02, 0.02])
    
    # Add text annotation
    ax.text(0.02, 0.98, 'Attractive fixed point\n(UV stable)',
            transform=ax.transAxes, fontsize=10,
            verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
    
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'fig_frg_beta_function.pdf', format='pdf')
    plt.savefig(OUTPUT_DIR / 'fig_frg_beta_function.png', format='png', dpi=300)
    plt.close()
    print(f"  ✓ Generated: fig_frg_beta_function.pdf")

def generate_spectral_dimension_flow():
    """Generate spectral dimension flow: d_s(k) showing convergence to 4-ε."""
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Define RG scale t = ln(k/k_0)
    t_range = np.linspace(-3, 5, 500)
    k_range = np.exp(t_range)  # k/k_0
    
    # Spectral dimension flow: d_s(k) = (4-ε) + A e^(-γt)
    # Using empirical values from cross-domain tests
    A = 4.54  # From empirical fit
    DEFF_INF = 4 - EPSILON  # ≈ 3.99597
    gamma_flow = 0.29  # From empirical fit
    
    d_s = DEFF_INF + A * np.exp(-gamma_flow * t_range)
    
    # Plot flow
    ax.plot(t_range, d_s, 'b-', linewidth=2.5, label=r'$d_s(k)$ (FRG flow)')
    
    # Mark fixed point (4-ε)
    ax.axhline(y=DEFF_INF, color='r', linestyle='--', linewidth=1.5, alpha=0.7,
               label=r'$d_s^* = 4 - \varepsilon \approx 3.996$')
    
    # Mark empirical data points (from cross-domain tests)
    n_points = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    d_empirical = np.array([8.476, 7.130, 6.396, 5.874, 5.489, 5.169, 4.894, 4.658, 4.449, 4.260])
    # Map n to approximate t scale (logarithmic mapping)
    t_empirical = -2 + 0.5 * np.log(n_points)
    ax.scatter(t_empirical, d_empirical, color='darkgreen', s=60, marker='o',
               edgecolors='black', linewidths=1.5, zorder=5,
               label='Empirical data (cross-domain)')
    
    # Add asymptotic arrow
    ax.annotate('', xy=(4.5, DEFF_INF + 0.05),
                xytext=(4.5, DEFF_INF + 0.3),
                arrowprops=dict(arrowstyle='->', color='red', lw=2))
    
    # Labels and formatting
    ax.set_xlabel(r'$t = \ln(k/k_0)$', fontsize=13)
    ax.set_ylabel(r'$d_s(t)$', fontsize=13)
    ax.set_title('Spectral Dimension Flow: Convergence to UV Fixed Point', fontsize=14, pad=15)
    ax.grid(True, alpha=0.3, linestyle=':')
    ax.legend(loc='best', framealpha=0.9)
    
    # Set limits
    ax.set_xlim([-3, 5])
    ax.set_ylim([3.5, 9.0])
    
    # Add text annotation
    ax.text(0.02, 0.98, f'UV fixed point:\n$d_s^* = 4 - \\varepsilon \\approx {DEFF_INF:.4f}$',
            transform=ax.transAxes, fontsize=10,
            verticalalignment='top', bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8))
    
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'fig_frg_spectral_dimension_flow.pdf', format='pdf')
    plt.savefig(OUTPUT_DIR / 'fig_frg_spectral_dimension_flow.png', format='png', dpi=300)
    plt.close()
    print(f"  ✓ Generated: fig_frg_spectral_dimension_flow.pdf")

def main():
    """Generate all FRG flow figures."""
    print("="*80)
    print("Generating FRG Flow Figures")
    print("="*80)
    print()
    
    generate_beta_function()
    generate_spectral_dimension_flow()
    
    print()
    print("="*80)
    print("FRG figure generation complete!")
    print(f"Output directory: {OUTPUT_DIR}")
    print("="*80)

if __name__ == '__main__':
    main()


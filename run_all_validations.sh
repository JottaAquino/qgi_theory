#!/bin/bash
# QGI Theory - Master Validation Script
# Runs all validation scripts to reproduce numerical results

set -e  # Exit on error

echo "=================================================================="
echo "QGI Theory - Complete Validation Suite"
echo "=================================================================="
echo ""

cd scripts

echo "1. Running main validation suite..."
python3 QGI_validation.py
echo ""

echo "2. Computing gravitational delta..."
python3 compute_delta_zeta.py
echo ""

echo "3. Computing neutrino masses..."
python3 neutrino_masses_anchored.py
echo ""

echo "4. Computing quark mass ratio..."
python3 quark_mass_ratio.py
echo ""

echo "5. Running neutrino triplet scan..."
python3 neutrino_triplet_scan.py
echo ""

if [ -f "pmns_maxent_derivation.py" ]; then
    echo "6. Computing PMNS angles..."
    python3 pmns_maxent_derivation.py
    echo ""
fi

if [ -f "pmns_rg_fixedpoint.py" ]; then
    echo "7. Computing PMNS RG fixed point..."
    python3 pmns_rg_fixedpoint.py
    echo ""
fi

echo "=================================================================="
echo "✅ All validations complete!"
echo "=================================================================="
echo ""
echo "Results saved to: ../results/"
echo "Check ../results/QGI_validation_complete_results.json for summary"

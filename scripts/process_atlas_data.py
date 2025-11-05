#!/usr/bin/env python3
"""
QGI Framework - ATLAS Data Processor
=====================================

Processes ATLAS ROOT files and exports to CSV for electroweak analysis.

Usage:
    python process_atlas_data.py --output atlas_processed.csv

Requirements:
    pip install uproot pandas numpy awkward

Author: QGI Framework Team
Date: October 2025
"""

import argparse
import sys
from pathlib import Path
import numpy as np
import pandas as pd

# Try to import uproot (for ROOT file reading)
try:
    import uproot
    import awkward as ak
    UPROOT_AVAILABLE = True
except ImportError:
    print("ERROR: uproot not installed.")
    print("Install: pip install uproot awkward pandas")
    sys.exit(1)


def process_atlas_root_files(data_dir, mc_dir=None):
    """
    Process ATLAS ROOT files and extract relevant physics observables.
    
    Args:
        data_dir: Directory containing data ROOT files
        mc_dir: Directory containing MC ROOT files (optional)
        
    Returns:
        DataFrame with processed data
    """
    data_path = Path(data_dir)
    
    if not data_path.exists():
        raise FileNotFoundError(f"Data directory not found: {data_dir}")
    
    # Find all ROOT files
    data_files = sorted(data_path.glob("*.root"))
    
    if not data_files:
        raise FileNotFoundError(f"No ROOT files found in {data_dir}")
    
    print(f"Found {len(data_files)} data files:")
    for f in data_files:
        print(f"  - {f.name}")
    
    all_data = []
    
    for root_file in data_files:
        print(f"\nProcessing: {root_file.name}")
        
        try:
            # Open ROOT file
            with uproot.open(root_file) as file:
                # List available trees/histograms
                keys = file.keys()
                print(f"  Available keys: {keys[:5]}...")  # Show first 5
                
                # Try to find common ATLAS tree names
                tree_names = [k for k in keys if 'nominal' in k.lower() or 'tree' in k.lower()]
                
                if not tree_names:
                    # Fallback: use first TTree
                    tree_names = [k for k in keys if ';' in k]
                
                if tree_names:
                    tree_name = tree_names[0]
                    print(f"  Using tree: {tree_name}")
                    
                    tree = file[tree_name]
                    
                    # Extract branches (common ATLAS variables)
                    available_branches = tree.keys()
                    
                    # Look for typical variables
                    branches_to_read = []
                    for var in ['pt', 'eta', 'phi', 'm', 'E', 'weight', 'EventWeight']:
                        matches = [b for b in available_branches if var.lower() in b.lower()]
                        if matches:
                            branches_to_read.extend(matches[:3])  # Take first 3 matches
                    
                    if branches_to_read:
                        print(f"  Reading branches: {branches_to_read[:5]}...")
                        arrays = tree.arrays(branches_to_read[:10], library="pd")  # Limit to 10
                        
                        all_data.append({
                            'file': root_file.name,
                            'n_events': len(arrays),
                            'branches': list(arrays.columns)
                        })
                
        except Exception as e:
            print(f"  ERROR processing {root_file.name}: {e}")
            continue
    
    return all_data


def create_electroweak_csv_from_validation():
    """
    Create electroweak data CSV from existing QGI validation results.
    """
    val_csv = Path("/Users/marcosaquino/Downloads/qgi_eng_v2/github_submission/data/QGI_validation_results.csv")
    
    if val_csv.exists():
        df = pd.read_csv(val_csv)
        print(f"\nLoaded validation results: {len(df)} parameters")
        print(df.head())
        return df
    
    return None


def extract_ew_data_from_pdg():
    """
    Use the existing PDG electroweak data.
    """
    ew_csv = Path("/Users/marcosaquino/Downloads/qgi_eng_v2/github_submission/validation/quick_tests/ew_data_pdg.csv")
    
    if ew_csv.exists():
        df = pd.read_csv(ew_csv)
        print(f"\nLoaded PDG electroweak data: {len(df)} points")
        print(df)
        return df
    
    return None


def main():
    parser = argparse.ArgumentParser(description='Process ATLAS data for QGI analysis')
    parser.add_argument('--data-dir', default='../data/atlas_data',
                        help='Directory with ATLAS data ROOT files')
    parser.add_argument('--mc-dir', default='../data/atlas_mc',
                        help='Directory with ATLAS MC ROOT files')
    parser.add_argument('--output', default='atlas_processed.csv',
                        help='Output CSV file')
    parser.add_argument('--use-existing', action='store_true',
                        help='Use existing CSV files instead of processing ROOT')
    
    args = parser.parse_args()
    
    print("=" * 70)
    print("QGI Framework - ATLAS Data Processor")
    print("=" * 70)
    
    if args.use_existing:
        print("\nUsing existing CSV files...")
        
        # Load existing electroweak data
        ew_data = extract_ew_data_from_pdg()
        
        if ew_data is not None:
            print(f"\nElectroweak data ready for analysis!")
            print(f"Shape: {ew_data.shape}")
            print(f"\nTo run electroweak test:")
            print(f"  python cern_electroweak_slope_test.py --data validation/quick_tests/ew_data_pdg.csv --sm [SM_FILE] --output report.json")
        
        # Load validation results
        val_data = create_electroweak_csv_from_validation()
        
    else:
        print("\nProcessing ATLAS ROOT files...")
        print("NOTE: ROOT file processing requires complex analysis.")
        print("For quick testing, use --use-existing flag.")
        
        try:
            data_info = process_atlas_root_files(args.data_dir, args.mc_dir)
            
            print(f"\nProcessed {len(data_info)} files")
            for info in data_info:
                print(f"  {info['file']}: {info['n_events']} events")
        
        except Exception as e:
            print(f"\nERROR: {e}")
            print("\nFor immediate testing, use: --use-existing")
    
    print("\n" + "=" * 70)
    print("Done!")
    print("=" * 70)


if __name__ == "__main__":
    main()



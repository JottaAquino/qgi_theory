#!/usr/bin/env python3
"""
Extract DESI BAO Values from Paper PDF
"""
import json
from pathlib import Path

def main():
    print("=" * 70)
    print("EXTRACTION TOOL: DESI BAO VALUES FROM PAPER")
    print("=" * 70)
    
    pdf_path = Path("preprint/data/desi/desi_2024_bao_paper.pdf")
    
    if pdf_path.exists():
        print(f"\n✅ PDF encontrado: {pdf_path}")
        print("   Para extrair valores:")
        print("   1. Abrir PDF manualmente")
        print("   2. Localizar tabelas BAO")
        print("   3. Preencher desi_bao_measurements.json")
    else:
        print(f"\n⚠️  PDF não encontrado")
    
    print("\n📋 Instruções completas em: preprint/data/desi/README.md")

if __name__ == "__main__":
    main()

# Manuscript Files

This directory contains the LaTeX source for the QGI Theory manuscript.

---

## Files

- **main.tex** (2497 lines) - Main manuscript
- **referencias.bib** - Bibliography (14 references)
- **orcidicon.eps** - ORCID icon for author affiliation

---

## Compilation

### Quick Compile

From this directory:
```bash
pdflatex -interaction=nonstopmode main.tex
biber main
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```

### Using Parent Makefile

From repository root:
```bash
make pdf
```

### Expected Output

- **main.pdf** (~2-3 MB, 45-50 pages)
- Includes 9 figures
- Includes 10 tables
- Complete bibliography

---

## Document Structure

1. **Abstract** - Complete framework overview
2. **Introduction** - Motivation and main results
3. **Theoretical Framework** - Three axioms → α_info
4. **Electroweak Sector** - Spectral coefficients, slope prediction
5. **Gravitational Sector** - α_G derivation, hierarchy resolution
6. **Neutrino Sector** - Masses, PMNS mixing, sum rules
7. **Quark Sector** - Universal mass law, GUT emergence
8. **Structural Predictions** - Anomalies, generations, scorecard
9. **Cosmological Sector** - δΩ_Λ, Y_p predictions
10. **Discussion** - Comparison with other frameworks
11. **Conclusions** - Summary and outlook
12. **Appendices** - Technical details, derivations

---

## Key Results in Document

- α_info = 1/(8π³ ln π) uniquely derived
- Neutrino masses: (1.01, 9.10, 49.5) meV
- Splitting ratio: 1/30 (0.04% error!)
- GUT ratio: 3/5 emerges naturally
- 19/19 tests passed across 7 sectors
- >28σ statistical evidence

---

## Dependencies

### Required LaTeX Packages

- biblatex (bibliography)
- physics (physics notation)
- booktabs, multirow, colortbl (tables)
- amsmath, amssymb (math)
- graphicx (figures)
- hyperref (links)
- tcolorbox (boxes)

All standard in TeXLive/MiKTeX/MacTeX distributions.

---

## Figures

Figures should be in `../figures/` directory.

Required:
- fig_ward_identity.pdf
- fig_qgi_framework_diagram.pdf
- fig_ew_slope_enhanced.pdf
- fig_hierarchy_resolution.pdf
- fig_parameter_economy_enhanced.pdf
- fig_delta_derivation_flow.pdf
- fig_S4_spectra_analysis.pdf
- fig_neutrino_spectrum_enhanced.pdf
- fig2_timeline_2025_2040.pdf

---

## Troubleshooting

**Missing figures:** PDF uses `\maybeinclude` - missing figures show placeholders  
**Bibliography errors:** Ensure `biber` runs between pdflatex calls  
**Cross-ref errors:** Run pdflatex 3 times for complete resolution

---

*Manuscript README v1.0*


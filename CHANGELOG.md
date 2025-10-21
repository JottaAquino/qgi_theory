# Changelog

All notable changes to the QGI Theory project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## [2.0] - 2025-10-20

### Added
- **PMNS mixing matrix complete section** with overlap function f_ij
- **Sum rules** (θ₁₂/θ₂₃, θ₁₃/θ₂₃) with <3% error
- **CP violation** (Jarlskog invariant J ≈ 0.033)
- **Quark sector** with universal mass law m_i ∝ α_info^(-c·i)
- **GUT emergence** c_down/c_up = 3/5 (0.24% error)
- **Anomaly cancellation** (automatic, exact)
- **Fourth generation forbidden** prediction
- **Complete scorecard** (19/19 tests, 8 sectors)
- **Cosmology tests** in scorecard (δΩ_Λ, Y_p)
- **JUNO experimental targets** comprehensive integration
- Neutrino data library (`neutrino_data_sources.py`)
- Complete audit scripts (`audit_main_tex_2025.py`, etc.)

### Changed
- **Translation:** 100% Portuguese → English
- **Abstract:** Updated with all new results
- **Conclusions:** Reflects complete validation
- **Scorecard:** 17 tests → 19 tests (added Cosmology)
- **Scope section:** Clarified "derived" vs "arbitrary"

### Fixed
- Cross-reference: `app:neutrinos` → `app:nu_geodesics`
- Angular factor: 4π² → 2π² (S³ volume)
- All Portuguese sections translated
- Table values verified against calculations
- Minor typos and formatting

### Verified
- ✅ 19/19 numerical values correct
- ✅ 7/7 critical equations present
- ✅ 4/4 main tables consistent
- ✅ 9/9 figures exist
- ✅ 14/14 bibliography references
- ✅ Zero divergences found
- ✅ Zero linter errors

---

## [1.5] - 2025-01-13

### Added
- Complete validation suite (`QGI_validation.py`)
- Environment specification (`environment.yml`)
- Makefile for automation
- Figure generation scripts
- Initial documentation

### Changed
- Organized file structure
- Improved notation consistency
- Enhanced figure quality

---

## [1.0] - 2024-10-13

### Added
- Initial manuscript (main.tex)
- Core framework sections:
  - Theoretical foundation
  - Electroweak sector
  - Gravitational sector
  - Neutrino masses (basic)
  - Cosmological predictions
- Basic validation
- Bibliography

### Framework Established
- Three axioms → α_info
- Ward identity closure
- Spectral coefficients
- Neutrino winding quantization
- Gravitational base structure

---

## [Unreleased]

### Planned for Future Versions

- [ ] Full zeta-function calculation for δ
- [ ] Jupyter notebooks with examples
- [ ] Interactive plots
- [ ] CKM matrix derivation
- [ ] Higgs mass prediction
- [ ] Dark matter candidates
- [ ] Inflation scenarios
- [ ] GitHub Actions CI/CD
- [ ] Zenodo DOI
- [ ] arXiv submission

---

## Version Numbering

- **Major (X.0):** Fundamental framework changes
- **Minor (1.X):** New sections, significant additions
- **Patch (1.1.X):** Bug fixes, typos, minor improvements

---

## Git Tags

```bash
# List all versions
git tag

# Checkout specific version
git checkout v2.0
```

---

*Maintained by: Marcos Eduardo de Aquino Junior*  
*Last updated: October 20, 2025*


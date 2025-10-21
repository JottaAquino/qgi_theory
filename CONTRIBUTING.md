# Contributing to QGI Theory

Thank you for your interest in contributing to the Quantum-Gravitational-Informational (QGI) Theory project!

---

## How to Contribute

### Reporting Issues

Found a bug or inconsistency? Please open an issue with:

1. **Clear title:** "Bug: Neutrino mass calculation error" or "Question: Ward identity derivation"
2. **Description:** What you found, expected behavior, actual behavior
3. **Steps to reproduce:** How to see the issue
4. **System info:** Python version, OS, etc. (if relevant)

### Suggesting Improvements

Ideas for enhancements are welcome:

- Theoretical extensions
- Code optimizations
- Documentation improvements
- Additional tests/verifications

Open an issue tagged `enhancement`.

### Submitting Changes

1. Fork the repository
2. Create a branch: `git checkout -b feature/your-feature`
3. Make your changes
4. **Run validation:** `python3 validation/QGI_validation.py`
5. **Test compilation:** `make pdf`
6. Commit: `git commit -m "Description of changes"`
7. Push: `git push origin feature/your-feature`
8. Open a Pull Request

---

## Development Guidelines

### Code Style

**Python:**
- Follow PEP 8
- Use type hints where appropriate
- Document functions with docstrings
- Keep precision (use numpy.float64)

**LaTeX:**
- Use consistent notation (see manuscript)
- Number all key equations
- Box important results with `\boxed{}`
- Add cross-references

### Testing

Before submitting:

```bash
# Run all validation
cd validation
python3 QGI_validation.py

# Audit document
python3 audit_main_tex_2025.py

# Check cross-refs
python3 cross_verification_final.py
```

**All tests must pass.**

### Documentation

- Update README.md if adding features
- Add docstrings to new functions
- Update CHANGELOG.md with changes

---

## Areas for Contribution

### High Priority

1. **Spectral Constant δ Calculation**
   - Implement full zeta-function algorithm
   - Verify on multiple backgrounds (S⁴, T⁴, CP²)
   - Target precision: <10⁻⁴

2. **Experimental Interface**
   - KATRIN data pipeline
   - JUNO oscillation analysis
   - CMB-S4 integration

3. **Extended Validation**
   - CKM matrix (quark mixing)
   - Higgs mass derivation
   - Dark matter candidates

### Medium Priority

4. **RG Flow Analysis**
   - Implement Wetterich equation
   - Study UV/IR fixed points
   - Asymptotic safety

5. **Figure Generation**
   - Automated figure scripts
   - Interactive plots (Plotly/Bokeh)
   - 3D visualizations

6. **Documentation**
   - Video tutorials
   - Jupyter notebook examples
   - FAQ expansion

### Community Contributions

7. **Independent Verification**
   - Reproduce results in different languages (Julia, Mathematica, etc.)
   - Cross-check with alternative methods
   - Peer review of derivations

8. **Extensions**
   - Black hole entropy corrections
   - Inflation scenarios
   - Non-perturbative regimes

---

## Code of Conduct

### Be Respectful

- Scientific discourse only
- Constructive criticism
- No personal attacks
- Acknowledge contributions

### Be Rigorous

- Verify calculations before submitting
- Cite sources
- Document assumptions
- Report uncertainties

### Be Transparent

- Show all steps
- Provide code for figures
- Archive data
- Version everything

---

## Review Process

### Pull Requests

1. **Automated checks** run on submission
2. **Author review** within 7 days
3. **Discussion** if needed
4. **Merge** when approved

### Acceptance Criteria

- All tests pass
- Code documented
- No breaking changes (or clearly flagged)
- Follows style guidelines

---

## Recognition

Contributors will be:

- Listed in CONTRIBUTORS.md
- Acknowledged in paper updates (if substantial)
- Credited in commit history

**Significant contributions** may warrant co-authorship on extensions/follow-up papers.

---

## Questions?

- Open a GitHub Discussion
- Email author (see README)
- Join [planned] Discord/Slack channel

---

## License

By contributing, you agree that your contributions will be licensed under CC BY 4.0, same as the project.

---

**Thank you for helping advance QGI Theory!** 🙏

*Contributing guide v1.0 - October 2025*


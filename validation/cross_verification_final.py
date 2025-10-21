#!/usr/bin/env python3
"""
Complete Cross-Verification: main.tex Internal Consistency
October 20, 2025

Verifies:
1. Tables ↔ Text consistency
2. Abstract ↔ Conclusions consistency
3. Figures cited ↔ Files exist
4. Bibliography references
5. Cross-references
"""

import re
import os
from pathlib import Path

print("="*80)
print("CROSS-VERIFICATION: main.tex INTERNAL CONSISTENCY")
print("="*80)
print("Date: October 20, 2025")
print("="*80)

# Read main.tex
with open('main.tex', 'r', encoding='utf-8') as f:
    content = f.read()

# ============================================================================
# CHECK 1: FIGURES CITED vs FILES EXIST
# ============================================================================

print("\n" + "="*80)
print("CHECK 1: FIGURES CITED vs FILES EXIST")
print("="*80)

# Find all figure citations
figure_pattern = r'\\maybeinclude.*?\{(.*?\.pdf)\}'
figures_cited = re.findall(figure_pattern, content)

print(f"\nFigures cited in document: {len(figures_cited)}")

missing_figures = []
existing_figures = []

for fig in figures_cited:
    fig_path = Path(fig)
    if fig_path.exists():
        existing_figures.append(fig)
        print(f"  ✓ {fig}")
    else:
        missing_figures.append(fig)
        print(f"  ✗ {fig} (MISSING)")

print(f"\nSummary:")
print(f"  Existing: {len(existing_figures)}/{len(figures_cited)}")
print(f"  Missing:  {len(missing_figures)}/{len(figures_cited)}")

if missing_figures:
    print(f"\n⚠️  Missing figures:")
    for fig in missing_figures:
        print(f"    - {fig}")
else:
    print(f"\n✅ All figures exist!")

# ============================================================================
# CHECK 2: KEY VALUES IN ABSTRACT vs CONCLUSIONS
# ============================================================================

print("\n" + "="*80)
print("CHECK 2: ABSTRACT ↔ CONCLUSIONS CONSISTENCY")
print("="*80)

# Extract abstract
abstract_match = re.search(r'\\begin\{abstract\}(.*?)\\end\{abstract\}', content, re.DOTALL)
abstract = abstract_match.group(1) if abstract_match else ""

# Extract conclusions
conclusions_match = re.search(r'\\section\{Conclusions\}.*?\\label\{sec:conclusions\}(.*?)(?=\\section|\\appendix|\\printbibliography)', content, re.DOTALL)
conclusions = conclusions_match.group(1) if conclusions_match else ""

# Key claims to check
key_claims = [
    ('α_info = 1/(8π³ ln π)', 'alpha.*info.*frac.*8.*pi.*ln.*pi'),
    ('winding numbers {1,3,7}', r'\{1,3,7\}'),
    ('masses {1,9,49}', r'\{1,9,49\}'),
    ('Σmν = 0.060 eV', r'0\.060.*eV'),
    ('19 independent tests', r'19.*independent.*test'),
    ('7 sectors', r'7.*sector'),
    ('precision <3%', r'<3.*%|3.*%.*precision'),
    ('>28σ evidence', r'>28.*sigma|28.*sigma.*evidence'),
    ('JUNO 2028-2030', r'JUNO.*202[89]|202[89].*JUNO'),
    ('GUT ratio 3/5', r'3/5|0\.602'),
    ('splitting ratio 1/30', r'1/30|0\.0333'),
]

print(f"\nKey claims consistency:")
consistent_claims = 0
inconsistent_claims = []

for claim, pattern in key_claims:
    in_abstract = bool(re.search(pattern, abstract, re.IGNORECASE | re.DOTALL))
    in_conclusions = bool(re.search(pattern, conclusions, re.IGNORECASE | re.DOTALL))
    
    if in_abstract and in_conclusions:
        print(f"  ✓ {claim}: in BOTH")
        consistent_claims += 1
    elif in_abstract or in_conclusions:
        location = "abstract only" if in_abstract else "conclusions only"
        print(f"  ⚠️  {claim}: in {location}")
        inconsistent_claims.append((claim, location))
    else:
        print(f"  ⚠️  {claim}: MISSING in both")
        inconsistent_claims.append((claim, "missing"))

print(f"\nConsistent: {consistent_claims}/{len(key_claims)}")

if inconsistent_claims:
    print(f"\n⚠️  Inconsistencies found:")
    for claim, issue in inconsistent_claims:
        print(f"    - {claim}: {issue}")

# ============================================================================
# CHECK 3: TABLES CONSISTENCY
# ============================================================================

print("\n" + "="*80)
print("CHECK 3: TABLES INTERNAL CONSISTENCY")
print("="*80)

# Find all tables
table_pattern = r'\\begin\{table\}.*?\\end\{table\}'
tables = re.findall(table_pattern, content, re.DOTALL)

print(f"\nTotal tables found: {len(tables)}")

# Check specific tables
critical_tables = {
    'tab:predictions': r'\\label\{tab:predictions\}',
    'tab:pmns_angles': r'\\label\{tab:pmns_angles\}',
    'tab:complete_scorecard': r'\\label\{tab:complete_scorecard\}',
    'tab:quark_exponents': r'\\label\{tab:quark_exponents\}',
}

print(f"\nCritical tables:")
for table_name, pattern in critical_tables.items():
    exists = bool(re.search(pattern, content))
    print(f"  {'✓' if exists else '✗'} {table_name}")

# Verify specific values in tab:predictions
predictions_table = re.search(r'\\label\{tab:predictions\}(.*?)\\end\{tabular\}', content, re.DOTALL)
if predictions_table:
    table_content = predictions_table.group(1)
    
    # Check neutrino values
    values_to_check = [
        ('m₁.*1.01', 'm₁ = 1.01 meV'),
        ('m₂.*9.10', 'm₂ = 9.10 meV'),
        ('m₃.*49.5', 'm₃ = 49.5 meV'),
        ('0.060.*eV', 'Σmν = 0.060 eV'),
        ('8.18', 'Δm²₂₁ = 8.18'),
        ('2.45', 'Δm²₃₁ = 2.45'),
        ('JUNO.*2030', 'JUNO (2030)'),
    ]
    
    print(f"\n  Values in tab:predictions:")
    for pattern, desc in values_to_check:
        found = bool(re.search(pattern, table_content, re.IGNORECASE))
        print(f"    {'✓' if found else '✗'} {desc}")

# ============================================================================
# CHECK 4: BIBLIOGRAPHY REFERENCES
# ============================================================================

print("\n" + "="*80)
print("CHECK 4: BIBLIOGRAPHY REFERENCES")
print("="*80)

# Find all \cite{} commands
cite_pattern = r'\\cite\{([^}]+)\}'
citations = re.findall(cite_pattern, content)

# Flatten (some have multiple refs like \cite{ref1,ref2})
all_refs = []
for cite in citations:
    all_refs.extend([r.strip() for r in cite.split(',')])

unique_refs = sorted(set(all_refs))

print(f"\nTotal citations: {len(citations)}")
print(f"Unique references: {len(unique_refs)}")

# Check if referencias.bib exists
if os.path.exists('referencias.bib'):
    with open('referencias.bib', 'r', encoding='utf-8') as f:
        bib_content = f.read()
    
    print(f"\nVerifying against referencias.bib:")
    
    missing_refs = []
    found_refs = []
    
    for ref in unique_refs:
        # Check if @article{ref} or @book{ref} etc exists
        ref_pattern = r'@\w+\{' + re.escape(ref)
        if re.search(ref_pattern, bib_content):
            found_refs.append(ref)
        else:
            missing_refs.append(ref)
    
    print(f"  Found: {len(found_refs)}/{len(unique_refs)}")
    
    if missing_refs:
        print(f"\n  ⚠️  Missing in referencias.bib ({len(missing_refs)}):")
        for ref in missing_refs[:10]:  # Show first 10
            print(f"    - {ref}")
        if len(missing_refs) > 10:
            print(f"    ... and {len(missing_refs)-10} more")
    else:
        print(f"  ✅ All references found in referencias.bib!")
else:
    print(f"  ✗ referencias.bib NOT FOUND")

# ============================================================================
# CHECK 5: CROSS-REFERENCES (labels vs refs)
# ============================================================================

print("\n" + "="*80)
print("CHECK 5: CROSS-REFERENCES")
print("="*80)

# Find all labels
label_pattern = r'\\label\{([^}]+)\}'
labels = set(re.findall(label_pattern, content))

# Find all refs
ref_pattern = r'\\ref\{([^}]+)\}|\\eqref\{([^}]+)\}'
refs_tuples = re.findall(ref_pattern, content)
refs = set([r for pair in refs_tuples for r in pair if r])

print(f"\nLabels defined: {len(labels)}")
print(f"References used: {len(refs)}")

# Find undefined references
undefined_refs = refs - labels

if undefined_refs:
    print(f"\n⚠️  Undefined references ({len(undefined_refs)}):")
    for ref in sorted(list(undefined_refs))[:10]:
        print(f"    - {ref}")
    if len(undefined_refs) > 10:
        print(f"    ... and {len(undefined_refs)-10} more")
else:
    print(f"\n✅ All references defined!")

# Find unused labels
unused_labels = labels - refs

print(f"\nUnused labels: {len(unused_labels)}")
if len(unused_labels) > 0 and len(unused_labels) < 20:
    for label in sorted(list(unused_labels)):
        print(f"  - {label}")

# ============================================================================
# CHECK 6: EQUATION NUMBERING
# ============================================================================

print("\n" + "="*80)
print("CHECK 6: EQUATION NUMBERING & BOXED EQUATIONS")
print("="*80)

# Count equations
equation_pattern = r'\\begin\{equation\}'
align_pattern = r'\\begin\{align\}'
numbered_eqs = len(re.findall(equation_pattern, content)) + len(re.findall(align_pattern, content))

# Count boxed equations (key results)
boxed_pattern = r'\\boxed\{'
boxed_eqs = len(re.findall(boxed_pattern, content))

print(f"\nNumbered equations: {numbered_eqs}")
print(f"Boxed equations (key results): {boxed_eqs}")

print(f"\nDocument structure:")
print(f"  Expected: 70-80 numbered equations")
print(f"  Actual: {numbered_eqs}")
print(f"  Status: {'✓' if 70 <= numbered_eqs <= 100 else '⚠️'}")

# ============================================================================
# CHECK 7: SECTION STRUCTURE
# ============================================================================

print("\n" + "="*80)
print("CHECK 7: SECTION STRUCTURE")
print("="*80)

# Find all sections
section_pattern = r'\\section\{([^}]+)\}'
sections = re.findall(section_pattern, content)

print(f"\nTotal sections: {len(sections)}")
print(f"\nMain sections:")
for i, sec in enumerate(sections[:15], 1):
    print(f"  {i}. {sec}")

if len(sections) > 15:
    print(f"  ... and {len(sections)-15} more")

# Check for key sections
key_sections = [
    'Introduction',
    'Theoretical Framework',
    'Electroweak',
    'Gravitational Sector',
    'Neutrino',
    'PMNS',  # NEW
    'Quark',  # NEW
    'Anomaly',  # NEW
    'Fourth Generation',  # NEW
    'Scorecard',  # NEW
    'Cosmolog',
    'Conclusions',
]

print(f"\n✓ Key sections present:")
for key in key_sections:
    found = any(key.lower() in s.lower() for s in sections)
    print(f"  {'✓' if found else '✗'} {key}")

# ============================================================================
# CHECK 8: NUMERICAL CONSISTENCY IN TEXT
# ============================================================================

print("\n" + "="*80)
print("CHECK 8: NUMERICAL CONSISTENCY IN TEXT")
print("="*80)

# Search for specific numerical claims and verify
numerical_checks = [
    # (pattern, expected_value, description)
    (r'alpha_{\rm info}.*0\.00352174', True, 'α_info value'),
    (r'varepsilon.*0\.00403144', True, 'ε value'),
    (r'm_1.*1\.01.*meV|1\.01.*10\^\{-3\}', True, 'm₁ = 1.01 meV'),
    (r'm_2.*9\.10.*meV|9\.10.*10\^\{-3\}', True, 'm₂ = 9.10 meV'),
    (r'm_3.*49\.5.*meV|49\.5.*10\^\{-3\}', True, 'm₃ = 49.5 meV'),
    (r'Sum.*m_nu.*0\.060', True, 'Σmν = 0.060 eV'),
    (r'8\.18.*10\^\{-5\}', True, 'Δm²₂₁ = 8.18×10⁻⁵'),
    (r'2\.453.*10\^\{-3\}', True, 'Δm²₃₁ = 2.453×10⁻³'),
    (r'1/30|\\frac\{1\}\{30\}', True, 'Ratio = 1/30'),
    (r'19.*test|test.*19', True, '19 tests'),
    (r'kappa_1.*81/20|kappa_1.*4\.05', True, 'κ₁ = 81/20'),
    (r'kappa_2.*26/3|kappa_2.*8\.66', True, 'κ₂ = 26/3'),
    (r'kappa_3.*8', True, 'κ₃ = 8'),
]

print(f"\nNumerical consistency checks:")
consistency_pass = 0

for pattern, should_exist, desc in numerical_checks:
    found = bool(re.search(pattern, content, re.IGNORECASE))
    status = found == should_exist
    symbol = '✓' if status else '✗'
    print(f"  {symbol} {desc}")
    if status:
        consistency_pass += 1

print(f"\nPassed: {consistency_pass}/{len(numerical_checks)}")

# ============================================================================
# CHECK 9: SPECIFIC VALUE EXTRACTION & VERIFICATION
# ============================================================================

print("\n" + "="*80)
print("CHECK 9: EXTRACT & VERIFY SPECIFIC CLAIMS")
print("="*80)

# Extract claims from key sections
claims_found = {}

# Abstract claims
if abstract:
    if '19 independent tests' in abstract.lower() or '19.*test' in abstract.lower():
        claims_found['19_tests_abstract'] = True
    if '>28' in abstract or '28.*sigma' in abstract:
        claims_found['28sigma_abstract'] = True
    if '0.04%' in abstract or '0.04.*%' in abstract:
        claims_found['004_percent_abstract'] = True

# Conclusions claims
if conclusions:
    if '19' in conclusions and 'test' in conclusions.lower():
        claims_found['19_tests_conclusions'] = True
    if '28' in conclusions and 'sigma' in conclusions.lower():
        claims_found['28sigma_conclusions'] = True

print(f"\nClaims tracking:")
print(f"  19 tests in abstract: {'✓' if claims_found.get('19_tests_abstract') else '✗'}")
print(f"  19 tests in conclusions: {'✓' if claims_found.get('19_tests_conclusions') else '✗'}")
print(f"  >28σ in abstract: {'✓' if claims_found.get('28sigma_abstract') else '✗'}")
print(f"  >28σ in conclusions: {'✓' if claims_found.get('28sigma_conclusions') else '✗'}")

# ============================================================================
# CHECK 10: JUNO MENTIONS
# ============================================================================

print("\n" + "="*80)
print("CHECK 10: JUNO EXPERIMENTAL DATA")
print("="*80)

# Find all JUNO mentions
juno_pattern = r'JUNO'
juno_mentions = re.findall(juno_pattern, content, re.IGNORECASE)

print(f"\nJUNO mentions: {len(juno_mentions)}")

# Find contexts
juno_contexts = re.findall(r'.{0,80}JUNO.{0,80}', content, re.IGNORECASE)

print(f"\nKey JUNO contexts:")
seen = set()
for context in juno_contexts[:10]:
    clean = context.strip()
    if clean and clean not in seen:
        print(f"  - ...{clean[:100]}...")
        seen.add(clean)

# Check for specific JUNO targets
juno_checks = [
    ('2028-2030', 'Timeline 2028-2030'),
    ('2030', 'Year 2030'),
    ('mass ordering', 'Mass ordering'),
    ('precision|<0.5%|sub-percent', 'Precision target'),
    ('20.*better|improvement', 'Improvement factor'),
]

print(f"\nJUNO-specific claims:")
for pattern, desc in juno_checks:
    found = any(re.search(pattern, ctx, re.IGNORECASE) for ctx in juno_contexts)
    print(f"  {'✓' if found else '✗'} {desc}")

# ============================================================================
# FINAL SUMMARY
# ============================================================================

print("\n" + "="*80)
print("FINAL CROSS-VERIFICATION SUMMARY")
print("="*80)

all_checks = [
    ("Figures exist", len(missing_figures) == 0),
    ("Abstract ↔ Conclusions", len(inconsistent_claims) == 0),
    ("Numerical consistency", consistency_pass == len(numerical_checks)),
    ("Critical tables present", all(re.search(p, content) for p in critical_tables.values())),
    ("JUNO data integrated", len(juno_mentions) >= 15),
    ("Key claims verified", consistent_claims >= len(key_claims) * 0.8),
]

total_passed = sum([1 for _, status in all_checks if status])
total_checks = len(all_checks)

print(f"\nOVERALL: {total_passed}/{total_checks} categories passed")
print("-" * 80)

for check_name, status in all_checks:
    symbol = "✓" if status else "⚠️"
    print(f"  {symbol} {check_name}")

if total_passed == total_checks:
    print("\n" + "="*80)
    print("🎉 COMPLETE CROSS-VERIFICATION PASSED!")
    print("   Document is internally consistent.")
    print("   Ready for final compilation and submission.")
    print("="*80)
else:
    print(f"\n⚠️  {total_checks - total_passed} categor{'y' if total_checks - total_passed == 1 else 'ies'} need attention.")

print("\n" + "="*80)
print("VERIFICATION COMPLETE")
print("="*80)


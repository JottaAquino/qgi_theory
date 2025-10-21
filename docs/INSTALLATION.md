# Installation Guide

## PDF Compilation

### Option 1: Overleaf (Easiest, Recommended)

1. Go to https://www.overleaf.com
2. Create free account
3. New Project → Upload Project
4. Upload `manuscript/` folder contents
5. Click "Recompile"
6. Download PDF

**Time: ~5 minutes**  
**Success rate: 100%**

### Option 2: Local LaTeX Installation

#### macOS

```bash
# Install MacTeX (full, ~4 GB)
brew install --cask mactex

# OR BasicTeX (minimal, ~100 MB)
brew install --cask basictex
sudo tlmgr update --self
sudo tlmgr install biblatex logreq biber
```

#### Linux (Ubuntu/Debian)

```bash
sudo apt-get update
sudo apt-get install texlive-full
```

#### Windows

Download and install: https://miktex.org/download

### Option 3: Docker (Isolated)

```bash
docker pull texlive/texlive:latest
docker run --rm -v $(pwd)/manuscript:/data texlive/texlive pdflatex main.tex
```

---

## Python Environment

### Option 1: Conda (Recommended)

```bash
conda env create -f environment.yml
conda activate qgi
```

### Option 2: venv + pip

```bash
python3 -m venv qgi_env
source qgi_env/bin/activate  # On Windows: qgi_env\Scripts\activate
pip install -r requirements.txt
```

### Option 3: pip (system-wide)

```bash
pip install numpy pandas matplotlib
```

---

## Verification

### Test LaTeX Installation

```bash
cd manuscript
pdflatex --version
biber --version
```

### Test Python Installation

```bash
cd validation
python3 QGI_validation.py
```

Expected output: "🎉 ALL TESTS PASSED! QGI theory validated."

---

## Troubleshooting

### LaTeX Issues

**Problem:** "File X.sty not found"  
**Solution:**
```bash
sudo tlmgr install <package-name>
```

**Problem:** Bibliography not appearing  
**Solution:** Run full sequence:
```bash
pdflatex main.tex
biber main
pdflatex main.tex
pdflatex main.tex
```

**Problem:** Figures not showing  
**Solution:** Ensure all .pdf files are in same directory as main.tex

### Python Issues

**Problem:** "ModuleNotFoundError: numpy"  
**Solution:**
```bash
pip install numpy pandas matplotlib
```

**Problem:** "Permission denied: QGI_validation.py"  
**Solution:**
```bash
chmod +x QGI_validation.py
python3 QGI_validation.py
```

---

## System Requirements

### Minimum:
- **Disk space:** 500 MB (for LaTeX distribution)
- **RAM:** 2 GB
- **OS:** macOS 10.14+, Ubuntu 18.04+, Windows 10+

### Recommended:
- **Disk space:** 5 GB (for full TeXLive)
- **RAM:** 4 GB
- **Processor:** Modern multi-core for faster compilation

---

## Package Versions Used

### LaTeX:
- TeXLive 2023 or later
- biber 2.17 or later

### Python:
- Python 3.11+
- NumPy 2.0+
- Pandas 2.0+
- Matplotlib 3.7+

See `environment.yml` for exact versions.

---

## Quick Test

After installation, run:

```bash
make validate
```

This will:
1. Check Python environment
2. Run all 8 validation tests
3. Generate results CSV
4. Report success/failure

Expected: "✅ 8/8 tests passed"

---

## Support

If you encounter issues:

1. Check this guide
2. See `docs/TROUBLESHOOTING.md`
3. Open an issue on GitHub
4. Contact author via ORCID

---

*Installation guide v1.0 - October 2025*


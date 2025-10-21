# Makefile for QGI Theory manuscript
# Author: Marcos Eduardo de Aquino Junior
# Date: 2025-01-13

.PHONY: all clean validate pdf view help

# Main targets
all: pdf validate

help:
	@echo "QGI Theory - Build System"
	@echo "========================="
	@echo ""
	@echo "Available targets:"
	@echo "  make pdf        - Compile LaTeX to PDF"
	@echo "  make validate   - Run validation tests"
	@echo "  make clean      - Remove generated files"
	@echo "  make view       - Open PDF (macOS)"
	@echo "  make package    - Create submission ZIP"
	@echo "  make all        - Build PDF and run validation"
	@echo ""

# Compile PDF
pdf:
	@echo "Compiling QGI manuscript..."
	pdflatex -interaction=nonstopmode main.tex
	biber main
	pdflatex -interaction=nonstopmode main.tex
	pdflatex -interaction=nonstopmode main.tex
	@echo "✓ PDF compiled successfully: main.pdf"

# Run validation tests
validate:
	@echo "Running QGI validation suite..."
	python3 QGI_validation.py
	@echo "✓ Validation complete. See QGI_validation_results.csv"

# View PDF (macOS)
view: pdf
	open main.pdf

# Clean auxiliary files
clean:
	rm -f *.aux *.log *.out *.toc *.bbl *.blg *.bcf *.run.xml
	rm -f *.synctex.gz *.fdb_latexmk *.fls
	@echo "✓ Cleaned auxiliary files"

# Clean everything including PDF
clean-all: clean
	rm -f main.pdf
	rm -f QGI_validation_results.csv
	rm -f neutrino_predictions.png
	@echo "✓ Cleaned all generated files"

# Create submission package
package: pdf validate
	@echo "Creating submission package..."
	mkdir -p submission
	cp main.tex submission/
	cp main.pdf submission/
	cp referencias.bib submission/
	cp QGI_validation.py submission/
	cp environment.yml submission/
	cp README.md submission/
	cp fig*.pdf fig*.png submission/ 2>/dev/null || true
	cp QGI_validation_results.csv submission/
	cd submission && zip -r ../QGI_submission_$(shell date +%Y%m%d).zip .
	rm -rf submission
	@echo "✓ Package created: QGI_submission_$(shell date +%Y%m%d).zip"



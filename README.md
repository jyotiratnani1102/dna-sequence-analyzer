# DNA Sequence Analyzer 🧬

This is one of my beginner projects in Python and bioinformatics. I built it to practice working with DNA sequences using Biopython.

## What does it do?

- Reads a DNA sequence from a FASTA file.
- Calculates the total sequence length.
- Counts the A, T, G, and C nucleotides.
- Calculates the percentage of each nucleotide.
- Finds the GC content of the sequence.
- Converts DNA into an RNA transcript and displays the first 60 bases.
- Saves the results in a text file.

## Tools Used
- Python
- Biopython
- VS Code

## How to Run It

First, install Biopython:

```bash
python -m pip install biopython
```

Make sure `dna_seq_analyzer.py` and `sequence.fasta` are in the same folder. Then run:

```bash
python dna_seq_analyzer.py
```

The results will appear in the terminal, and a report named `analysis_report.txt` will be created.

## About the Sequence

I used the *Saccharomyces cerevisiae* DNA sequence with GenBank accession **U49845.1**, obtained from NCBI.

## What I Learned

While building this project, I practised using Python to work with biological sequences, calculate nucleotide statistics, and save analysis results to a file. It also helped me understand how programming can be used in bioinformatics.

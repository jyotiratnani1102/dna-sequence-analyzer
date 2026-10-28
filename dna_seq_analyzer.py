
from Bio import SeqIO
from collections import Counter

try:
    record = SeqIO.read("sequence.fasta", "fasta")
    dna = str(record.seq).upper()

    if not dna:
        raise ValueError("The sequence is empty.")

    invalid_bases = set(dna) - set("ATGC")
    if invalid_bases:
        raise ValueError(f"Invalid DNA characters: {invalid_bases}")

    counts = Counter(dna)
    length = len(dna)
    gc_content = (counts["G"] + counts["C"]) / length * 100
    rna = dna.replace("T", "U")

    print("=== DNA SEQUENCE ANALYZER ===")
    print("Sequence ID:", record.id)
    print("Sequence length:", length, "bp")
    print("Nucleotide counts:", dict(counts))
    print("Nucleotide percentages:")
    for base in "ATGC":
        percentage = counts[base] / length * 100
        print(f"{base}: {percentage:.2f}%")
    print(f"GC content: {gc_content:.2f}%")
    print("RNA transcript (first 60 bases):", rna[:60])

    # Save the analysis report
    with open("analysis_report.txt", "w") as report:
        report.write("DNA SEQUENCE ANALYSIS REPORT\n")
        report.write("============================\n")
        report.write(f"Sequence ID: {record.id}\n")
        report.write(f"Sequence length: {length} bp\n")
        report.write(f"Nucleotide counts: {dict(counts)}\n")

        report.write("\nNucleotide percentages:\n")
        for base in "ATGC":
            percentage = counts[base] / length * 100
            report.write(f"{base}: {percentage:.2f}%\n")

        report.write(f"GC content: {gc_content:.2f}%\n")
        report.write(f"RNA preview: {rna[:60]}\n")

    print("Report saved to analysis_report.txt")
except FileNotFoundError:
    print("Error: sequence.fasta was not found.")

except ValueError as error:
    print("Error:", error)

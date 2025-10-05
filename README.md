# BI_tools: Bioinformatics Utilities in Python
A small collection of Python tools for working with nucleotide and FASTQ data.  
The project is modular and organized into separate files for clarity and reuse.

P.S. This repository was created for educational purposes.

---

## Project structure

```
BI_tools/
│
├── modules/
│ ├── filter_fastq_funcs.py 
│ ├── nucleic_acid_func.py 
│ ├── phred33.py 
│ ├── transcription_funcs.py 
│
├── main.py 
└── README.md 
```

---

## Description

### Main script — `main.py`

The main script provides the `run_dna_rna_tools()` and `filter_fastq()` functions,  
which allow you to process nucleotide sequences and filter FASTQ data.

#### `run_dna_rna_tools()`
Runs basic DNA/RNA operations:
- `is_nucleic_acid`
- `transcribe`
- `reverse`
- `complement`
- `reverse_complement`

**Example:**
```python
from main import run_dna_rna_tools

print(run_dna_rna_tools("ATGC", "reverse_complement"))
```

#### `filter_fastq()`
Filters FASTQ sequences by GC content, length, and quality score.
Validation is performed automatically before filtering.

**Example:**
```python
from main import filter_fastq

sequences = {
    "read1": ("ATGC", "DFF@"),
    "read2": ("GGGG", "IIII")
}

filtered = filter_fastq(sequences, gc_bounds=(20, 80), length_bounds=1000, quality_threshold=30)
print(filtered)
```


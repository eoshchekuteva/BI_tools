# BI_tools: Bioinformatics Utilities in Python
A small collection of Python tools for working with nucleotide and FASTQ data.  
The project is modular and organized into separate files for clarity and reuse.

P.S. This repository was created for educational purposes.

## Project structure

```
BI_tools/
│
├── modules/
│  ├── check_bounds.py 
│  ├── filter_fastq_funcs.py 
│  ├── nucleic_acid_func.py 
│  ├── phred33.py 
│  ├── read_write_fastq_files.py 
│  ├── transcription_funcs.py 
│
├── bio_files_processor.py 
├── main.py 
└── README.md 
```

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
Filters FASTQ records on the fly — reads one record, validates, and writes immediately,
minimizing memory usage.

Implemented using helper modules:

- `filter_fastq_funcs.py` – filtering logic
- `check_bounds.py` – range validation (GC%, length, quality)
- `phred33.py` – Phred quality conversion
- `read_write_fastq_files.py` – safe reading/writing utilities

**Example:**
```python
from main import filter_fastq

result = filter_fastq('reads.fastq', gc_bounds=(20, 80), length_bounds=1000, quality_threshold=30)
```

### `bio_files_processors.py`

#### `convert_multiline_fasta_to_oneline()`
Converts a FASTA file with multiline sequences into a single-line-per-sequence format.

**Example:**
```python
from modules.bio_files_processor import convert_multiline_fasta_to_oneline

convert_multiline_fasta_to_oneline("example_multiline_fasta.fasta")
```

#### `parse_blast_output()`
Parses BLAST output files, extracts the top hit (first description) from each “Sequences producing significant alignments” section, sorts them alphabetically, and writes to a new file.

**Example:**
```python
from modules.bio_files_processor import parse_blast_output

parse_blast_output("example_blast_results.txt")
```

## Dependencies

- Python 3.10+
- No external libraries required (standard library only)

## Author

Developed by Ekaterina Shchekuteva.

![coding cat](https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif)
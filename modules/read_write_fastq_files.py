from typing import Iterator
import os

def read_fastq_sample(file: str) -> Iterator[tuple[str, str]]:
    """
    Yield nucleic and phred sequence for each sample read in fastq file.

    Argument:
    file: An open FASTQ file object for reading.

    Yields: tuple[str, str]
    A pair containing:
    - the nucleotide sequence;
    - the phred sequence.
    """
    while True:
        name = file.readline()
        seq = file.readline()
        plus = file.readline()
        phred = file.readline()

        if not phred:
            break
        
        yield seq, phred


def safe_write(path: str) -> str | None:
    """
    Check if the file can be safely written.

    Argument: str
    Input directory for output file.
    
    Returns: 
    - str: The same path if the file does not exist or is empty.
    - None: If the file already exists and contains data.
    """
    if not os.path.exists(path):
        return path
    elif os.path.getsize(path)==0:
        return path
    else:
        return None
    
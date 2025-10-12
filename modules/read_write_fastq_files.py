from typing import Iterator

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

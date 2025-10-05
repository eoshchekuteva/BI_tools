def is_dna(sequence: str) -> bool:
    """
    Chek if the given sequence is a DNA sequence.

    A valid DNA sequence contains only A, T, G and C nucleotide.

    Argument:
    sequence (str): The input nucleotide sequence.

    Returns bool:
    True if the sequence is DNA, False otherwise.
    """
    dna = set("AGTC")
    return set(sequence.upper()) <= dna


def is_rna(sequence: str) -> bool:
    """
    Chek if the given sequence is a RNA sequence.

    A valid RNA sequence contains only A, U, G and C nucleotide.

    Argument:
    sequence (str): The input nucleotide sequence.

    Returns bool:
    True if the sequence is RNA, False otherwise.
    """
    rna = set("AUGC")
    return set(sequence.upper()) <= rna


def is_nucleic_acid(sequence: str) -> bool:
    """
    Chek if the given sequence is a nucleic acid sequence (DNA or RNA).

    Argument:
    sequence (str): The input nucleotide sequence.

    Returns bool:
    True if the sequence is DNA or RNA, False otherwise.
    """
    return is_dna(sequence) or is_rna(sequence)

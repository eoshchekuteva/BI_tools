from phred33 import phred_quality, is_phred
from nucleic_acid_funcs import is_nucleic_acid


def is_gc_filter(sequence: str, start=0, end=100) -> bool:
    """
    Chek if the GC content of the given sequence is within the specified range.

    Arguments:
    sequence (str): the input nucleotide sequence.
    start (int, float, optional): lower GC content bound (in percent). Defaults to 0.
    end (int, float, optional): upper GC content bound (in percent). Defaults to 100.

    Return bool:
    True if GC content is within the specified range, False otherwise.
    """
    gc_number = sequence.upper().count("G") + sequence.upper().count("C")
    gc_percent = (gc_number / len(sequence)) * 100
    return start <= gc_percent <= end


def is_length_filter(sequence: str, start=0, end=2**23) -> bool:
    """
    Check if the sequence length is within the specified range.

    Arguments:
    sequence (str): the input nucleotide sequence.
    start (int, float, optional): minimum allowed sequence length. Default to 0.
    end (int, float, optional): maximum allowed sequence length. Default to 2**23.

    Return bool:
    True if the sequence length is within the range, False otherwise.
    """
    return start <= len(sequence) <= end


def is_quality_control(phred_sequence: str, min_quality) -> bool:
    """
    Check if the average phred quality score of the sequence meets the required treashold.

    The mean quality is calculated using the Phred33 encoding table.

    Argument:
    phred_sequence (str): the input phred quality sequence.
    quality_need (int): the minimum avarage quality score required.

    Return bool:
    True if the average quality is greater than or equal to the threshold, False otherwise.
    """
    current_quality = 0
    for symbol in phred_sequence:
        current_quality += phred_quality[symbol]
    mean_current_quality = current_quality / len(phred_sequence)
    return min_quality <= mean_current_quality


def is_validate(sequences: dict) -> bool:
    """
    Validate that all records in the given dict contain correct data.

    Each record must have:
    1. A valid nucleic acid sequence;
    2. A valid phred quality sequence;
    3. Matching nucleic acid sequence and quality sequence length.

    Argument:
    sequence (dict): dictionary of the form {name: (nuc_sequence, phred_sequence)}.

    Return bool:
    True if all records are valid, False otherwise.
    """
    for name, (nuc_seq, phred_seq) in sequences.items():
        if not (is_nucleic_acid(nuc_seq) and is_phred(phred_seq)):
            return False
        if len(nuc_seq) != len(phred_seq):
            return False
    return True


def bounds_processing(
    nuc_seq: str,
    phred_seq: str,
    gc_start: float | int,
    gc_end: float | int,
    ln_start: int,
    ln_end: int,
    quality_threshold: int,
) -> bool:
    """
    Apply all filtering criteria (GC content, length, quality)
    to a given nucleotide and quality sequence.

    Returns bool:
    True if sequence passes all filters, False otherwise.
    """
    return (
        is_gc_filter(nuc_seq, gc_start, gc_end)
        and is_length_filter(nuc_seq, ln_start, ln_end)
        and is_quality_control(phred_seq, quality_threshold)
    )

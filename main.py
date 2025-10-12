import modules.filter_fastq_funcs as ff
import modules.transcription_funcs as trf
import modules.nucleic_acid_funcs as ncf
import modules.check_bounds as cb


def filter_fastq(
    sequences: dict[int, float, str[str, str]],
    gc_bounds: tuple[float, float] | int | float = (0, 100),
    length_bounds: tuple[int, int] | int = (0, 2**23),
    quality_threshold: int | float = 0,
) -> dict[int, float, str[str, str]] | None:
    """
    Filter FASTQ records based on GC content, sequence length, and quality score.

    The function validates all input records, normalizes filtering bounds,
    and returns only those reads that meet the specified criteria.

    Argument:
    sequences (dict): dictionary of reads in the form {name: (nucleotide_seq, phred_seq)}.
    gc_bounds (int, float, tuple, optional): GC content threshold.
    length_bounds (int, float, tuple, optional): allowed range of sequence lengths.
    quality_threshold (int, float): minimum average Phred quality score.

    Return dict:
    Dictionary of filtered sequences that passed all filters.
    """
    if not ff.is_validate(sequences):
        return None

    filtered_sequences = {}

    gc_start, gc_end = cb.parse_bounds(gc_bounds, (0, 100))
    ln_start, ln_end = cb.parse_bounds(length_bounds, (0, 2**23))

    for name, (nuc_seq, phred_seq) in sequences.items():
        if ff.bounds_processing(
            nuc_seq, phred_seq, gc_start, gc_end, ln_start, ln_end, quality_threshold
        ):
            filtered_sequences[name] = (nuc_seq, phred_seq)

    return filtered_sequences


def run_dna_rna_tools(*args: str) -> str | list[str] | None:
    """
    Run the specified nucleic acid operation on one or more sequences.

    The last argument defines the operation to perform.
    Supported operations:
        - 'is_nucleic_acid'
        - 'transcribe'
        - 'reverse'
        - 'complement'
        - 'reverse_complement'

    Arguments:
    *args: One or more nucleotide sequences followed by an operation name.
    Example: run_dna_rna_tools("ATGC", "AUGC", "reverse_complement")

    Returns str, list or None:
    1. A single string if one sequence is processed;
    2. A list of results if multiple sequences are provided;
    3. None if the specified operation is invalid.
    """
    *sequences, operation = args

    operations = {
        "is_nucleic_acid": ncf.is_nucleic_acid,
        "transcribe": trf.transcribe,
        "reverse": trf.reverse,
        "complement": trf.complement,
        "reverse_complement": trf.reverse_complement,
    }

    if operation in operations:
        func = operations[operation]
        result = []
        for sequence in sequences:
            if ncf.is_nucleic_acid(sequence):
                result.append(func(sequence))
        return result[0] if len(result) == 1 else result
    else:
        return None

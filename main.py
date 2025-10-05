import modules.filter_fastq_funcs as ff


def filter_fastq(sequences, gc_bounds, length_bounds, quality_threshold) -> dict:
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

    if isinstance(gc_bounds, (int, float)):
        gc_start, gc_end = 0, gc_bounds
    elif isinstance(gc_bounds, (tuple, dict)):
        gc_start, gc_end = gc_bounds
    else:
        gc_start, gc_end = 0, 100

    if isinstance(length_bounds, (int, float)):
        ln_start, ln_end = 0, length_bounds
    elif isinstance(length_bounds, (tuple, dict)):
        ln_start, ln_end = length_bounds
    else:
        ln_start, ln_end = 0, 2**23

    for name, (nuc_seq, phred_seq) in sequences.items():
        if (
            ff.is_gc_filter(nuc_seq, gc_start, gc_end)
            and ff.is_length_filter(nuc_seq, ln_start, ln_end)
            and ff.is_quality_control(phred_seq, quality_threshold)
        ):
            filtered_sequences[name] = (nuc_seq, phred_seq)

    return filtered_sequences

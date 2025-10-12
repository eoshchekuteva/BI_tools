import modules.filter_fastq_funcs as ff
import modules.transcription_funcs as trf
import modules.nucleic_acid_funcs as ncf
import modules.check_bounds as cb
import os
import modules.read_write_fastq_files as rwf


def filter_fastq(
    input_fastq: str,
    output_fastq: str,
    gc_bounds: tuple[float, float] | int | float = (0, 100),
    length_bounds: tuple[int, int] | int = (0, 2**23),
    quality_threshold: int | float = 0,
):
    """
    Filter FASTQ file on-the-fly without loading it entirely into memory.
    Each read is validated, filtered, and written immediately if it passes.

    Argument:
    input_fastq (str): input fastq file directory.
    output_fastq(str): output fastq file directory.
    gc_bounds (int, float, tuple, optional): GC content threshold.
    length_bounds (int, float, tuple, optional): allowed range of sequence lengths.
    quality_threshold (int, float): minimum average Phred quality score.
    """
    gc_start, gc_end = cb.parse_bounds(gc_bounds, (0, 100))
    ln_start, ln_end = cb.parse_bounds(length_bounds, (0, 2**23))

    os.makedirs("filtered", exist_ok=True)
    output_path = rwf.safe_output_path(os.path.join("filtered", output_fastq))

    read_id = 0

    with open(input_fastq) as infile, open(output_path, "w") as outfile:
        for seq, phred in rwf.read_fastq_sample(infile):
            read_id += 1
            if ff.is_filter_posses(
                seq, phred, gc_start, gc_end, ln_start, ln_end, quality_threshold
            ):
                passed += 1
                rwf.write_fastq_sample(outfile, read_id, seq, phred)


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

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

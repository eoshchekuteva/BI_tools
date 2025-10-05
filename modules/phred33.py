symbols = [chr(i) for i in range(33, 74)]
quality_score = [i for i in range(0, 41)]

phred_quality = dict(zip(symbols, quality_score))


def is_phred(sequence: str) -> bool:
    """
    Check if the given sequence is a phred quality sequence.

    A valid phred sequence contains only ASCII symbols in the range of 33-73.

    Argument:
    sequence (str): the input phred quality sequence.

    Return bool:
    True if the sequence contains only valid phred symbols, False otherwise.
    """
    return set(sequence) <= set(symbols)

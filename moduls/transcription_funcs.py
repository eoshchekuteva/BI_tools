def transcribe(sequence: str) -> str:
    """
    Transcribe a DNA sequence into RNA sequence by replacing all T nuclrotide with U nucleotide.

    Argument:
    sequence (str): The input DNA sequence.

    Returns str:
    The transcribed RNA sequence.
    """
    transcribe_sequence = sequence.replace("T", "U").replace("t", "u")
    return transcribe_sequence


def reverse(sequence: str) -> str:
    """
    Return the reversed sequence of the given sequence.

    Argument:
    sequence (str): the input sequence.

    Return str:
    the reversed sequence.
    """
    reverse_sequence = sequence[::-1]
    return reverse_sequence

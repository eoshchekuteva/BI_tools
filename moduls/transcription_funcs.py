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


def complement(sequence):
    """
    Return the complement DNA strand for the given sequence without changing the letter case.

    Each nucleotide is replaced with its complement: A - T, G - C.

    Argument:
    sequence (str): the input DNA sequence.

    Return str:
    the complementary DNA sequence.
    """
    complement_dict ={'A': 'T',
                      'a': 't',
                      'T': 'A',
                      't': 'a',
                      'C': 'G',
                      'c': 'g',
                      'G': 'C',
                      'g': 'c'}
    return "".join(complement_dict[char] for char in sequence)
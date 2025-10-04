def is_dna(sequence):
    dna = set("AGTC")
    return set(sequence.upper()) <= dna

def is_rna(sequence):
    rna = set("AUGC")
    return set(sequence.upper()) <= rna

def is_nucleic_acid(sequence):
    return is_dna(sequence) or is_rna(sequence)

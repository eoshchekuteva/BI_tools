def is_dna(sequence):
    dna = set('AGTC')
    return set(sequence) <= dna
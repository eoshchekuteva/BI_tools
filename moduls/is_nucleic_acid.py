def is_dna(sequence):
    dna = set("AGTC")
    return set(sequence) <= dna

def is_rna(sequence):
    rna = set("AUGC")
    return set(sequence) <= rna

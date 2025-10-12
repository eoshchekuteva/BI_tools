from typing import Optional


def convert_multiline_fasta_to_oneline(
    input_fasta: str, output_fasta: Optional[str] = None
) -> str:
    """
    Converts a FASTA file where sequences may be split across multiple lines
    into a format where each sequence is contained on a single line.

    Arguments:
    input_fasta (str): Path to the input FASTA file.
    output_fasta (str, optional): Path to the output FASTA file.

    Returns str: Path to the created output file.
    """
    if output_fasta is None:
        output_fasta = input_fasta + "_oneline.fasta"

    with open(input_fasta, "r") as infile, open(output_fasta, "w") as outfile:
        header = ""
        sequence_parts = []
        for line in infile:
            line = line.strip()

            if not line:
                continue
            if line.startswith(">"):
                if header and sequence_parts:
                    outfile.write(f"{header}\n{''.join(sequence_parts)}\n")
                header = line
                sequence_parts = []
            else:
                sequence_parts.append(line)

        if header and sequence_parts:
            outfile.write(f"{header}\n{''.join(sequence_parts)}\n")
    return output_fasta


def parse_blast_output(input_file: str, output_file: Optional[str] = None) -> str:
    """
    Parses a BLAST output text file and extracts the top hit (first description)
    for each query section ("Sequences producing significant alignments:").
    """
    if output_file is None:
        output_file = input_file + "_parsed.txt"

    best_hits = []
    flag = False

    with open(input_file) as infile:
        for line in infile:
            line = line.strip()

            if "Sequences producing significant alignments:" in line:
                flag = True
                continue
            elif flag and line:
                description = line.split()[0]
                best_hits.append(description)
                flag = False
            else:
                continue
        unique_hits = sorted(set(best_hits))

    with open(output_file, "w") as outfile:
        for hit in unique_hits:
            outfile.write(f"{hit}\n")

    return output_file

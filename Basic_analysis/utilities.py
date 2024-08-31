def colored(seq):
    bcolors = {
        'A': '\033[92m',  # Green
        'C': '\033[94m',  # Blue
        'G': '\033[93m',  # Yellow
        'T': '\033[91m',  # Red
        'U': '\033[91m',  # Red
        'reset': '\033[0m'  # Reset to default color
    }

    tmpStr = ""

    for nuc in seq:
        if nuc in bcolors:
            tmpStr += bcolors[nuc] + nuc  # Add the color and the nucleotide
        else:
            tmpStr += bcolors['reset'] + nuc  # Reset color and add the nucleotide

    tmpStr += bcolors['reset']  # Ensure the final color is reset
    return tmpStr

from Basic_analysis.DNAToolkit import *
from Basic_analysis.utilities import *
import random

randDNAStr = ''.join([random.choice(Nucleotides) for n in range(50)])


DNAStr = validateSeq(randDNAStr)
print(f'\nSequence: {colored(DNAStr)}\n')
print(f'[1] + Sequence Length: {len(DNAStr)}\n')
print(f'[2] + Nucleotide Frequency: {countNucFrequency(DNAStr)}\n')
print(f'[3] + DNA/RNA transcription: {colored(transcription(DNAStr))}\n')
print(f"[4] + DNA String + Reverse Complement:\n5' {colored(DNAStr)} 3'")
print(f"   {''.join(['|' for c in range(len(DNAStr))])}")
print(f"3' {colored(reverse_complement(DNAStr))} 5'\n")
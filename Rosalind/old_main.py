from Basic_analysis.DNAToolkit import *
from Basic_analysis.utilities import *
import random

randDNAStr = ''.join([random.choice(Nucleotides) for n in range(60)])


DNAStr = validateSeq(randDNAStr)
print(f'\nSequence: {colored(DNAStr)}\n')
print(f'[1] + Sequence Length: {len(DNAStr)}\n')
print(f'[2] + Nucleotide Frequency: {countNucFrequency(DNAStr)}\n')
print(f'[3] + DNA/RNA transcription: {colored(transcription(DNAStr))}\n')
print(f"[4] + DNA String + Reverse Complement:\n5' {colored(DNAStr)} 3'")
print(f"   {''.join(['|' for c in range(len(DNAStr))])}")
print(f"3' {colored(reverse_complement(DNAStr))} 5'\n")
print(f'[5] + GC Content: {gc_content(DNAStr)}%\n')
print(f'[6] + GC Content in Subsection k=5: {gc_content_subsec(DNAStr, k=5)}\n')
print(f'[7] + Aminoacids Sequence from DNA: {translate_dna_to_codons(DNAStr)}\n')
print(f'[8] + Codon frequency (L):{codon_usage(DNAStr, "L")}\n')
# Assuming gen_reading_frames(DNAStr) returns a list of lists
print(f'[9] + Reading_frames: ')
for frame in gen_reading_frames(DNAStr):
    print(frame)

frames = ['G', 'M', 'G', 'A', 'S', 'Y', 'P', 'G', 'V', '_', 'M', 'R', 'L', 'L',  'R', 'N', 'P', 'S', 'E', 'K', '_']

print(proteins_from_rf(frames))
print(f'\n[10] + All prots in 6 open reading frames: ')
for prot in all_proteins_from_orfs(NM_000207_3, 0, 0, True):
    print(f'{prot}')


from collections import Counter
from DNA_Toolkit.structures import *

def validateSeq(dna_seq):
    tempseq = dna_seq.upper()
    for nuc in tempseq:
        if nuc not in Nucleotides:
            return False
    return tempseq
def countNucFrequency(seq):
    tmpFreqDict = {"A":0, "C":0, "G":0, "T":0}
    for base in seq:
        tmpFreqDict[base] += 1
    return tmpFreqDict
def transcription(seq):
    return seq.replace('T','U')
def reverse_complement(seq):
    """ Swapping adenin with thymine and guanine with cytocine and then reversing the order of the DNA sequence"""
    # return ''.join([DNA_ReverseCompliment[nuc] for nuc in seq])[::-1]
    mapping = str.maketrans('ATCG', 'TAGC')
    return seq.translate(mapping)[::-1]
def gc_content(seq):
    # gc content is yhe percent of guanine and cytosine compared to adesine and thymine
    return round(100*((seq.count('G') + seq.count('C'))/ len(seq)), 2)
def gc_content_subsec(seq, k=20):
    """GC Content in a dna/rna sub sequence lenght k. k=20 by default"""
    res = []
    for i in range(0, len(seq) - k + 1, k):
        sebseq = seq[i:i + k]
        res.append(gc_content(sebseq))
    return res
def translate_dna_to_codons(seq, init_pos=0):
    return [DNA_Codons[seq[pos:pos +3]] for pos in range(init_pos, len(seq)-2, 3)]
def codon_usage(seq, aminoacid):
    tmpList = []
    for i in range(0, len(seq)-2, 3):
        if DNA_Codons[seq[i:i+3]] == aminoacid:
            tmpList.append(seq[i:i+3])

    freqDict = dict(Counter(tmpList))
    totalWight = sum(freqDict.values())
    for seq in freqDict:
        freqDict[seq] = round(freqDict[seq] / totalWight, 2)
    return freqDict
def gen_reading_frames(seq):
    frames = []
    frames.append(translate_dna_to_codons(seq, 0))
    frames.append(translate_dna_to_codons(seq, 1))
    frames.append(translate_dna_to_codons(seq, 2))
    frames.append(translate_dna_to_codons(reverse_complement(seq), 0))
    frames.append(translate_dna_to_codons(reverse_complement(seq), 1))
    frames.append(translate_dna_to_codons(reverse_complement(seq), 2))
    return frames
def proteins_from_rf(aa_seq):
    current_prot = []
    proteins = []
    for aa in aa_seq:
        if aa == "_":
            if current_prot:
                for p in current_prot:
                    proteins.append(p)
                current_prot = []
        else:
            if aa == "M":
                current_prot.append("")
            for i in range(len(current_prot)):
                current_prot[i] += aa
    return proteins

# Generate all reading frames
# extract all proteins
# Return a list of sorted/unsorted

def all_proteins_from_orfs(seq, startReadPos=0, endReadPos=0, ordered=False):
    """Compute all possible proteins for all open reading frames
    Protine Search DB: https//www.ncbi.nlm.hih.gov/nuccore/nm_001185097.2
    API can be used to pull protein info"""
    if endReadPos > startReadPos:
        rfs = gen_reading_frames(seq[startReadPos: endReadPos])
    else:
        rfs = gen_reading_frames(seq)

    res = []
    for rf in rfs:
        prots = proteins_from_rf(rf)
        for p in prots:
            res.append(p)

    if ordered:
        return sorted(res, key=len, reverse=True)
    return res



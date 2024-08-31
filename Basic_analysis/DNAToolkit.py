import collections
from Basic_analysis.structures import *

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

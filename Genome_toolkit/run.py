from genome_toolkit import genomeToolkit

gt = genomeToolkit()

seq = "AAGGATTAAGGGAAAAGCCCAGAA"
kmer = "AAGG"
print(f'kmers: {kmer}')
print(f'sequence: {seq}')
print(f'Repeats found: {gt.count_kmers(seq, kmer)}')
print(f'Most common kmers: {gt.find_most_frequent_kmer(seq, 5)}')

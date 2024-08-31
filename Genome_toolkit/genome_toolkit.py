import collections




class genomeToolkit:
    def __init__(self):
        print("Genome toolkit initialized")

    def count_kmers(self, sequence, kmer):
        """overlapping kmers are supported in this algorithm"""
        kmer_count = 0
        for position in range(len(sequence) - (len(kmer) - 1) ):
            if sequence[position:position + len(kmer)] == kmer:
                kmer_count += 1
        return kmer_count

    def find_most_frequent_kmer(self, sequence, k_len):

        kmer_frequencies = {}

        for i in range(len(sequence) - k_len +1):
            kmer = sequence[i:i + k_len]
            if kmer in kmer_frequencies:
                kmer_frequencies[kmer] += 1
            else:
                kmer_frequencies[kmer] = 1

        highest_frequency = max(kmer_frequencies.values())

        return [
            kmer for kmer, frequency in kmer_frequencies.items()
            if frequency == highest_frequency
        ]


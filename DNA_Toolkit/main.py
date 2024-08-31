from DNA_Toolkit.bio_seq import bio_seq

test_dna = bio_seq()
test_dna.generate_rnd_seq(40, "DNA")

print(test_dna.get_seq_info())
print(test_dna.nucleotide_frequency())
print(test_dna.transcription())
print(test_dna.seq)
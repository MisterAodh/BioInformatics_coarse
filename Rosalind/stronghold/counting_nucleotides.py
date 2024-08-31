def countNucFrequency(seq):
    tmpFreqDict = {"A":0, "C":0, "G":0, "T":0}
    for base in seq:
        tmpFreqDict[base] += 1
    return tmpFreqDict

dna_string = 'GTTTTAGAGGGCTGAATTGTTATGTGACTTTCAGATTCTTGAGTATAAACCCATGTCTTCCCTCTTAACACCGTGAAAATCACCCCCTTAAGAACTGTTCGCGTTGGTTAAATGGGATGAGAGGCACCAGGGACAGAGCCCTACCTAGGAATCGATTTCCTTGTCTACCTTTGAAAATCCCGCGGAAACCGATGTCCATATTGAGAAGGGATGACTGTCTACATTGAGACATAGAGCGTTGATTCTCTCCGTCAGGAAATGTTTCCTGGACTCCGAATCCATACGAAATGTACATCCTGCTGGGCAATAAGTAACACCCCCCTCTCACATTGGTGTCGCAAGGTATTCTTTGATGCAGCAGGCTTGTTGCTAAGCGTCTACCCTATTTTGGCAGAGGTGGCTTGGCCACGACGCTTCGCTCTCTTTGTAGGCTGGTTGGATGCTGCGCGTTACATTAAGTATGGGAGCCAACGATCTGACACGTACTTGACCATGTTTCAGCTCACATTCGATGTAGCATTGAGGTAACTCGTTCGATGGGGCCGTTTCGTCCATGTCCACTAACGGAGCCTCACTAAGCTTATTCTCAGCGCTATGGGGCGCTCTAGCCTGTGCTAGTCAACGCCTGCCCTGACTATTTCCTTCAATTATCATCCTATGAGTAAGCGAGCTTTACACGCGAATGAAACTTCATGCTATTATTAGAATCAAAGTCTCGCTCGCCTCGGGGGATGGAGGCATTGCCCATGAATTTCTACTATAATTCGATCCCTCGTCAGACCACACCAGGTTAAAGTTTAGAAGGAGTATTCACCAGTTGTCCTAACGTTGGATTTTAACCTATAGATCAATAATCATACTTCGGCGATCCAAAGGGTCCACGAGTACCTTGTTGTTAGGAAGTGATACAGCGACCGGTTCACACAAGGCTGCCCAGGCACTACCAGCCTCTTTGAGAACTCAGTATTCGCACCGGCCCGAGATCTCATGTCTCCGCATT'
output = ('')
for value in countNucFrequency(dna_string).values():
    output = output + str(value) + ' '
output = output[:-1]
# I am following along rebelScience youtube tutorial however my colde is a little different to his
print(output)
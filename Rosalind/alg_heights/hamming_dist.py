dna_str_1 = "TTCGATCCATTG"
dna_str_2 = "TTCGATCCATT"

def h_d_loop(str1, str2):
    h_distance = 0
    for position in range(len(str1)):
        if str1[position] != str2[position]:
            h_distance += 1
    return h_distance

def h_d_set(str1, str2):
    nucleotide_set_1 = set([(x, y) for x, y in enumerate(str1)])
    nucleotide_set_2 = set([(x, y) for x, y in enumerate(str2)])
    return len(nucleotide_set_1.difference(nucleotide_set_2))

def h_d_zip(str1, str2):
    h_distance = [(n1, n2) for n1, n2 in zip(str1, str2) if n1 != n2]



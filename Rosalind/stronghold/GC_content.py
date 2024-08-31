def gc_content(seq):
    # gc content is yhe percent of guanine and cytosine compared to adesine and thymine
    return round(100*((seq.count('G') + seq.count('C'))/ len(seq)), 6)

def gc_content_subsec(seq, k=20):
    """GC Content in a dna/rna sub sequence lenght k. k=20 by default"""
    res = []
    for i in range(0, len(seq) - k + 1, k):
        sebseq = seq[i:i + k]
        res.append(gc_content(sebseq))
    return res

def calc_highest_gc(filename):
    with open(filename, "r") as file:
        FASTAFile = [l.strip() for l in file.readlines()]
        FASTADict = {}
        FASTALabel = ""
        for line in FASTAFile:
            if '>' in line:
                FASTALabel = line
                FASTADict[FASTALabel] = ""
            else:
                FASTADict[FASTALabel] += line
        results_dict = {key: gc_content(value) for (key, value) in FASTADict.items()}
        MAxGC = max(results_dict, key=results_dict.get)
        print(results_dict)
        print(f'{MAxGC}\n{results_dict[MAxGC]}')



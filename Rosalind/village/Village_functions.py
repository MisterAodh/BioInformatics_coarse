def triangle_hypotenous(a, b):
    c_sq = a**2 + b**2
    return c_sq

def read_values(file_name):
    with open(file_name, "r") as file:
        content = file.read()
    list = content.split(' ')
    a = int(list[0])
    b = int(list[1])
    c = triangle_hypotenous(a, b)
    return c


def read_text(file_name):
    with open(file_name, "r") as file:
        content = file.read()
    x = content.split("\n")
    s = x[0]  # The string is the first line
    numbers = x[1].split(' ')
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])
    a_b = s[numbers[0]:numbers[1]+1]  # Slice the string s
    c_d = s[numbers[2]:numbers[3]+1]  # Slice the string s
    return f'{a_b} {c_d}'

def sum_odds(a, b):
    x = 0
    for i in range(a, b+1):
        if i % 2 != 0:
            x += i
    return x

def even_lines(filename):
    with open(filename, "r") as file:
        content = file.read()
        lines = content.split("\n")
    return_lines = []
    for i in range(len(lines)):

        if i % 2 != 0:
            return_lines.append(lines[i])

    file_name = "village_5_results.txt"
    with open(file_name, "w") as file:
        for line in return_lines:
            file.write(line + "\n")

def count_words(filename):
    with open(filename, "r") as file:
        content = file.read()
        words = content.split(' ')
    occurance_dictionary = {}
    for word in words:
        if word in occurance_dictionary:
            occurance_dictionary[word] += 1
        else:
            occurance_dictionary[word] = 1
    return occurance_dictionary
occurrences_dict = count_words("rosalind_ini5.txt")
for key in sorted(occurrences_dict):
    print(f"{key} {occurrences_dict[key]}")

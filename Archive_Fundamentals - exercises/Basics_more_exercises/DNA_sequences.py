score = int(input())
points = {
    "A": 1,
    "C": 2,
    "G": 3,
    "T": 4
}


all_iterations = ['AAA', 'AAC', 'AAG', 'AAT',
                  'ACA', 'ACC', 'ACG', 'ACT',
                  'AGA', 'AGC', 'AGG', 'AGT',
                  'ATA', 'ATC', 'ATG', 'ATT',
                  'CAA', 'CAC', 'CAG', 'CAT',
                  'CCA', 'CCC', 'CCG', 'CCT',
                  'CGA', 'CGC', 'CGG', 'CGT',
                  'CTA', 'CTC', 'CTG', 'CTT',
                  'GAA', 'GAC', 'GAG', 'GAT',
                  'GCA', 'GCC', 'GCG', 'GCT',
                  'GGA', 'GGC', 'GGG', 'GGT',
                  'GTA', 'GTC', 'GTG', 'GTT',
                  'TAA', 'TAC', 'TAG', 'TAT',
                  'TCA', 'TCC', 'TCG', 'TCT',
                  'TGA', 'TGC', 'TGG', 'TGT',
                  'TTA', 'TTC', 'TTG', 'TTT']

counter = 1
for letter in all_iterations:
    if points[letter[0]] + points[letter[1]] + points[letter[2]] >= score:
        print(f"O{letter}O", end=" ")
    else:
        print(f"X{letter}X", end=" ")
    if counter % 4 == 0:
        print()
    counter += 1

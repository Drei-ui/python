def complement(dna):
    comp = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    compdna = ''
    for i in dna:
        compdna += comp[i]
    return compdna


def reverse(dna):
    return dna[::-1]


def reversecomp(dna):
    compdna = complement(dna)
    revdna = reverse(compdna)
    return revdna


dna = input('Enter DNA sequence: ')
dna = dna.upper()
print('THe DNA input is:', dna)
print('')
print('The frequency of Adenine:', dna.count('A'))
print('The frequency of Guanine:', dna.count('G'))
print('The frequency of Cytosine:', dna.count('C'))
print('The frequency of Thymine:', dna.count('T'))
print('')
print('The length of the DNA string is', str(len(dna)))
print('The reversed complement of the DNA is', reversecomp(dna))

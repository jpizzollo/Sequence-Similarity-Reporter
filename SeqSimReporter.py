# Sequence similarity reporter

# This script takes as input:
#    1) probe: query sequence
#    2) target: sequence in which to scan for similarity

# query sequence:
probe="ggtttatgga"
# target sequence
target="atctacagaatgatcaaacccagaattgttctccttatttttgtttctggaaaagttgtattaacaggtgctaaagtcagagcagaaatttatgaagcatttgaaaacatctaccctattctaaagggattcaggaagacgacgtaaactgagaacaccgcgcagcgtgactgtgagttgctcataccgtgctgctatctgggcagcgctgcccatttatttatatgtagattttaaacactgctgttgacaagttggtttgagggagaaaactttaagtgttaaagccacctctataattgattggactttttaattttaatgtttttccccatgaaccacagtttttatatttctaccagaaaagtaaaaatcttttttaaaagtgttgtttttctaatttataactcctaggggttatttctgtgccagacacattccacctctccagtattgcaggacagaatatatgtgttaatgaaaatgaatggctgtacatatttttttctttcttcagagtactctgtacaataaatgcagtttataaaagtgtta"

# Set the minimum number of matching bases to report
threshold=8

probe=probe.upper()
target=target.upper()

# Get the probe reverse complement
prober = probe[::-1]
NUC = "ATCG"
NUCCOMP = "TAGC"
trantab = str.maketrans(NUC, NUCCOMP)
proberc = prober.translate(trantab)


i=0
j=len(probe)
report={}

# Inerate through all target sub-sequences of len(probe)
while i+j<len(target):
    region=target[i:i+j]
    match=0
    pos=0
# Check the forward strand
    for base in range(j):
        if probe[base]==region[base]:
            match+=1
    # Adjust match threshold
    if match>=threshold:
        report[i]=[region, match]
# Check the reverse strand
    match=0
    pos=0
    for base in range(j):
        if proberc[base]==region[base]:
            match+=1
    # Adjust match threshold
    if match>=threshold:
        key="{}r".format(i)
        report[key]=[region, match]
    i+=1

len(report)
# Report values:
#   first col, key, is the index position in the target sequence, with matches on the reverse strand indicated with index"r"
#   second col is the target sequence with some number of bases that match the query sequence
#   third col is the number of bases that match the query sequence
for key in report:
    print("{}\t{}\t{}".format(key, report[key][0], report[key][1]))

# SeqSimReporter.py

This script searches for sequences within a specified target that are similar to a probe sequence. The results are target matches, the index position for those matches, and the number of bases that match the probe.

### Example

Paste your probe and target sequence in the script:

```

probe="ggtttatgga"

target="atctacagaatgatcaaacccagaattgttctccttatttttgtttctggaaaagttgtattaacaggtgctaaagtcagagcagaaatttatgaagcatttgaaaacatctaccctattctaaagggattcaggaagacgacgtaaactgagaacaccgcgcagcgtgactgtgagttgctcataccgtgctgctatctgggcagcgctgcccatttatttatatgtagattttaaacactgctgttgacaagttggtttgagggagaaaactttaagtgttaaagccacctctataattgattggactttttaattttaatgtttttccccatgaaccacagtttttatatttctaccagaaaagtaaaaatcttttttaaaagtgttgtttttctaatttataactcctaggggttatttctgtgccagacacattccacctctccagtattgcaggacagaatatatgtgttaatgaaaatgaatggctgtacatatttttttctttcttcagagtactctgtacaataaatgcagtttataaaagtgtta"

```
Set the minimum number of matching bases to report
```
threshold=8

```



#### Output
The first column shows index position for the start of the match, with "r" indicating if the match is on the reverse strand. The second column is the matching sequence on the forward strand (even if the match is on the reverse). The third column is the number of matching bases.
```

41    TGTTTCTGGA	8
330r  CCCATGAACC	8

```

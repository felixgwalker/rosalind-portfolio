# Transcribing DNA into RNA (RNA)
# Rosalind problem: https://rosalind.info/problems/rna/
#
# Problem: Given a DNA string, produce the corresponding RNA transcript by
# replacing every Thymine (T) with Uracil (U). A, C, G are unchanged.
#
# Algorithm: str.replace scans the string once — O(n).

import os
import sys

def get_input():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', 'rosalind-files', 'rosalind_rna.txt')
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip()
    return sys.stdin.read().strip()

def solve(data):
    print(data.strip().replace('T', 'U'))

if __name__ == '__main__':
    solve(get_input())

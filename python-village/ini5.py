# Working with Files (INI5)
# Rosalind problem: https://rosalind.info/problems/ini5/
#
# Problem: Given a file containing at most 1000 lines, print every second
# line starting from the second line (i.e., lines at 1-based positions 2, 4, 6...).
#
# The dataset file is input.txt located in the same directory as this script.
# Indexing: enumerate() gives 0-based index; odd indices (1, 3, 5...) = even-numbered lines.

import os

script_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(script_dir, 'input.txt')

with open(input_path, 'r') as f:
    for index, line in enumerate(f):
        if index % 2 != 0:          # keep 0-indexed odd lines = 1-based even lines
            print(line.strip())

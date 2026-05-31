# Installing Python (INI1)
# Rosalind problem: https://rosalind.info/problems/ini1/
#
# Problem: After installing Python, verify the installation by running a short
# snippet. The sample dataset asks for the result of: 17 ** 1000 % 10
#
# The last digit of 17^n follows the cycle 7,9,3,1,7,9,3,1,... (period 4).
# 1000 mod 4 == 0, so 17^1000 ends in 1.  That is, 17**1000 % 10 == 1.

result = 17 ** 1000 % 10
print(result)

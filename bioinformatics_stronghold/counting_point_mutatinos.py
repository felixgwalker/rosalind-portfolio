# 	Counting Point Mutations

with open("C:/Users/user/Documents/Python_code/Rosalind_code/rosalind_files/rosalind_hamm.txt", "r") as f:
    s = f.readline().strip()
    t = f.readline().strip()

distance = 0

for i in range(len(s)):
    if s[i] != t[i]:
        distance += 1

print(distance)

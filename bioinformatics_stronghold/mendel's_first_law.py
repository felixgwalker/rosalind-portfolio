# 	Mendel's First Law

with open("C:/Users/user/Documents/Python_code/Rosalind_code/rosalind_files/rosalind_iprb.txt", "r") as file:
    dominant, heterozygous, recessive = map(int, file.read().split())

total = dominant + heterozygous + recessive

prob_recessive_child = (
    (recessive / total) * ((recessive - 1) / (total - 1)) +
    0.5 * (
        (recessive / total) * (heterozygous / (total - 1)) +
        (heterozygous / total) * (recessive / (total - 1))
    ) +
    0.25 * (
        (heterozygous / total) * ((heterozygous - 1) / (total - 1))
    )
)

prob_dominant_child = 1 - prob_recessive_child

print(prob_dominant_child)

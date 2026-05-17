import math

def prob_random_genome(s, gc_contents):
    results = []
    for x in gc_contents:
        log_prob = 0.0
        for base in s:
            if base in 'GC':
                log_prob += math.log10(x / 2)
            else:  # A or T
                log_prob += math.log10((1 - x) / 2)
        results.append(round(log_prob, 3))
    return results


if __name__ == "__main__":
    with open("rosalind_files/rosalind_prob.txt") as f:
        s = f.readline().strip()
        gc_contents = list(map(float, f.readline().split()))

    result = prob_random_genome(s, gc_contents)
    print(" ".join(str(v) for v in result))

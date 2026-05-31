# BA8B — Compute the Distortion of a Clustering
# https://rosalind.info/problems/ba8b/
#
# Given: k centers and a set of data points.
# Return: the distortion (sum of squared distances from each point to nearest center).

import os, sys
import math

def get_input():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rosalind-files', 'rosalind_ba8b.txt')
    return (open(p).read() if os.path.exists(p) else sys.stdin.read()).strip()

def dist2(a, b):
    return sum((x-y)**2 for x,y in zip(a,b))

def solve(data):
    lines = data.splitlines()
    k, m = map(int, lines[0].split())
    centers = [list(map(float, lines[i+1].split())) for i in range(k)]
    points = [list(map(float, l.split())) for l in lines[k+2:] if l.strip()]
    distortion = sum(min(dist2(p, c) for c in centers) for p in points) / len(points)
    print(f"{distortion:.3f}")

if __name__ == '__main__': solve(get_input())

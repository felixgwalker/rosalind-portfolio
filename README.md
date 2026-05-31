# Rosalind Bioinformatics Portfolio

Solutions to all problems on [rosalind.info](https://rosalind.info), written in Python using only the standard library — no BioPython or other bioinformatics packages.

## Repository Layout

```
rosalind-portfolio/
├── python-village/             # Introductory Python problems (INI1–INI6)
├── bioinformatics-stronghold/  # Core bioinformatics algorithms (~90 problems)
├── algorithmic-heights/        # Classical algorithms: graphs, sorting, DP
├── textbook-track/             # Compeau & Pevzner textbook BA1A–BA10J (~100 problems)
├── armory/                     # Bioinformatics databases & tools
└── rosalind-files/             # Downloaded dataset files (rosalind_<id>.txt)
```

### Input convention

Every solution checks for `rosalind-files/rosalind_<id>.txt` and reads from it if present; otherwise it reads from `stdin`. Drop your downloaded dataset file into `rosalind-files/` and run the script directly, or pipe input from the terminal.

---

## Python Village

| ID | Problem | File | Status |
|----|---------|------|--------|
| INI1 | Installing Python | [ini1.py](python-village/ini1.py) | Solved |
| INI2 | Variables and Some Arithmetic | [ini2.py](python-village/ini2.py) | Solved |
| INI3 | Strings and Lists | [ini3.py](python-village/ini3.py) | Solved |
| INI4 | Conditions and Loops | [ini4.py](python-village/ini4.py) | Solved |
| INI5 | Working with Files | [ini5.py](python-village/ini5.py) | Solved |
| INI6 | Dictionaries | [ini6.py](python-village/ini6.py) | Solved |

---

## Bioinformatics Stronghold

| ID | Problem | File | Status |
|----|---------|------|--------|
| DNA | Counting DNA Nucleotides | [dna.py](bioinformatics-stronghold/dna.py) | Solved |
| RNA | Transcribing DNA into RNA | [rna.py](bioinformatics-stronghold/rna.py) | Solved |
| REVC | Complementing a Strand of DNA | [revc.py](bioinformatics-stronghold/revc.py) | Solved |
| FIB | Rabbits and Recurrence Relations | [fib.py](bioinformatics-stronghold/fib.py) | Solved |
| GC | Computing GC Content | [gc.py](bioinformatics-stronghold/gc.py) | Solved |
| HAMM | Counting Point Mutations | [hamm.py](bioinformatics-stronghold/hamm.py) | Solved |
| IPRB | Mendel's First Law | [iprb.py](bioinformatics-stronghold/iprb.py) | Solved |
| PROT | Translating RNA into Protein | [prot.py](bioinformatics-stronghold/prot.py) | Solved |
| SUBS | Finding a Motif in DNA | [subs.py](bioinformatics-stronghold/subs.py) | Solved |
| CONS | Consensus and Profile | [cons.py](bioinformatics-stronghold/cons.py) | Solved |
| FIBD | Mortal Fibonacci Rabbits | [fibd.py](bioinformatics-stronghold/fibd.py) | Solved |
| GRPH | Overlap Graphs | [grph.py](bioinformatics-stronghold/grph.py) | Solved |
| IEV | Calculating Expected Offspring | [iev.py](bioinformatics-stronghold/iev.py) | Solved |
| LIA | Independent Alleles | [lia.py](bioinformatics-stronghold/lia.py) | Solved |
| MPRT | Finding a Protein Motif | [mprt.py](bioinformatics-stronghold/mprt.py) | Solved (needs internet) |
| MRNA | Inferring mRNA from Protein | [mrna.py](bioinformatics-stronghold/mrna.py) | Solved |
| ORF | Open Reading Frames | [orf.py](bioinformatics-stronghold/orf.py) | Solved |
| PERM | Enumerating Gene Orders | [perm.py](bioinformatics-stronghold/perm.py) | Solved |
| PRTM | Calculating Protein Mass | [prtm.py](bioinformatics-stronghold/prtm.py) | Solved |
| REVP | Locating Restriction Sites | [revp.py](bioinformatics-stronghold/revp.py) | Solved |
| SPLC | RNA Splicing | [splc.py](bioinformatics-stronghold/splc.py) | Solved |
| LGIS | Longest Increasing Subsequence | [lgis.py](bioinformatics-stronghold/lgis.py) | Solved |
| LONG | Genome Assembly as Shortest Superstring | [long.py](bioinformatics-stronghold/long.py) | Solved |
| PMCH | Perfect Matchings and RNA Secondary Structures | [pmch.py](bioinformatics-stronghold/pmch.py) | Solved |
| PPER | Partial Permutations | [pper.py](bioinformatics-stronghold/pper.py) | Solved |
| PROB | Introduction to Random Strings | [prob.py](bioinformatics-stronghold/prob.py) | Solved |
| SIGN | Enumerating Oriented Gene Orderings | [sign.py](bioinformatics-stronghold/sign.py) | Solved |
| SSEQ | Finding a Spliced Motif | [sseq.py](bioinformatics-stronghold/sseq.py) | Solved |
| TRAN | Transitions and Transversions | [tran.py](bioinformatics-stronghold/tran.py) | Solved |
| TREE | Completing a Tree | [tree.py](bioinformatics-stronghold/tree.py) | Solved |
| CAT | Catalan Numbers and RNA Secondary Structures | [cat.py](bioinformatics-stronghold/cat.py) | Solved |
| CORR | Error Correction in Reads | [corr.py](bioinformatics-stronghold/corr.py) | Solved |
| INOD | Counting Phylogenetic Ancestors | [inod.py](bioinformatics-stronghold/inod.py) | Solved |
| KMER | k-Mer Composition | [kmer.py](bioinformatics-stronghold/kmer.py) | Solved |
| KMP | Speeding Up Motif Finding | [kmp.py](bioinformatics-stronghold/kmp.py) | Solved |
| LCSQ | Finding a Shared Spliced Motif | [lcsq.py](bioinformatics-stronghold/lcsq.py) | Solved |
| LEXF | Enumerating k-mers Lexicographically | [lexf.py](bioinformatics-stronghold/lexf.py) | Solved |
| MMCH | Maximum Matchings and RNA Secondary Structures | [mmch.py](bioinformatics-stronghold/mmch.py) | Solved |
| PDST | Creating a Distance Matrix | [pdst.py](bioinformatics-stronghold/pdst.py) | Solved |
| REAR | Reversal Distance | [rear.py](bioinformatics-stronghold/rear.py) | Solved |
| RSTR | Matching Random Motifs | [rstr.py](bioinformatics-stronghold/rstr.py) | Solved |
| SSET | Counting Subsets | [sset.py](bioinformatics-stronghold/sset.py) | Solved |
| ASPC | Introduction to Alternative Splicing | [aspc.py](bioinformatics-stronghold/aspc.py) | Solved |
| EDIT | Edit Distance | [edit.py](bioinformatics-stronghold/edit.py) | Solved |
| EVAL | Expected Number of Restriction Sites | [eval.py](bioinformatics-stronghold/eval.py) | Solved |
| MOTZ | Motzkin Numbers and RNA Secondary Structures | [motz.py](bioinformatics-stronghold/motz.py) | Solved |
| NWCK | Distances in Trees | [nwck.py](bioinformatics-stronghold/nwck.py) | Solved |
| SCSP | Interleaving Two Motifs | [scsp.py](bioinformatics-stronghold/scsp.py) | Solved |
| SETO | Introduction to Set Operations | [seto.py](bioinformatics-stronghold/seto.py) | Solved |
| SORT | Sorting by Reversals | [sort.py](bioinformatics-stronghold/sort.py) | Solved |
| SPEC | Inferring Protein from Spectrum | [spec.py](bioinformatics-stronghold/spec.py) | Solved |
| TRIE | Introduction to Pattern Matching | [trie.py](bioinformatics-stronghold/trie.py) | Solved |
| CONV | Comparing Spectra with the Spectral Convolution | [conv.py](bioinformatics-stronghold/conv.py) | Solved |
| FULL | Inferring Peptide from Full Spectrum | [full.py](bioinformatics-stronghold/full.py) | Solved |
| INDC | Independent Segregation of Chromosomes | [indc.py](bioinformatics-stronghold/indc.py) | Solved |
| ITWV | Finding Disjoint Motifs in a Gene | [itwv.py](bioinformatics-stronghold/itwv.py) | Solved |
| LREP | Finding the Longest Multiple Repeat | [lrep.py](bioinformatics-stronghold/lrep.py) | Solved |
| NKEW | Distances in Trees with Weights | [nkew.py](bioinformatics-stronghold/nkew.py) | Solved |
| RNAS | Wobble Bonding and RNA Secondary Structures | [rnas.py](bioinformatics-stronghold/rnas.py) | Solved |
| AFRQ | Counting Disease Carriers | [afrq.py](bioinformatics-stronghold/afrq.py) | Solved |
| CSTR | Creating a Character-Based Phylogeny | [cstr.py](bioinformatics-stronghold/cstr.py) | Solved |
| CTBL | Creating a Character Table from Leaves | [ctbl.py](bioinformatics-stronghold/ctbl.py) | Solved |
| DBRU | Constructing a De Bruijn Graph | [dbru.py](bioinformatics-stronghold/dbru.py) | Solved |
| EDTA | Edit Distance Alignment | [edta.py](bioinformatics-stronghold/edta.py) | Solved |
| GLOB | Global Alignment with Scoring Matrix | [glob.py](bioinformatics-stronghold/glob.py) | Solved |
| PCOV | Genome Assembly with Perfect Coverage | [pcov.py](bioinformatics-stronghold/pcov.py) | Solved |
| PRSM | Matching a Spectrum to a Protein | [prsm.py](bioinformatics-stronghold/prsm.py) | Solved |
| SGRA | Using the Spectrum Graph to Infer Peptides | [sgra.py](bioinformatics-stronghold/sgra.py) | Solved |
| SUFF | Encoding Suffix Trees | [suff.py](bioinformatics-stronghold/suff.py) | Solved |
| BPHR | Base Quality Distribution | [bphr.py](bioinformatics-stronghold/bphr.py) | Solved |
| CLUS | Global Multiple Alignment | [clus.py](bioinformatics-stronghold/clus.py) | Solved |
| EBIN | Wright-Fisher's Model of Genetic Drift | [ebin.py](bioinformatics-stronghold/ebin.py) | Solved |
| FOUN | The Founder Effect and Genetic Drift | [foun.py](bioinformatics-stronghold/foun.py) | Solved |
| GAFF | Global Alignment with Affine Gap Penalty | [gaff.py](bioinformatics-stronghold/gaff.py) | Solved |
| LAFF | Local Alignment with Affine Gap Penalty | [laff.py](bioinformatics-stronghold/laff.py) | Solved |
| LING | Linguistic Complexity of a Genome | [ling.py](bioinformatics-stronghold/ling.py) | Solved |
| LOCA | Local Alignment with Scoring Matrix | [loca.py](bioinformatics-stronghold/loca.py) | Solved |
| OAP | Overlap Alignment | [oap.py](bioinformatics-stronghold/oap.py) | Solved |
| SEXL | Sex-Linked Inheritance | [sexl.py](bioinformatics-stronghold/sexl.py) | Solved |
| WFMD | The Wright-Fisher Model of Genetic Drift | [wfmd.py](bioinformatics-stronghold/wfmd.py) | Solved |
| ASMQ | Assessing Assembly Quality with N50 and N75 | [asmq.py](bioinformatics-stronghold/asmq.py) | Solved |
| CSET | Fixing an Inconsistent Character Set | [cset.py](bioinformatics-stronghold/cset.py) | Solved |
| GASM | Genome Assembly Using Reads | [gasm.py](bioinformatics-stronghold/gasm.py) | Solved |
| GCON | Global Alignment with Constant Gap Penalty | [gcon.py](bioinformatics-stronghold/gcon.py) | Solved |
| LCON | Local Alignment with Constant Gap Penalty | [lcon.py](bioinformatics-stronghold/lcon.py) | Solved |
| PTRA | Protein Translation | [ptra.py](bioinformatics-stronghold/ptra.py) | Solved |
| RDAG | Searching a Graph with a Sink | [rdag.py](bioinformatics-stronghold/rdag.py) | Solved |

---

## Algorithmic Heights

| ID | Problem | File | Status |
|----|---------|------|--------|
| BINS | Binary Search | [bins.py](algorithmic-heights/bins.py) | Solved |
| DDEG | Double-Degree Array | [ddeg.py](algorithmic-heights/ddeg.py) | Solved |
| DEG | Degree Array | [deg.py](algorithmic-heights/deg.py) | Solved |
| HDAG | Hamiltonian Path in DAG | [hdag.py](algorithmic-heights/hdag.py) | Solved |
| INS | Insertion Sort | [ins.py](algorithmic-heights/ins.py) | Solved |
| PAR | 2-Way Partition | [par.py](algorithmic-heights/par.py) | Solved |
| PAR3 | 3-Way Partition | [par3.py](algorithmic-heights/par3.py) | Solved |
| 2SUM | 2-Sum Problem | [2sum.py](algorithmic-heights/2sum.py) | Solved |
| BFS | Breadth-First Search | [bfs.py](algorithmic-heights/bfs.py) | Solved |
| CC | Connected Components | [cc.py](algorithmic-heights/cc.py) | Solved |
| DIJ | Dijkstra's Algorithm | [dij.py](algorithmic-heights/dij.py) | Solved |
| HS | Heap Sort | [hs.py](algorithmic-heights/hs.py) | Solved |
| MED | Weighted Median | [med.py](algorithmic-heights/med.py) | Solved |
| MIS | Maximal Independent Set | [mis.py](algorithmic-heights/mis.py) | Solved |
| MS | Merge Sort | [ms.py](algorithmic-heights/ms.py) | Solved |
| QS | Quick Sort | [qs.py](algorithmic-heights/qs.py) | Solved |
| SQ | Square in a Graph | [sq.py](algorithmic-heights/sq.py) | Solved |
| SDAG | Shortest Paths in DAG | [sdag.py](algorithmic-heights/sdag.py) | Solved |
| 3SUM | 3-Sum Problem | [3sum.py](algorithmic-heights/3sum.py) | Solved |
| BFSP | Bellman-Ford Shortest Paths | [bfsp.py](algorithmic-heights/bfsp.py) | Solved |
| DAG | Testing Acyclicity | [dag.py](algorithmic-heights/dag.py) | Solved |
| GS | General Sink | [gs.py](algorithmic-heights/gs.py) | Solved |
| HEA | Building a Heap | [hea.py](algorithmic-heights/hea.py) | Solved |
| SC | Semi-Connected Graph | [sc.py](algorithmic-heights/sc.py) | Solved |
| TS | Topological Sorting | [ts.py](algorithmic-heights/ts.py) | Solved |
| LONG | Longest Path in a DAG | [long.py](algorithmic-heights/long.py) | Solved |

---

## Bioinformatics Textbook Track

Problems from *Bioinformatics Algorithms* (Compeau & Pevzner).

### Chapter 1 — Finding Hidden Messages in DNA

| ID | Problem | File |
|----|---------|------|
| BA1A | Count occurrences of a pattern | [ba1a.py](textbook-track/ba1a.py) |
| BA1B | Most frequent k-mers | [ba1b.py](textbook-track/ba1b.py) |
| BA1C | Reverse complement | [ba1c.py](textbook-track/ba1c.py) |
| BA1D | All occurrences of a pattern | [ba1d.py](textbook-track/ba1d.py) |
| BA1E | Patterns forming clumps | [ba1e.py](textbook-track/ba1e.py) |
| BA1F | Position minimising skew | [ba1f.py](textbook-track/ba1f.py) |
| BA1G | Hamming distance | [ba1g.py](textbook-track/ba1g.py) |
| BA1H | Approximate pattern occurrences | [ba1h.py](textbook-track/ba1h.py) |
| BA1I | Frequent words with mismatches | [ba1i.py](textbook-track/ba1i.py) |
| BA1J | Frequent words with mismatches + rev comp | [ba1j.py](textbook-track/ba1j.py) |
| BA1K | Frequency array | [ba1k.py](textbook-track/ba1k.py) |
| BA1L | PatternToNumber | [ba1l.py](textbook-track/ba1l.py) |
| BA1M | NumberToPattern | [ba1m.py](textbook-track/ba1m.py) |
| BA1N | d-Neighborhood | [ba1n.py](textbook-track/ba1n.py) |

### Chapter 2 — Molecular Clocks

| ID | Problem | File |
|----|---------|------|
| BA2A | Motif Enumeration | [ba2a.py](textbook-track/ba2a.py) |
| BA2B | Median String | [ba2b.py](textbook-track/ba2b.py) |
| BA2C | Profile-most probable k-mer | [ba2c.py](textbook-track/ba2c.py) |
| BA2D | GreedyMotifSearch | [ba2d.py](textbook-track/ba2d.py) |
| BA2E | GreedyMotifSearch with pseudocounts | [ba2e.py](textbook-track/ba2e.py) |
| BA2F | RandomizedMotifSearch | [ba2f.py](textbook-track/ba2f.py) |
| BA2G | GibbsSampler | [ba2g.py](textbook-track/ba2g.py) |
| BA2H | Distance between pattern and strings | [ba2h.py](textbook-track/ba2h.py) |

### Chapter 3 — Genome Assembly

| ID | Problem | File |
|----|---------|------|
| BA3A–BA3L | k-mer composition through gapped path reconstruction | [ba3a.py](textbook-track/ba3a.py) … [ba3l.py](textbook-track/ba3l.py) |

### Chapter 4 — Antibiotic Sequencing

| ID | Problem | File |
|----|---------|------|
| BA4A–BA4I | RNA translation through convolution sequencing | [ba4a.py](textbook-track/ba4a.py) … [ba4i.py](textbook-track/ba4i.py) |

### Chapter 5 — Sequence Alignment

| ID | Problem | File |
|----|---------|------|
| BA5A–BA5N | Coins through multiple alignment | [ba5a.py](textbook-track/ba5a.py) … [ba5n.py](textbook-track/ba5n.py) |

### Chapter 6 — Genome Rearrangements

| ID | Problem | File |
|----|---------|------|
| BA6A–BA6J | GreedySorting through 2-BreakOnGenomeGraph | [ba6a.py](textbook-track/ba6a.py) … [ba6j.py](textbook-track/ba6j.py) |

### Chapters 7–10 — Phylogenetics, Clustering, Suffix Structures, HMMs

| Range | Topics | Files |
|-------|--------|-------|
| BA7A–BA7G | Phylogenetics (UPGMA, NJ, parsimony) | [ba7a.py](textbook-track/ba7a.py) … [ba7g.py](textbook-track/ba7g.py) |
| BA8A–BA8E | Clustering (k-means, hierarchical) | [ba8a.py](textbook-track/ba8a.py) … [ba8e.py](textbook-track/ba8e.py) |
| BA9A–BA9O | Suffix trees, BWT, pattern matching | [ba9a.py](textbook-track/ba9a.py) … [ba9o.py](textbook-track/ba9o.py) |
| BA10A–BA10J | HMMs, Viterbi, Baum-Welch | [ba10a.py](textbook-track/ba10a.py) … [ba10j.py](textbook-track/ba10j.py) |

---

## Bioinformatics Armory

> Problems marked *(needs web)* make HTTP requests to NCBI, UniProt, or PDB.

| ID | Problem | File | Status |
|----|---------|------|--------|
| INI | Introduction to the Armory | [ini.py](armory/ini.py) | Solved |
| GBK | GenBank Introduction | [gbk.py](armory/gbk.py) | Solved *(needs web)* |
| FRMT | Data Formats | [frmt.py](armory/frmt.py) | Solved *(needs web)* |
| MULT | Pairwise Global Alignment | [mult.py](armory/mult.py) | Solved |
| PDBT | PDB Introduction | [pdbt.py](armory/pdbt.py) | Solved *(needs web)* |
| GREP | Searching Datasets Globally | [grep.py](armory/grep.py) | Solved *(needs web)* |
| BFIL | Base Filtration by Quality | [bfil.py](armory/bfil.py) | Solved |
| OLIS | Online Bioinformatics Resources | [olis.py](armory/olis.py) | Solved *(needs web)* |
| DNAS | Identifying DNA Strings | [dnas.py](armory/dnas.py) | Solved *(needs web)* |
| ORI | Finding an Origin of Replication | [ori.py](armory/ori.py) | Solved |

---

## Design Principles

- **No bioinformatics libraries.** Every algorithm — from Needleman-Wunsch to Burrows-Wheeler, from UPGMA to Hierholzer's Eulerian circuit — is implemented from first principles using Python's standard library only.
- **Self-contained files.** Each solution is a standalone `.py` file with a header describing the problem, algorithm, and I/O format. Large constants (BLOSUM62, PAM250) are defined inline.
- **Dual input mode.** Drop `rosalind_<id>.txt` into `rosalind-files/` to run without typing; or pipe from stdin for generic use.
- **Descriptive comments.** Non-obvious algorithmic steps are annotated inline; straightforward code is left uncommented.

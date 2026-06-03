# Rosalind Bioinformatics Portfolio

Solutions to all problems on [rosalind.info](https://rosalind.info), written in Python using only the standard library — no BioPython or other bioinformatics packages.

## Repository Layout

```
rosalind-portfolio/
├── python-village/             # Introductory Python problems (INI1–INI6)
├── bioinformatics-stronghold/  # Core bioinformatics algorithms (105 problems)
├── algorithmic-heights/        # Classical algorithms: graphs, sorting, DP (34 problems)
├── bioinformatics-textbook-track/             # Compeau & Pevzner textbook BA1A–BA11J (124 problems)
├── bioinformatics-armory/      # Bioinformatics databases & tools
├── rosalind-inputs/            # Downloaded dataset files, split by track — gitignored
│   ├── bioinformatics-stronghold/
│   ├── algorithmic-heights/
│   ├── bioinformatics-textbook-track/
│   └── bioinformatics-armory/
└── rosalind-outputs/           # Generated answers, same layout — gitignored
```

### Input / output convention

Every solution checks for `rosalind-inputs/<track>/rosalind_<id>.txt` and reads from it if present; otherwise it falls back to `stdin`. Drop your downloaded dataset file into the matching track subdirectory and run the script directly — the answer is printed to the terminal **and** written to `rosalind-outputs/<track>/rosalind_<id>.txt` for easy access when output is long. Python Village problems (`ini*.py`) read from `stdin` only.

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
| LCSM | Finding a Shared Motif | [lcsm.py](bioinformatics-stronghold/lcsm.py) | Solved |
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
| LEXV | Ordering Strings of Varying Length Lexicographically | [lexv.py](bioinformatics-stronghold/lexv.py) | Solved |
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
| MULT | Multiple Alignment | [mult.py](bioinformatics-stronghold/mult.py) | Solved |
| CUNR | Counting Unrooted Binary Trees | [cunr.py](bioinformatics-stronghold/cunr.py) | Solved |
| PDPL | Creating a Distance Matrix from Restriction Maps | [pdpl.py](bioinformatics-stronghold/pdpl.py) | Solved |
| MREP | Finding the Longest Multiple Repeat | [mrep.py](bioinformatics-stronghold/mrep.py) | Solved |
| EUBT | Enumerating Unrooted Binary Trees | [eubt.py](bioinformatics-stronghold/eubt.py) | Solved |
| MEND | Inferring Genotype from a Pedigree | [mend.py](bioinformatics-stronghold/mend.py) | Solved |
| CHBP | Character-Based Phylogeny | [chbp.py](bioinformatics-stronghold/chbp.py) | Solved |
| QRT | Quartets | [qrt.py](bioinformatics-stronghold/qrt.py) | Solved |
| CTEA | Counting Topological Orderings of Evolutionary Ancestors | [ctea.py](bioinformatics-stronghold/ctea.py) | Solved |
| ALPH | Alignment-Based Phylogeny | [alph.py](bioinformatics-stronghold/alph.py) | Solved |
| MGAP | Maximizing the Gap Symbols of an Optimal Alignment | [mgap.py](bioinformatics-stronghold/mgap.py) | Solved |
| OSYM | Counting Palindromic Substrings | [osym.py](bioinformatics-stronghold/osym.py) | Solved |
| ROOT | Counting Rooted Binary Trees | [root.py](bioinformatics-stronghold/root.py) | Solved |
| SPTD | Phylogeny Comparison with Split Distance | [sptd.py](bioinformatics-stronghold/sptd.py) | Solved |
| SMGB | Semiglobal Alignment | [smgb.py](bioinformatics-stronghold/smgb.py) | Solved |
| CNTQ | Counting Quartets | [cntq.py](bioinformatics-stronghold/cntq.py) | Solved |
| QRTD | Quartet Distance | [qrtd.py](bioinformatics-stronghold/qrtd.py) | Solved |
| GREP | Genome Assembly with Perfect Coverage Revisited | [grep.py](bioinformatics-stronghold/grep.py) | Solved |
| SIMS | Finding a Motif with Modifications | [sims.py](bioinformatics-stronghold/sims.py) | Solved |
| RSUB | Identifying Reversing Substitutions | [rsub.py](bioinformatics-stronghold/rsub.py) | Solved |
| KSIM | Finding All Similar Motifs | [ksim.py](bioinformatics-stronghold/ksim.py) | Solved |

---

## Algorithmic Heights

| ID | Problem | File | Status |
|----|---------|------|--------|
| FIBO | Fibonacci Numbers | [fibo.py](algorithmic-heights/fibo.py) | Solved |
| BINS | Binary Search | [bins.py](algorithmic-heights/bins.py) | Solved |
| DEG | Degree Array | [deg.py](algorithmic-heights/deg.py) | Solved |
| INS | Insertion Sort | [ins.py](algorithmic-heights/ins.py) | Solved |
| MAJ | Majority Element | [maj.py](algorithmic-heights/maj.py) | Solved |
| 2SUM | 2-Sum Problem | [2sum.py](algorithmic-heights/2sum.py) | Solved |
| MS | Merge Sort | [ms.py](algorithmic-heights/ms.py) | Solved |
| MED | Weighted Median | [med.py](algorithmic-heights/med.py) | Solved |
| DDEG | Double-Degree Array | [ddeg.py](algorithmic-heights/ddeg.py) | Solved |
| MER | Merging Two Sorted Arrays | [mer.py](algorithmic-heights/mer.py) | Solved |
| BFS | Breadth-First Search | [bfs.py](algorithmic-heights/bfs.py) | Solved |
| CC | Connected Components | [cc.py](algorithmic-heights/cc.py) | Solved |
| HEA | Building a Heap | [hea.py](algorithmic-heights/hea.py) | Solved |
| PAR | 2-Way Partition | [par.py](algorithmic-heights/par.py) | Solved |
| 3SUM | 3-Sum Problem | [3sum.py](algorithmic-heights/3sum.py) | Solved |
| DIJ | Dijkstra's Algorithm | [dij.py](algorithmic-heights/dij.py) | Solved |
| BIP | Testing Bipartiteness | [bip.py](algorithmic-heights/bip.py) | Solved |
| DAG | Testing Acyclicity | [dag.py](algorithmic-heights/dag.py) | Solved |
| SQ | Square in a Graph | [sq.py](algorithmic-heights/sq.py) | Solved |
| HS | Heap Sort | [hs.py](algorithmic-heights/hs.py) | Solved |
| INV | Counting Inversions | [inv.py](algorithmic-heights/inv.py) | Solved |
| PAR3 | 3-Way Partition | [par3.py](algorithmic-heights/par3.py) | Solved |
| TS | Topological Sorting | [ts.py](algorithmic-heights/ts.py) | Solved |
| BF | Bellman-Ford Algorithm | [bf.py](algorithmic-heights/bf.py) | Solved |
| CTE | Shortest Cycle Through a Given Edge | [cte.py](algorithmic-heights/cte.py) | Solved |
| PS | Partial Sort | [ps.py](algorithmic-heights/ps.py) | Solved |
| NWC | Negative Weight Cycle | [nwc.py](algorithmic-heights/nwc.py) | Solved |
| QS | Quick Sort | [qs.py](algorithmic-heights/qs.py) | Solved |
| HDAG | Hamiltonian Path in DAG | [hdag.py](algorithmic-heights/hdag.py) | Solved |
| SCC | Strongly Connected Components | [scc.py](algorithmic-heights/scc.py) | Solved |
| SDAG | Shortest Paths in DAG | [sdag.py](algorithmic-heights/sdag.py) | Solved |
| 2SAT | 2-Satisfiability | [2sat.py](algorithmic-heights/2sat.py) | Solved |
| GS | General Sink | [gs.py](algorithmic-heights/gs.py) | Solved |
| SC | Semi-Connected Graph | [sc.py](algorithmic-heights/sc.py) | Solved |

---

## Bioinformatics Textbook Track

Problems from *Bioinformatics Algorithms* (Compeau & Pevzner).

### Chapter 1 — Finding Hidden Messages in DNA

| ID | Problem | File |
|----|---------|------|
| BA1A | Count occurrences of a pattern | [ba1a.py](bioinformatics-textbook-track/ba1a.py) |
| BA1B | Most frequent k-mers | [ba1b.py](bioinformatics-textbook-track/ba1b.py) |
| BA1C | Reverse complement | [ba1c.py](bioinformatics-textbook-track/ba1c.py) |
| BA1D | All occurrences of a pattern | [ba1d.py](bioinformatics-textbook-track/ba1d.py) |
| BA1E | Patterns forming clumps | [ba1e.py](bioinformatics-textbook-track/ba1e.py) |
| BA1F | Position minimising skew | [ba1f.py](bioinformatics-textbook-track/ba1f.py) |
| BA1G | Hamming distance | [ba1g.py](bioinformatics-textbook-track/ba1g.py) |
| BA1H | Approximate pattern occurrences | [ba1h.py](bioinformatics-textbook-track/ba1h.py) |
| BA1I | Frequent words with mismatches | [ba1i.py](bioinformatics-textbook-track/ba1i.py) |
| BA1J | Frequent words with mismatches + rev comp | [ba1j.py](bioinformatics-textbook-track/ba1j.py) |
| BA1K | Frequency array | [ba1k.py](bioinformatics-textbook-track/ba1k.py) |
| BA1L | PatternToNumber | [ba1l.py](bioinformatics-textbook-track/ba1l.py) |
| BA1M | NumberToPattern | [ba1m.py](bioinformatics-textbook-track/ba1m.py) |
| BA1N | d-Neighborhood | [ba1n.py](bioinformatics-textbook-track/ba1n.py) |

### Chapter 2 — Molecular Clocks

| ID | Problem | File |
|----|---------|------|
| BA2A | Motif Enumeration | [ba2a.py](bioinformatics-textbook-track/ba2a.py) |
| BA2B | Median String | [ba2b.py](bioinformatics-textbook-track/ba2b.py) |
| BA2C | Profile-most probable k-mer | [ba2c.py](bioinformatics-textbook-track/ba2c.py) |
| BA2D | GreedyMotifSearch | [ba2d.py](bioinformatics-textbook-track/ba2d.py) |
| BA2E | GreedyMotifSearch with pseudocounts | [ba2e.py](bioinformatics-textbook-track/ba2e.py) |
| BA2F | RandomizedMotifSearch | [ba2f.py](bioinformatics-textbook-track/ba2f.py) |
| BA2G | GibbsSampler | [ba2g.py](bioinformatics-textbook-track/ba2g.py) |
| BA2H | Distance between pattern and strings | [ba2h.py](bioinformatics-textbook-track/ba2h.py) |

### Chapter 3 — Genome Assembly

| ID | Problem | File |
|----|---------|------|
| BA3A–BA3M | k-mer composition through maximal non-branching paths | [ba3a.py](bioinformatics-textbook-track/ba3a.py) … [ba3m.py](bioinformatics-textbook-track/ba3m.py) |

### Chapter 4 — Antibiotic Sequencing

| ID | Problem | File |
|----|---------|------|
| BA4A–BA4M | RNA translation through Turnpike problem | [ba4a.py](bioinformatics-textbook-track/ba4a.py) … [ba4m.py](bioinformatics-textbook-track/ba4m.py) |

### Chapter 5 — Sequence Alignment

| ID | Problem | File |
|----|---------|------|
| BA5A–BA5N | Coins through multiple alignment | [ba5a.py](bioinformatics-textbook-track/ba5a.py) … [ba5n.py](bioinformatics-textbook-track/ba5n.py) |

### Chapter 6 — Genome Rearrangements

| ID | Problem | File |
|----|---------|------|
| BA6A–BA6K | GreedySorting through 2-BreakOnGenome | [ba6a.py](bioinformatics-textbook-track/ba6a.py) … [ba6k.py](bioinformatics-textbook-track/ba6k.py) |

### Chapters 7–11 — Phylogenetics, Clustering, Suffix Structures, HMMs, Proteomics

| Range | Topics | Files |
|-------|--------|-------|
| BA7A–BA7G | Phylogenetics (UPGMA, NJ, parsimony) | [ba7a.py](bioinformatics-textbook-track/ba7a.py) … [ba7g.py](bioinformatics-textbook-track/ba7g.py) |
| BA8A–BA8E | Clustering (k-means, hierarchical) | [ba8a.py](bioinformatics-textbook-track/ba8a.py) … [ba8e.py](bioinformatics-textbook-track/ba8e.py) |
| BA9A–BA9R | Suffix trees, BWT, pattern matching, partial suffix array | [ba9a.py](bioinformatics-textbook-track/ba9a.py) … [ba9r.py](bioinformatics-textbook-track/ba9r.py) |
| BA10A–BA10K | HMMs, Viterbi, Baum-Welch, forward-backward | [ba10a.py](bioinformatics-textbook-track/ba10a.py) … [ba10k.py](bioinformatics-textbook-track/ba10k.py) |
| BA11A–BA11J | De novo sequencing, peptide vectors, PSM search, spectral dictionaries | [ba11a.py](bioinformatics-textbook-track/ba11a.py) … [ba11j.py](bioinformatics-textbook-track/ba11j.py) |

---

## Bioinformatics Armory

> Problems marked *(needs web)* make HTTP requests to NCBI or UniProt.

| ID | Problem | File | Status |
|----|---------|------|--------|
| INI | Introduction to the Armory | [ini.py](bioinformatics-armory/ini.py) | Solved |
| GBK | GenBank Introduction | [gbk.py](bioinformatics-armory/gbk.py) | Solved *(needs web)* |
| MEME | New Motif Discovery | [meme.py](bioinformatics-armory/meme.py) | Solved |
| FRMT | Data Formats | [frmt.py](bioinformatics-armory/frmt.py) | Solved *(needs web)* |
| NEED | Pairwise Global Alignment | [need.py](bioinformatics-armory/need.py) | Solved |
| TFSQ | Transforming FASTQ to FASTA | [tfsq.py](bioinformatics-armory/tfsq.py) | Solved |
| PTRA | Protein Translation | [ptra.py](bioinformatics-armory/ptra.py) | Solved |
| SUBO | Suboptimal Local Alignment | [subo.py](bioinformatics-armory/subo.py) | Solved |
| PHRE | Phred Quality Scores | [phre.py](bioinformatics-armory/phre.py) | Solved |
| RVCO | Complementing a Strand of DNA | [rvco.py](bioinformatics-armory/rvco.py) | Solved |
| FILT | Read Quality Distribution | [filt.py](bioinformatics-armory/filt.py) | Solved |
| ORFR | Finding Genes with ORFs | [orfr.py](bioinformatics-armory/orfr.py) | Solved |
| CLUS | Global Multiple Alignment | [clus.py](bioinformatics-armory/clus.py) | Solved |
| BPHR | Base Quality Distribution | [bphr.py](bioinformatics-armory/bphr.py) | Solved |
| BFIL | Base Filtration by Quality | [bfil.py](bioinformatics-armory/bfil.py) | Solved |

---

## Design Principles

- **No bioinformatics libraries.** Every algorithm — from Needleman-Wunsch to Burrows-Wheeler, from UPGMA to Hierholzer's Eulerian circuit — is implemented from first principles using Python's standard library only.
- **Self-contained files.** Each solution is a standalone `.py` file with a header describing the problem, algorithm, and I/O format. Large constants (BLOSUM62, PAM250) are defined inline.
- **Dual input mode.** Drop `rosalind_<id>.txt` into `rosalind-inputs/<track>/` to run without typing; or pipe from stdin for generic use. Answers are automatically saved to `rosalind-outputs/<track>/` when running from a file.
- **Descriptive comments.** Non-obvious algorithmic steps are annotated inline; straightforward code is left uncommented.

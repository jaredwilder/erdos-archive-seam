# Mathematics recovered across archive boundaries

A recovery sweep of material outside the ordinary repository tree: 297 ZIP archives, two tarballs containing Lean sources, and a separate computational-result store.

This repository records the mathematics found there and routes mature subjects to dedicated repositories.

## Exact corrections and finite results

### Erdős #168

For subsets of `[1,n]` avoiding every triple `{k,2k,3k}`, exact computation gives

\[
F(10)=8,
\qquad
F(20)=16,
\qquad
F(30)=24,
\qquad
\boxed{F(42)=34}.
\]

The `F(42)=34` value corrects an earlier archived value of 30. The focused result is published in [`erdos168-triple-avoidance`](https://github.com/jaredwilder/erdos168-triple-avoidance).

### Universal two-digit additive collision

For every base `B>=2` and digits `a<b`,

\[
(aB+a)+(bB+b)=(aB+b)+(bB+a).
\]

Thus no complete two-digit positional family over an alphabet of size at least two is Sidon. The broader sharp encoding theory is in [`positional-encoding-thresholds`](https://github.com/jaredwilder/positional-encoding-thresholds).

### Ramsey `(5,5)` circulant structure

For

\[
G=\operatorname{Cay}(\mathbb Z_{41},\pm\{1,2,3,5,7,10,13,15,16,17\}),
\]

the recovered exact data include

```text
alpha(G) = omega(G) = 4
410 edges
1230 triangles
1025 K4s and 1025 independent 4-sets
chi(G) = 11
chi(G-v) = 10 for every v
Aut(G) has order 82
```

The focused structural and extension results are in [`ramsey-r55-circulant-41`](https://github.com/jaredwilder/ramsey-r55-circulant-41).

### Finite-to-infinite transfer

For any translation-invariant forbidden relation, if the exact maximum on an interval of length `L` is `M`, then every infinite relation-free set has upper density at most

\[
M/L.
\]

Applied to one exact `C_3` table with `M=11`, `L=50`, this gives the unconditional bound

\[
\overline d(A)\le 11/50.
\]

A later recovered `C_3(60)=12` instance strengthens the same mechanism to `1/5`; see [`pascal-relation-extremal-atlas`](https://github.com/jaredwilder/pascal-relation-extremal-atlas).

## Structural programs recovered

The archive layer also contained substantial work now organized elsewhere:

- induced-`P6` Erdős–Hajnal structure — [`p6-erdos-hajnal`](https://github.com/jaredwilder/p6-erdos-hajnal);
- Caccetta–Häggkvist boundary identities and exact finite relation tables — [`caccetta-haggkvist-triangles`](https://github.com/jaredwilder/caccetta-haggkvist-triangles);
- positional encoding thresholds — [`positional-encoding-thresholds`](https://github.com/jaredwilder/positional-encoding-thresholds);
- finite relation-family extrema — [`relation-family-atlas`](https://github.com/jaredwilder/relation-family-atlas);
- Erdős #385, #477, #700 and other compact theorems — [`erdos-proved-lemmas`](https://github.com/jaredwilder/erdos-proved-lemmas).

## Lean-source audit

The two tarballs contain 1,360 Lean files. The audit found:

```text
614 files with exit code 0
348 files with exit code 0 and a clean printed axiom footprint
291 distinct clean files after duplicate removal
119 problem numbers represented
```

A clean footprint alone is not enough to establish mathematical substance: many files are bounded decision procedures, harness self-tests, or arithmetic skeletons. Several strong standalone theorems do survive the audit, including results on quadratic tilings, finite-sums avoidance, covering degree, semiprime binomial gcds, and related number-theoretic identities.

The broader semantic lesson and receipt analysis are separated into [`formalizer-kernel-audit`](https://github.com/jaredwilder/formalizer-kernel-audit).

## Purpose of this repository

This is a recovery map for mathematics found outside normal source traversal. It is not intended to compete with the focused repositories above; when a subject has a dedicated home, that is the preferred place to read and cite it.

Author: Jared Wilder. License: Apache-2.0.

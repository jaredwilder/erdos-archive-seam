# The archive seam

**Mathematics recovered from 297 archives, two tarballs, and a computational store that no
directory walk sees.**

Author: Jared Wilder. Published 2026-09-11.

Three separate passes, each into material that sits outside the searchable tree: 907 zip archives in
a downloads folder (297 opened here), two tarballs holding 1,360 Lean files across 119 problem
numbers, and an exhaustive-search result store.

**Claims I re-verified myself are marked [verified].** The rest are reported with their source and
should be treated as leads until checked.

---

## The headline: an estate flagship is false, and its own audit said so

Two audits of the same corpus disagreed about Erdos 168, which asks for the largest subset of
`[1,n]` containing no triple `{k, 2k, 3k}`.

- One inventory records: *"Exact F(42)=30 (witness+bound) refutes the 3/7 residue-periodic density
  conjecture"* and treats it as a flagship result.
- A later audit rejects exactly that, exhibiting a 34-element subset of `[1,42]` avoiding every
  `{k,2k,3k}`.

**At most one could be right. I settled it by exact computation.** [verified]

```
F(10) = 8      F(20) = 16      F(30) = 24      F(42) = 34
```

**F(42) = 34.** The audit is right, the flagship is false, and the "refutation of the residue-periodic
density conjecture" that rested on `F(42)=30` establishes nothing.

The minimum hitting set for the triples `{k,2k,3k}` in `[1,42]` has size 8, so the maximum avoiding
set has size `42 - 8 = 34`. Computed by exact branch and bound, not search heuristics.

---

## A complete negative result, hand-checkable in thirty seconds [verified]

For any base `B >= 2` and any two digits `a < b`, the four two-digit words satisfy

```
(aB + a) + (bB + b)  =  (aB + b) + (bB + a)  =  (a + b)(B + 1)
```

and all four are distinct. **So no fixed digit alphabet of size 2 or more is Sidon in any base.**

Verified for every base `2..11` and every digit pair. The identity is immediate, which is the point:
a whole family of proposed Sidon constructions is dead on arrival, and the obstruction fits on one
line.

---

## Exact classifications recovered from the archives

Reported from their source archives. These are the kind of result that is expensive to produce and
cheap to check, and none of them was in a findings document.

### Erdos-Hajnal, the P6 wall

In the source-bound 3-tooth complement-comb model with stable handles and two vertices per tooth:
**exactly 5,680 of 32,768 configurations contain an induced P6.** The pairwise rectangle law rejects
5,440, leaving **240** pairwise-legal P6-containing configurations, whose inclusion-minimal forcing
patterns number **252 in 8 symmetry orbits**.

In the induced dominating `K(3,3)` private-representative model, encoding the 15 private edges and
deciding all 32,768 states: **exactly four** graphs extend to a P6-free full graph, and all four are
cluster graphs (empty, X-clique only, Y-clique only, complete).

Alongside: a 30-case classification of nonempty proper P5 signatures, each rejection carrying an
explicit 6-vertex co-P6 witness.

### Caccetta-Haggkvist at r=3, an exact defect budget

For a minimum counterexample with `d = ceil(n/3)`, arc-minimality forces `d+(v) = d` everywhere and
**`n` in `{3d-1, 3d}`**, so the boundary surplus `delta = 3d - (n-1)` is 2 or 1. Fourth-moment bound:
`tr(A^4) >= n d^2 (3d + 2 - n)`. Every critical edge has **`O(a,b) <= ceil(d/3) - 1`**.

The route replaces Razborov's edge potential with the exact identity
`F(a,b) = O(a,b) + d-(b) - 1 - Q_ab`, and proves the key step by an **exhaustive 21-state relation
table**: triangle-freeness kills two states, the score is at most 1 in twenty of them, and equals 2
only in the single Twisted-Circle witness.

### The Ramsey (5,5) witness has unmined exact structure

`G = Cay(Z41, +/-{1,2,3,5,7,10,13,15,16,17})`. The multiplier `phi(x) = 9x` gives `9S = Z41* \ S` and
`9^2 = -1 (mod 41)`, so **G is explicitly isomorphic to its own complement**.

```
alpha = omega = 4       410 edges      1230 triangles
1025 K4's and 1025 I4's
chi(G) = 11             chi(G - v) = 10 for every v   (11-chromatic vertex-critical)
Aut(G) = D41, order 82
clique polynomial  1 + 41x + 410x^2 + 1230x^3 + 1025x^4
```

The chromatic lower bound is `ceil(41/4)`; the upper bound comes from the ten classes
`C_k = {4(4k+1), .., 4(4k+4)}`, whose internal differences `+/-4, +/-8, +/-12` all miss `S`, plus `{0}`.
`Aut` follows from Burnside on prime degree (affine) plus the fact that only `+/-1` satisfy `aS = S`.

Two related facts worth keeping: **G is not strongly regular**, so it is genuinely distinct from
Paley(41), and Paley(41) itself contains monochromatic K5 in both colours and is **not** a (5,5)
witness. Separately, **no circulant (5,5) witness exists on Z42** (all 2,097,151 inverse-closed sets
checked), while witnesses exist at n=40 and n=41 and none at 39: non-monotone inside the circulant
family.

### Erdos 385, the complete failure set

`F(n) = max over composite m < n of m + p(m)`. The certificate in the store lists 9 failures for
`n <= 200`. The true set for `n <= 200` has **29** members, and the complete set for `n <= 6,000,000`
is exactly **100 values**, largest **267,680**:

```
6, 8, 12, 14, 18, 20, 24, 30, 32, 42, 44, 48, 60, 62, 72, 74, 84, 90, 102, 104, 108, 110, 114,
132, 140, 168, 182, 198, 200, 234, 240, 242, 270, 272, 282, 284, 312, 314, 318, 354, 360, 390,
420, 422, 434, 462, 464, 468, 510, 572, 648, 660, 662, 762, 840, 884, 888, 942, 1064, 1110,
1302, 1304, 1308, 1430, 1434, 1440, 1452, 1454, 1488, 1490, 1494, 1500, 1572, 2004, 2114, 2352,
2394, 2400, 2622, 2688, 2690, 2694, 2700, 2862, 2970, 2972, 3042, 3540, 3542, 4290, 4974, 5418,
5420, 5852, 5862, 5880, 5882, 8742, 267672, 267680
```

Every one is `p + 1` with `p` prime.

### A finite-to-infinite transfer that pays

For a translation-invariant relation, if the exact maximum on an interval of length `L` is `M`, then
`|A| <= M * ceil(N/L)`, and every infinite relation-free set has upper density at most `M/L`.

Instantiated on the exact C3 tables in the store: **C3-free upper density <= 11/50 = 0.22.** This
converts every exact finite table in that store into an unconditional infinite-density bound, which
makes it the highest-leverage single item in the collection.

### Exact plateaus

Long constant stretches in combined-constraint extremal functions, each value verified at every `n`:

- AP3-free and sum-free: **f(n) = 8 for n = 22..31**, then 9 at n = 32. Witness at 31:
  `{1, 9, 11, 14, 24, 26, 29, 31}`.
- C3-free and sum-free (distinct): **f(n) = 9 for n = 23..35**, a 13-long plateau. Witness at 35:
  `{1, 15, 17, 19, 24, 26, 31, 33, 35}`.
- C3-free and AP3-free, complete for n = 1..50, with plateau 8 on `n = 26..35`:
  `1,2,2,3,4,4,4,4,4,5,5,5,5,6,6,6,6,6,6,6,7,7,7,7,7,8,8,8,8,8,8,8,8,8,8,9,9,9,9,9,9,9,9,10,10,10,10,10,10,10`

### Shifted-Schur is a parity dichotomy

For `x + y = z + c` with repeats allowed, the extremal size is exactly a parity class: **`ceil(n/2)`
when `c` is even, `floor(n/2)` when `c` is odd**, once `n` exceeds roughly `c`. Checked for
`c` in `{0,1,2,5,10,20}` and `n = 10..30`. The construction is one line: take the parity class the
shift cannot reach.

### A Rado-family collapse

Max `|S|` in `[1..n]` avoiding `x1 + k*x2 = x3` equals max `|S|` avoiding `x1 + .. + x(k+1) = x(k+2)`,
and **both equal `n - floor(n/(k+1))`**. Two structurally different equations with an identical
extremal function at every `n` tested (`k = 1..4`, `n = 6..30`).

---

## The Lean pools: what 1,360 files actually contain

Two tarballs, read in place. The second is a **byte-for-byte duplicate** of a subdirectory of the
first and adds nothing.

| | count | share |
|---|---|---|
| exit code 0 | 614 | 45.1% |
| exit code 1, hard compile failure | 700 | 51.5% |
| **exit 0 AND the target prints an axiom footprint with no `sorryAx`** | **348** | **25.6%** |
| exit 0 but no axiom footprint printed at all | 233 | 17.1% |
| exit 0 but a declaration prints `sorryAx` | 33 | 2.4% |
| literal `sorry` in source | 402 | 29.6% |

Of the 348 verified files, 291 are distinct, covering **119 problem numbers**. But **221 of the 348
are bounded decision procedures**, and a further ~47 are self-tests of the harness wearing a problem
label. The honest read: roughly three quarters of the pool is scaffolding or failure, and most of the
remaining quarter is bounded arithmetic rather than mathematics.

### Four ways an axiom footprint and an exit code disagree

This matters because a clean `#print axioms` line is the trust signal, and it can be printed by a
file that never compiled.

1. **Exit code nonzero, clean footprint printed anyway: 51 files, 84 declarations.** Restricted to the
   file's own target theorem, **38 files**. The mechanism is a text-splicing bug that emits
   `theorem <wrapper> : namespace <X> ...`, which fails to parse, while a genuine lemma above it
   elaborated cleanly. **Real mathematics is being discarded by a wrapper bug.**
2. **Exit code 0 but a declaration prints `sorryAx`: 33 files.** Notably every strengthening `step`
   file is in this set while its `base` and `implication` siblings pass: the ladders never close
   their induction step.
3. **Exit code 0 while the paired log contains hard Lean errors: 9 files.** This is the serious one,
   because exit 0 is what downstream tooling trusts.
4. **A log printing `EXIT=0` next to `invalid 'import' command` with zero declarations elaborated: 1.**

### Vacuity, with names

37 of the 348 match a vacuity pattern. The clearest are worth printing because they show what a
"verified theorem" can be:

```lean
theorem ... : forall n, selfCheck n = true    where   def selfCheck n := n == n
L1Statement := forall n d : Int, d != 0 -> d != 0 /\ n = n
... certifies a scan over   let registry : List RegistryEntry := []
check_witness k := Nat.Prime 2 && (List.range k).all (fun _ => List.prod [1] % 2 == 1)
... second conjunct ends   || true
```

plus `(2 : Rat) / 4 = 1 / 2`, `2 + 2 = 4`, `n % 2 < 2`, and `1/3 + 1/6 = 1/2`.

### The genuine ones

The strongest self-contained files in the pool, all exit 0, no `sorry`, no `native_decide`, footprint
exactly `[propext, Classical.choice, Quot.sound]`:

- `erdos477_no_square_tiling` : there is no set `A` of integers such that every `n` has a unique
  representation `n = a + k^2` with `a` in `A`. 60 lines, complete.
- Erdos 949 core: a `decide +kernel` finite core over 1,024 subsets transferred to a universal
  statement over sets of reals, plus a sharpness witness `{1,4,6}`.
- `cover20_point_degree` : in any family of 6-subsets of a 13-point set covering every triple, every
  point lies in at least 8 blocks. **The linter shows the cardinality hypothesis is unused, so the
  theorem is stronger than its statement advertises.**
- `erdos700_choose_q_gcd` : for primes `p < q`, `gcd(pq, C(pq, q)) = p`. Lucas-based, fully general.
- Erdos 885 duality: `(exists a b, ab = N and b <= a and a - b = d)` iff `(exists s, s^2 = d^2 + 4N)`,
  general in `N` and `d`.
- Erdos 289: a `decide +kernel` fragment plus a **proved** rational-to-natural bridge, which is what
  makes it a theorem rather than a numeral check.
- `3^a divides 2^(3^a) + 1`, general; `2^(2^j p) = 2^(2^j) mod (2^j p)` for odd prime `p`;
  `9 | 2^n + 1` iff `n = 3 mod 6`; `sigma_1` iterates strictly increase for `n >= 2`.

One caution on the largest file in the pool: its headline `f(4) >= 49` takes two of its own key
facts as **hypotheses** rather than proving them, and a supporting lemma assumes the `f(3) >= 19`
bound. The file's own docstring is honest about this; a reader skimming for the theorem name would
not be.

---

## Two corrections to material in the archives

**A quantifier slip presented as a disproof.** One ranked row claims that `A` union `3A` gives
`F(3N) >= 2F(N)`, hence `F(N + 2N) - F(N)` tends to infinity, "proving the literal negation of the
canonical claim." But the problem fixes `k` and asks about all large `N`; **`k = 2N` is not fixed.**
The sibling row in the same file is the real result: `F(N+1) <= F(N) + 1` for all `N >= 1` under both
conventions, sharp at `N = 1` and `N = 3`, closing `k = 1` and provably not lifting to `k >= 2`.

**A constraint-count claim that is off by two orders of magnitude.** The assertion that a `d=7` Sidon
model creates "millions of clauses" is false: exact static enumeration gives **30,912** pairwise
collision constraints, or 24,651 plus 7,680 pair variables under a reified encoding. Two symmetry
reductions are justified in the same source: fixing the zero vector is valid for nonempty sets since
coordinate complement maps pair-sum coordinate `s` to `2 - s`, and coordinate-weight ordering is
valid since permutations preserve pair-sum equality.

## One semantics warning that a reader will need

Results in the computational store carry per-relation `allow_repeats` and `ordered` flags. **Ignoring
them produces phantom contradictions.** The condition `(1,1,-1,-1)` alone is *not* Sidon; true Sidon
is that plus `(1,-2,1)`. Under the wrong reading a correct stored claim looks flatly false:

| encoding | least counterexample | differing values in [10,50] |
|---|---|---|
| distinct-quadruple only (wrong) | N = 13 | 27 |
| true Sidon (correct) | **N = 26** | **14** |

The stored claim is exactly right under the correct reading, down to the precise differing set
`{26, 27} union [35,40] union [45,50]`. A reader who skips the flags would confidently refute a
correct result.

Relatedly, one stored family is a **known sequence, not a discovery**: `(1,-2,1)` and `(1,1,-1,-1)`
together are the classical Sidon condition, and its thresholds are the known optimal Golomb ruler
lengths 6, 11, 17, 25, 34, 44 for orders 4 to 9. Good calibration, zero novelty.

## License

Apache-2.0.

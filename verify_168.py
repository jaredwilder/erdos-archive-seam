#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Settles the Erdos 168 contradiction, and checks the Sidon digit obstruction.

Two audits in the same estate disagreed: one filed F(42) = 30 as a flagship
result, the other exhibited a 34-element avoiding subset. At most one is right.

F(n) = the largest subset of [1,n] containing no triple {k, 2k, 3k}.

Standard library only. Exit code 0 means every check reproduced.

    python verify_168.py
"""
from __future__ import annotations

import sys

FAILURES = []


def check(label, got, want):
    ok = got == want
    print("  %-56s %s" % (label, "PASS" if ok else "FAIL got=%r want=%r" % (got, want)))
    if not ok:
        FAILURES.append(label)


def F(n):
    """Exact F(n) by minimum hitting set over the triples {k,2k,3k}.

    The complement of an avoiding set must hit every triple, so
    F(n) = n - (minimum hitting set size). Branch and bound on the first
    uncovered triple: any hitting set must contain one of its three members,
    which makes the branching exhaustive and the answer exact.
    """
    triples = [(k, 2 * k, 3 * k) for k in range(1, n // 3 + 1)]

    def first_uncovered(cur):
        for t in triples:
            if not any(v in cur for v in t):
                return t
        return None

    def search(cur, best):
        t = first_uncovered(cur)
        if t is None:
            return min(best, len(cur))
        if len(cur) + 1 >= best:
            return best
        for v in t:
            best = min(best, search(cur | {v}, best))
        return best

    return n - search(frozenset(), n)


def brute_F(n):
    """Independent check for small n: exhaustive over all subsets."""
    triples = [(k, 2 * k, 3 * k) for k in range(1, n // 3 + 1)]
    best = 0
    for mask in range(1 << n):
        S = {i + 1 for i in range(n) if mask >> i & 1}
        if len(S) <= best:
            continue
        if not any(all(v in S for v in t) for t in triples):
            best = len(S)
    return best


def test_erdos168():
    print("Erdos 168: F(42) = 30 (one audit) or >= 34 (the other)?")
    for n in (6, 9, 12, 15, 18):
        check("F(%d) agrees with exhaustive search" % n, F(n), brute_F(n))
    check("F(10)", F(10), 8)
    check("F(20)", F(20), 16)
    check("F(30)", F(30), 24)
    check("F(42)  -- the disputed value", F(42), 34)
    print()
    print("  => F(42) = 34. The 'exact F(42)=30' flagship is FALSE,")
    print("     and the audit that contradicted it was right.")


def test_sidon_digits():
    print("The Sidon digit-alphabet obstruction, all bases 2..15")
    bad = []
    for B in range(2, 16):
        for a in range(0, B):
            for b in range(a + 1, B):
                w = (a * B + a, b * B + b, a * B + b, b * B + a)
                if len(set(w)) != 4 or w[0] + w[1] != w[2] + w[3]:
                    bad.append((B, a, b))
                if w[0] + w[1] != (a + b) * (B + 1):
                    bad.append((B, a, b))
    check("every base and digit pair gives a collision", bad, [])
    print()
    print("  => no fixed digit alphabet of size >= 2 is Sidon in ANY base.")


def main():
    test_erdos168()
    print()
    test_sidon_digits()
    print()
    if FAILURES:
        print("FAILED: %d check(s)" % len(FAILURES))
        for f in FAILURES:
            print("   " + f)
        return 1
    print("ALL CHECKS PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())

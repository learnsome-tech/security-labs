# m02l03-02 · The lease: a borrowed credential with an end date

**Lesson:** [Moving To A Secret Manager](https://learnsome.tech/learn/security-course/m02l03) (lesson 2.3, module 2: Secrets And Identity) · Pro  
**Check:** Read along

## Goal

You can name the five properties a secret manager adds over an environment variable, and build or drive one that enforces a per caller policy, records every read, versions values for rotation, and hands out short leases.

In the lesson: Start with what the caller actually receives, because this is the piece people leave out. A lease holds the value, the version number it came from, and the moment it stops being valid. Asking whether it is valid is one comparison against the clock. Revealing the value checks validity first and raises rather than returning something the caller would go on to send to a live system. And printing a lease shows only the version, so the redaction habit from the first lesson is built into the type itself. A lease is a borrowed credential with an end date, rather than a copy you now own forever.

## Files

- [`starter/lease.py`](starter/lease.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/lease.py` alongside the lesson.
2. Notes from the lesson:
   - Line 14: revealing checks the clock first, so an ended lease cannot be used
   - Line 19: the type prints its version and never the value it holds

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l03-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m02l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

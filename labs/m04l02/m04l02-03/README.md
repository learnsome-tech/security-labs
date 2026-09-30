# m04l02-03 · Fix: the owner belongs inside the lookup

**Lesson:** [Broken Object Level Authorization](https://learnsome.tech/learn/security-course/m04l02) (lesson 4.2, module 4: API Security) · Pro  
**Check:** Read along

## Goal

You can spot an endpoint that trusts an identifier from the caller, move the ownership test inside the data lookup so no route can skip it, answer not found rather than forbidden, and recognise the nested route where the parent is checked and the child is not.

In the lesson: The fix introduces a loader that takes the caller and the identifier together and returns either an object the caller may have or nothing at all. One function owns both questions, so no route can answer only one of them. In a database this is a where clause naming the owner, not a condition written after the row comes back, because the second form is a rule that the next engineer can forget. Run the fix. Bob's own order still arrives exactly as before, which matters: a fix that breaks the legitimate path will be reverted. His neighbour's order now answers no such order. Notice the wording. Not forbidden. Forbidden would confirm the record exists.

## Files

- [`starter/bola_fixed.py`](starter/bola_fixed.py): the listing from the lesson
- [`starter/httplab.py`](starter/httplab.py)
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/bola_fixed.py` alongside the lesson.
2. Notes from the lesson:
   - Line 9: one function owns both questions, so no route can answer only one

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m04l02-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m04l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

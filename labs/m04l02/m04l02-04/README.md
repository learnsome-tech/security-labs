# m04l02-04 · The nested route trap

**Lesson:** [Broken Object Level Authorization](https://learnsome.tech/learn/security-course/m04l02) (lesson 4.2, module 4: API Security) · Pro  
**Check:** Read along

## Goal

You can spot an endpoint that trusts an identifier from the caller, move the ownership test inside the data lookup so no route can skip it, answer not found rather than forbidden, and recognise the nested route where the parent is checked and the child is not.

In the lesson: Here is the version that survives review, because it contains a visible permission test. The path carries two identifiers: a customer account, then an order underneath it. The handler confirms that the account in the path belongs to the caller and returns forbidden when it does not. The parent is checked properly, and the check ends there. The order is then fetched by its own identifier, with no requirement that it sit under that account at all. Run it. Bob passes the account check using his own account, keeps it in the path, swaps only the trailing order identifier, and walks straight out with a record belonging to a different customer.

## Files

- [`starter/httplab.py`](starter/httplab.py)
- [`starter/nested_vuln.py`](starter/nested_vuln.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/nested_vuln.py` alongside the lesson.
2. Notes from the lesson:
   - Line 11: the parent is checked properly, and the check ends there

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m04l02-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m04l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

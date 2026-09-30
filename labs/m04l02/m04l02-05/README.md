# m04l02-05 · Fix: every segment of the path is authorised

**Lesson:** [Broken Object Level Authorization](https://learnsome.tech/learn/security-course/m04l02) (lesson 4.2, module 4: API Security) · Pro  
**Check:** Read along

## Goal

You can spot an endpoint that trusts an identifier from the caller, move the ownership test inside the data lookup so no route can skip it, answer not found rather than forbidden, and recognise the nested route where the parent is checked and the child is not.

In the lesson: The repair is one added condition, and the principle behind it is worth more than the clause. A child object is only reachable through the parent the caller was authorised for, so the relationship between them is part of the query. Run the fixed handler. The legitimate read is untouched and the swapped identifier is now missing. Generalise this: any time a route has two identifiers, a caller will try mixing one of theirs with one of yours. Documents inside projects, attachments inside tickets, transactions inside accounts. Check every segment, or better, derive the child from the parent so the unauthorised combination cannot be expressed at all.

## Files

- [`starter/httplab.py`](starter/httplab.py)
- [`starter/nested_fixed.py`](starter/nested_fixed.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/nested_fixed.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m04l02-05` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m04l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

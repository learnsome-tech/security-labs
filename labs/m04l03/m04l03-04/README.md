# m04l03-04 · Fix: an allowlist for each operation

**Lesson:** [Mass Assignment](https://learnsome.tech/learn/security-course/m04l03) (lesson 4.3, module 4: API Security) · Pro  
**Check:** Read along

## Goal

You can recognise a handler that copies a request body into a model, replace it with a per-operation allowlist that rejects unknown fields loudly, and serialise responses from a named field list so private columns never reach a client.

In the lesson: The first fix is an allowlist, and the detail that makes it work is where the loop starts. The code iterates over the fields it permits and asks whether each one was sent. It never iterates over the body, so a key the server has never heard of cannot participate. Notice that the list depends on the operation: two operations, two lists. Creation may set a name, while an update may not, because renaming an account is a separate flow with its own audit trail. Run the fix. The promotion attempt at creation vanishes without comment, and the update changes the address while leaving the name exactly as it was.

## Files

- [`starter/allowlist.py`](starter/allowlist.py): the listing from the lesson
- [`starter/apilab.py`](starter/apilab.py)
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/allowlist.py` alongside the lesson.
2. Notes from the lesson:
   - Line 2: two operations, two lists: the set of writable fields is not global
   - Line 9: the loop walks the allowlist, never the request body

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m04l03-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m04l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

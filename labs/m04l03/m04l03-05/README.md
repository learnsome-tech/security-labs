# m04l03-05 · Fix: reject unknown fields loudly

**Lesson:** [Mass Assignment](https://learnsome.tech/learn/security-course/m04l03) (lesson 4.3, module 4: API Security) · Pro  
**Check:** Read along

## Goal

You can recognise a handler that copies a request body into a model, replace it with a per-operation allowlist that rejects unknown fields loudly, and serialise responses from a named field list so private columns never reach a client.

In the lesson: Silently dropping an unknown field is safe but quiet, and quiet is a missed alert. This version compares the keys that arrived with the keys it accepts and refuses the whole request when anything is left over, naming what it refused. Run the strict version. The clean request is created. The attack is answered with a bad request that lists the offending fields. That response is now a signal: count it, alert on it, and you learn that somebody is probing your schema, which is information the allowlist alone threw away. It also catches honest mistakes, so a client that misspells a field hears about it during development rather than wondering why the value never saved.

## Files

- [`starter/apilab.py`](starter/apilab.py)
- [`starter/strict.py`](starter/strict.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/strict.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m04l03-05` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m04l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

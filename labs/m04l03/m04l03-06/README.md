# m04l03-06 · The read direction: what the response names

**Lesson:** [Mass Assignment](https://learnsome.tech/learn/security-course/m04l03) (lesson 4.3, module 4: API Security) · Pro  
**Check:** Read along

## Goal

You can recognise a handler that copies a request body into a model, replace it with a per-operation allowlist that rejects unknown fields loudly, and serialise responses from a named field list so private columns never reach a client.

In the lesson: Mass assignment has a mirror image on the way out. If a handler returns whatever the database handed it, then every column the model gains later becomes public the moment somebody adds it. Run it and read the two lists. Returning the whole model ships an email address, a password hash, an internal note and a fraud score to whoever asked. The serialiser names its two public fields and returns those, so a new column is private until a human adds it to that tuple. This is why frameworks separate an input schema from an output schema, and why the output schema should be a list of names rather than an exclusion list of secrets.

## Files

- [`starter/apilab.py`](starter/apilab.py)
- [`starter/serialise.py`](starter/serialise.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/serialise.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m04l03-06` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m04l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

# m04l03-02 · Exploit: signing up as an administrator

**Lesson:** [Mass Assignment](https://learnsome.tech/learn/security-course/m04l03) (lesson 4.3, module 4: API Security) · Pro  
**Check:** Read along

## Goal

You can recognise a handler that copies a request body into a model, replace it with a per-operation allowlist that rejects unknown fields loudly, and serialise responses from a named field list so private columns never reach a client.

In the lesson: A real signup endpoint, over a real socket. The handler starts from a template holding the safe defaults: an empty name, the customer role, a zero balance. Then it copies the request body over that template. Run it. The documented request produces exactly what you expect, a customer with nothing in the bank. The second request is the same endpoint with two extra keys attached, and the response hands back an administrator with money. Nothing was bypassed and no error was raised, because the handler was asked to apply the body and it applied the body. Update takes whatever arrived, and the defaults above are decoration.

## Files

- [`starter/apilab.py`](starter/apilab.py)
- [`starter/mass_vuln.py`](starter/mass_vuln.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/mass_vuln.py` alongside the lesson.
2. Notes from the lesson:
   - Line 6: update takes whatever arrived, and the defaults above are decoration

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m04l03-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m04l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

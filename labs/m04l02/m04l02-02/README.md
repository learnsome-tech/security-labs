# m04l02-02 · Exploit: counting to somebody else's order

**Lesson:** [Broken Object Level Authorization](https://learnsome.tech/learn/security-course/m04l02) (lesson 4.2, module 4: API Security) · Pro  
**Check:** Read along

## Goal

You can spot an endpoint that trusts an identifier from the caller, move the ownership test inside the data lookup so no route can skip it, answer not found rather than forbidden, and recognise the nested route where the parent is checked and the child is not.

In the lesson: This is a real server, not a sketch. A local HTTP listener is running, the caller identity arrives in a header the way a session or a verified token would, and each line you see came back over a socket. The handler pulls the order identifier straight out of the path, looks it up, and returns it. The lookup asks which order, and never asks whose order. Run the exploit. Bob reads his own order, which is the case every test covers. Then he counts around his own identifier, and the response body for the neighbouring number contains another customer's total and the last digits of her card. No tool was needed. He changed a number.

## Files

- [`starter/bola_vuln.py`](starter/bola_vuln.py): the listing from the lesson
- [`starter/httplab.py`](starter/httplab.py)
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/bola_vuln.py` alongside the lesson.
2. Notes from the lesson:
   - Line 8: the identifier comes straight out of the path and is trusted
   - Line 9: the lookup asks which order, and never asks whose order

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m04l02-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m04l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

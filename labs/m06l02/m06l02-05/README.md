# m06l02-05 · Check headers as well as application content

**Lesson:** [Dynamic Scanning](https://learnsome.tech/learn/security-course/m06l02) (lesson 6.2, module 6: Scanning And The Pipeline) · Pro  
**Check:** Read along

## Goal

You can use a running service as a test target, demonstrate a reflected injection and an unauthorised state change, and turn those probes into a repeatable dynamic scan against the fixed service.

In the lesson: A running service also reveals defaults that source review may miss. This probe asks for a harmless page, records its response headers, and checks for four browser protections. Run the header check. Every requested header is missing, and the server banner identifies the implementation. These are small observations, but they are useful in a pipeline because they catch configuration drift in the deployed test image. The fixed service should make the same check report no missing headers and should avoid giving away a framework version that an attacker can use to narrow a search.

## Files

- [`starter/harness.py`](starter/harness.py)
- [`starter/scan_headers.py`](starter/scan_headers.py): the listing from the lesson
- [`starter/weakapp.py`](starter/weakapp.py)
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/scan_headers.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m06l02-05` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m06l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

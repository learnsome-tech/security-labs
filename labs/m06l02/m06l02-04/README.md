# m06l02-04 · The same probes pass against the fixed service

**Lesson:** [Dynamic Scanning](https://learnsome.tech/learn/security-course/m06l02) (lesson 6.2, module 6: Scanning And The Pipeline) · Pro  
**Check:** Read along

## Goal

You can use a running service as a test target, demonstrate a reflected injection and an unauthorised state change, and turn those probes into a repeatable dynamic scan against the fixed service.

In the lesson: Now the same dynamic checks target the fixed service. The response escapes the payload, supplies the required security headers, rejects an anonymous state change, and leaves the profile untouched. Run the fixed probes. Four assertions pass, and each one describes an observable property rather than a code style preference. Keep these probes small and deterministic. They become regression tests for the vulnerability, so a later refactor cannot quietly restore the behaviour that the scanner helped you remove.

## Files

- [`starter/fixedapp.py`](starter/fixedapp.py)
- [`starter/harness.py`](starter/harness.py)
- [`starter/scan_all.py`](starter/scan_all.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/scan_all.py` alongside the lesson.
2. Notes from the lesson:
   - Line 11: the assertions are the contract the pipeline can enforce

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m06l02-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m06l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

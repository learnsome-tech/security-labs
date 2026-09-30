# m06l02-03 · Probe a state change without credentials

**Lesson:** [Dynamic Scanning](https://learnsome.tech/learn/security-course/m06l02) (lesson 6.2, module 6: Scanning And The Pipeline) · Pro  
**Check:** Read along

## Goal

You can use a running service as a test target, demonstrate a reflected injection and an unauthorised state change, and turn those probes into a repeatable dynamic scan against the fixed service.

In the lesson: Dynamic checks can observe more than reflected text. This probe posts a profile change with no credential and then reads the in memory state of the test server. Run the state probe. The server returns success, the email changes, and the final assertion is true. That is an unauthorised state change, captured as a request and an effect. A useful dynamic test does not stop at status code. It checks the state that should have remained unchanged, because a friendly success response can hide a serious authorisation failure.

## Files

- [`starter/harness.py`](starter/harness.py)
- [`starter/scan_auth.py`](starter/scan_auth.py): the listing from the lesson
- [`starter/weakapp.py`](starter/weakapp.py)
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/scan_auth.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m06l02-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m06l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

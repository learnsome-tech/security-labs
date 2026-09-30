# m06l02-02 · A reflected payload proves a live path is unsafe

**Lesson:** [Dynamic Scanning](https://learnsome.tech/learn/security-course/m06l02) (lesson 6.2, module 6: Scanning And The Pipeline) · Pro  
**Check:** Read along

## Goal

You can use a running service as a test target, demonstrate a reflected injection and an unauthorised state change, and turn those probes into a repeatable dynamic scan against the fixed service.

In the lesson: This is a real probe against a server that starts on a local port for the duration of the program. The scanner sends a script tag as a search term and reads the response body. Run the probe. The payload comes back as markup, which is the observation that matters. No claim about a framework or a source file is needed. A browser receiving that response would interpret the tag in the page context. The scanner has captured a request and a response that a developer can reproduce against the test service.

## Files

- [`starter/harness.py`](starter/harness.py)
- [`starter/scan_reflect.py`](starter/scan_reflect.py): the listing from the lesson
- [`starter/weakapp.py`](starter/weakapp.py)
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/scan_reflect.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m06l02-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m06l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

# m06l01-06 · A mature scanner adds context and severity

**Lesson:** [Static Application Security Testing](https://learnsome.tech/learn/security-course/m06l01) (lesson 6.1, module 6: Scanning And The Pipeline) · Pro  
**Check:** Read along

## Goal

You can explain what static analysis can and cannot see, run a small syntax aware scanner against vulnerable code, and tune a pipeline gate so useful findings stop the build without turning every warning into an emergency.

In the lesson: A production scanner carries a larger rule set, understands more frameworks, and usually reports confidence and severity alongside the location. Bandit is not installed here, so this panel is an accurate transcript marked as missing tool. The useful fields are the stable rule, the line, and the two judgements about severity and confidence. Treat those as inputs to a policy rather than as an automatic priority list. A high confidence medium issue on an internet facing path may matter more than a low confidence high issue in dead code.

## Files

- [`starter/bandit.sh`](starter/bandit.sh): the listing from the lesson
- [`starter/command.txt`](starter/command.txt)
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/bandit.sh` alongside the lesson.
2. On a machine that has what it needs, the lesson ran it with:

   ```sh
   bash bandit.sh
   ```

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m06l01-06` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m06l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

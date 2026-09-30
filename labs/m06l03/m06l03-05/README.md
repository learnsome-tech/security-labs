# m06l03-05 · The scanner command belongs in the build

**Lesson:** [Image Scanning And Trivy](https://learnsome.tech/learn/security-course/m06l03) (lesson 6.3, module 6: Scanning And The Pipeline) · Pro  
**Check:** Read along

## Goal

You can explain why image scanning sees risks a lockfile misses, compare findings across base and application layers, and assign each finding to the team that can fix it.

In the lesson: The real pipeline command scans the immutable image digest and returns a failing status for high and critical findings. Trivy is not installed on this machine, so this panel is an accurate transcript marked as missing tool. The important details are the digest, the severity threshold, and the exit status. Run it after the image is built and before promotion, keep the report with the artefact, and make exceptions explicit with an owner and an expiry.

## Files

- [`starter/command.txt`](starter/command.txt)
- [`starter/trivy.sh`](starter/trivy.sh): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/trivy.sh` alongside the lesson.
2. On a machine that has what it needs, the lesson ran it with:

   ```sh
   bash trivy.sh
   ```

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m06l03-05` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m06l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

# m05l05-06 · Scan the image before it becomes a release

**Lesson:** [Container Security: Minimal Bases And Non Root](https://learnsome.tech/learn/security-course/m05l05) (lesson 5.5, module 5: The Supply Chain) · Pro  
**Check:** Read along

## Goal

You can reduce an image attack surface with a minimal base and a non root user, inspect those properties in a Dockerfile, and place an image scan where it can block an unsafe release.

In the lesson: A scanner belongs after the image is built and before its digest is promoted. Trivy is not installed on this machine, so this panel is an accurate transcript marked as missing tool rather than a claimed local run. The command asks for high and critical findings and returns a failing status when it finds them. That exit status is the useful part: the pipeline cannot publish a release while the policy is red. Scan the exact image digest you will deploy, keep the report as an artefact, and define an exception path with an owner and an expiry instead of teaching the pipeline to ignore the finding.

## Files

- [`starter/command.txt`](starter/command.txt)
- [`starter/scan-image.sh`](starter/scan-image.sh): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/scan-image.sh` alongside the lesson.
2. On a machine that has what it needs, the lesson ran it with:

   ```sh
   bash scan-image.sh
   ```

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m05l05-06` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m05l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

# m06l03-02 · A base swap changes the findings

**Lesson:** [Image Scanning And Trivy](https://learnsome.tech/learn/security-course/m06l03) (lesson 6.3, module 6: Scanning And The Pipeline) · Pro  
**Check:** Read along

## Goal

You can explain why image scanning sees risks a lockfile misses, compare findings across base and application layers, and assign each finding to the team that can fix it.

In the lesson: This comparison uses the same application dependencies in two images and changes only the base. Run the comparison. Both images carry seven packages, so the difference is not size. The Debian image has seven matching advisories, four of them in the base layer. The Alpine image has three findings, all from the application layer. The exact numbers are an example, not a promise that one distribution is always safer. The useful observation is that a base change changes your exposure while your own dependency set stays the same. That is why the image, not just the repository, is the scan target.

## Files

- [`starter/advisories.json`](starter/advisories.json)
- [`starter/inventory.json`](starter/inventory.json)
- [`starter/minimal.py`](starter/minimal.py): the listing from the lesson
- [`starter/scan.py`](starter/scan.py)
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/minimal.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m06l03-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m06l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

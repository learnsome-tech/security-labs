# m06l03-03 · Rank findings with a fix or without one

**Lesson:** [Image Scanning And Trivy](https://learnsome.tech/learn/security-course/m06l03) (lesson 6.3, module 6: Scanning And The Pipeline) · Pro  
**Check:** Read along

## Goal

You can explain why image scanning sees risks a lockfile misses, compare findings across base and application layers, and assign each finding to the team that can fix it.

In the lesson: A scanner report is useful when it says what can be done next. Run the report. Findings are ranked by severity, each names the package and installed version, and each says which version fixes it when a fix exists. One entry has no published fix, which needs an owner and a risk decision rather than a pretend upgrade. Keep the raw report, but make the pipeline summary this actionable view. A critical base finding belongs to the platform team; a critical application package belongs to the service team.

## Files

- [`starter/advisories.json`](starter/advisories.json)
- [`starter/inventory.json`](starter/inventory.json)
- [`starter/report.py`](starter/report.py): the listing from the lesson
- [`starter/scan.py`](starter/scan.py)
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/report.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m06l03-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m06l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

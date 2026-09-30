# m05l01-06 · What an auditing tool adds on top

**Lesson:** [Dependency Risk And Typosquatting](https://learnsome.tech/learn/security-course/m05l01) (lesson 5.1, module 5: The Supply Chain) · Pro  
**Check:** Read along

## Goal

You can describe the trust surface a single install command opens, detect a name that is one edit away from a package you meant, and name the four defences that shrink the surface without stopping delivery.

In the lesson: A review gate tells you whether somebody looked. It does not tell you whether what they approved has since turned out to be vulnerable. That is what an auditing tool does: it resolves your pinned versions against a public advisory database and reports the ones with a known problem and a fixed version. This machine does not have that tool installed, so here is what it prints, faithfully. Two packages, three advisories, and for each one the identifier and the version that fixes it. The useful discipline is to run this in the pipeline on every change and on a schedule, because the set of known vulnerabilities grows while your pinned versions stay exactly where you left them.

## Files

- [`starter/audit.sh`](starter/audit.sh): the listing from the lesson
- [`starter/command.txt`](starter/command.txt)
- [`starter/requirements.txt`](starter/requirements.txt)
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/audit.sh` alongside the lesson.
2. On a machine that has what it needs, the lesson ran it with:

   ```sh
   bash audit.sh
   ```

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m05l01-06` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m05l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

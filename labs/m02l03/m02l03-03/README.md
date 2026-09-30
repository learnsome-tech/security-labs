# m02l03-03 · The manager: policy, versions and an audit list

**Lesson:** [Moving To A Secret Manager](https://learnsome.tech/learn/security-course/m02l03) (lesson 2.3, module 2: Secrets And Identity) · Pro  
**Check:** Read along

## Goal

You can name the five properties a secret manager adds over an environment variable, and build or drive one that enforces a per caller policy, records every read, versions values for rotation, and hands out short leases.

In the lesson: Now the manager itself. It holds a policy, a version history for each name, and an audit list. Storing a value appends to the chain for that name and returns the number of the version you created, so nothing is ever overwritten. Getting a value does four things in order. It asks the policy whether this caller may read this name. It records the attempt and the verdict whether or not the answer was yes, because denied attempts are the interesting ones. It refuses loudly when the policy says no. And when the policy says yes it hands back a lease over the newest version, with a lifetime attached. Every property from the opening list is in those twenty lines.

## Files

- [`starter/vault.py`](starter/vault.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/vault.py` alongside the lesson.
2. Notes from the lesson:
   - Line 16: the policy is a table from caller to names, checked before anything
   - Line 17: the refusal is recorded too; denied reads are the useful signal

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l03-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m02l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

# m02l03-07 · The same shape, in a hosted manager

**Lesson:** [Moving To A Secret Manager](https://learnsome.tech/learn/security-course/m02l03) (lesson 2.3, module 2: Secrets And Identity) · Pro  
**Check:** Read along

## Goal

You can name the five properties a secret manager adds over an environment variable, and build or drive one that enforces a per caller policy, records every read, versions values for rotation, and hands out short leases.

In the lesson: Every managed service is this shape with more paperwork around it. Here are three calls against a hosted manager, and we are reading them rather than running them, because this machine has the command line tool but no account behind it. Creating a secret gives it a path, much like a file name. Reading names the secret and a stage, and current is a moving pointer rather than a number, which is how the provider hands you a new version without your code changing at all. Rotation is a scheduled job that writes the next version and moves that pointer. Behind all three, the provider records who called, from where, and whether the call was allowed.

## Files

- [`starter/aws.sh`](starter/aws.sh): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/aws.sh` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l03-07` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m02l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

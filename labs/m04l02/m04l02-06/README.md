# m04l02-06 · Unguessable identifiers are depth, not defence

**Lesson:** [Broken Object Level Authorization](https://learnsome.tech/learn/security-course/m04l02) (lesson 4.2, module 4: API Security) · Pro  
**Check:** Read along

## Goal

You can spot an endpoint that trusts an identifier from the caller, move the ownership test inside the data lookup so no route can skip it, answer not found rather than forbidden, and recognise the nested route where the parent is checked and the child is not.

In the lesson: A common response is to make identifiers random, and it is worth doing, but be clear about what it buys. This server issues unguessable tokens instead of counters. Four hundred sequential guesses find nothing, which removes the cheap mass harvesting we saw earlier. Then one identifier escapes, the way identifiers really escape: a referer header, a support ticket, a shared link, an error report, a browser history on a borrowed laptop. The handler still has no ownership test, so that single leak is enough. Random identifiers hide the door. They do not lock it. Treat them as a delay that buys your alerting time, and keep the ownership test underneath.

## Files

- [`starter/httplab.py`](starter/httplab.py)
- [`starter/ids.py`](starter/ids.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/ids.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m04l02-06` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m04l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

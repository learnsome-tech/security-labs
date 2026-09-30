# m05l02-05 · What this looks like in a real project

**Lesson:** [Lockfiles And Reproducible Builds](https://learnsome.tech/learn/security-course/m05l02) (lesson 5.2, module 5: The Supply Chain) · Pro  
**Check:** Read along

## Goal

You can explain what a lockfile pins and what it leaves open, verify delivered artefacts against recorded digests, and describe the three separate things that have to be fixed before a build is reproducible.

In the lesson: In Python the shape is a generated requirements file with a digest beside every pin, installed with the require hashes option. That option is the part that matters: with it, the installer refuses to install anything that is not pinned exactly and does not match a recorded hash, including transitive dependencies you never named. Other ecosystems spell it differently and mean the same thing. Three rules regardless of the language. Generate the lock, never edit it by hand. Commit it, because a lock that lives only on a build machine describes nothing. And make the build use it, since a lockfile that the install command ignores is a file full of comforting numbers.

## Files

- [`starter/requirements.lock`](starter/requirements.lock): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/requirements.lock` alongside the lesson.
2. Notes from the lesson:
   - Line 2: with require hashes, an unhashed or unpinned line is a hard error

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m05l02-05` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m05l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

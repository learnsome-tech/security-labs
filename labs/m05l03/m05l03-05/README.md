# m05l03-05 · What a dedicated generator adds

**Lesson:** [Software Bill Of Materials](https://learnsome.tech/learn/security-course/m05l03) (lesson 5.3, module 5: The Supply Chain) · Pro  
**Check:** Read along

## Goal

You can generate a machine readable bill of materials for a build, answer whether a new advisory affects you by querying it with a correct version comparison, and say what such a document does not cover.

In the lesson: You would not write the generator yourself. A dedicated tool knows how to read a dozen ecosystems, how to walk image layers, and how to recognise a vendored copy of a library that has no package metadata at all. This machine does not have one installed, so here is its table output as it really appears. Notice the type column: language packages and operating system packages come out of the same scan with a single command, which is what makes the merged inventory practical. The point is not the tool. The point is that this runs inside the build, as a step, with the output stored beside the artefact it describes.

## Files

- [`starter/command.txt`](starter/command.txt)
- [`starter/inventory.sh`](starter/inventory.sh): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/inventory.sh` alongside the lesson.
2. On a machine that has what it needs, the lesson ran it with:

   ```sh
   bash inventory.sh
   ```

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m05l03-05` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m05l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

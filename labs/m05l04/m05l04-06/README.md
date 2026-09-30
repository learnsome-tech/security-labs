# m05l04-06 · A real signing tool in the pipeline

**Lesson:** [Provenance And Signing](https://learnsome.tech/learn/security-course/m05l04) (lesson 5.4, module 5: The Supply Chain) · Pro  
**Check:** Read along

## Goal

You can explain what provenance records, verify that a release was signed by the expected builder, and reject an artefact whose bytes or origin no longer match the release policy.

In the lesson: In a container pipeline, a tool such as cosign signs an image reference and later verifies the signature and its claims. Cosign is not installed on this machine, so this panel is an accurate transcript of the two commands and their successful result, marked as a transcript for that reason. In your pipeline the important details are the same: sign the immutable digest, keep the private key out of the build job when possible, publish the signature beside the image, and make deployment fail when verification fails. A green build that never checks its signature has recorded a ceremony, not an enforceable control.

## Files

- [`starter/command.txt`](starter/command.txt)
- [`starter/sign-image.sh`](starter/sign-image.sh): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/sign-image.sh` alongside the lesson.
2. On a machine that has what it needs, the lesson ran it with:

   ```sh
   bash sign-image.sh
   ```

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m05l04-06` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m05l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

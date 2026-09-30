# m05l02 · Lockfiles And Reproducible Builds

Module 5: The Supply Chain · lesson 5.2 · Pro · [Open the lesson](https://learnsome.tech/learn/security-course/m05l02)

**Goal:** You can explain what a lockfile pins and what it leaves open, verify delivered artefacts against recorded digests, and describe the three separate things that have to be fixed before a build is reproducible.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m05l02-02](m05l02-02/) | A range is a promise you let somebody else keep | Graded |
| [m05l02-03](m05l02-03/) | A version names a release; a digest names the bytes | Graded |
| [m05l02-04](m05l02-04/) | A lock verifier, in fifteen lines | Graded |
| [m05l02-05](m05l02-05/) | What this looks like in a real project | Read along |
| [m05l02-06](m05l02-06/) | Reproducible builds pin the process | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Check what your build really pins

1. Find every dependency specification in your project that is a range, not a pin.
2. Check whether your lock records digests or only names and versions.
3. Make the install command fail when an artefact does not match its digest.
4. Build your artefact twice and compare the two digests.

> **Hint:** Container base images and pipeline actions are dependencies too, and they are usually the ones referred to by a floating tag.

## Check yourself

- What exactly does a lockfile decide, and at what moment would that otherwise be decided?
- Why is a recorded digest a stronger claim than a pinned version number?
- What does the require hashes option add beyond a file full of hashes?
- Name two common reasons the same source produces two different artefacts.
- Why is a stale lock a security problem rather than only a maintenance one?

---

[Course README](../../README.md) · [Application Security & Threat Modeling for Engineers on LearnSome.tech](https://learnsome.tech/courses/security-course)

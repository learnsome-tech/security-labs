# Exercises — Lockfiles And Reproducible Builds

Lesson `m05l02` · [Watch](https://learnsome.tech/courses/security-course/watch?lesson=m05l02)

## Exercise 1: Check what your build really pins

1. Find every dependency specification in your project that is a range, not a pin.
2. Check whether your lock records digests or only names and versions.
3. Make the install command fail when an artefact does not match its digest.
4. Build your artefact twice and compare the two digests.

> **Hint**: Container base images and pipeline actions are dependencies too, and they are usually the ones referred to by a floating tag.


---

© LearnSome.tech · support@iwantto.learnsome.tech

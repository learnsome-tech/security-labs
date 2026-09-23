# Exercises — Why Secrets Leak

Lesson `m02l01` · [Watch](https://learnsome.tech/courses/security-course/watch?lesson=m02l01)

## Exercise 1: Hunt one repository properly

1. Search a repository you own across its whole history, not the checkout, for key shaped strings.
2. For each hit, record when it was committed and how many clones of that repository exist.
3. Rotate anything you find before you attempt any cleanup, and time how long rotation takes.
4. Add an ignore rule and a check that runs before a commit, so the file cannot come back.

> **Hint**: Whole history means every branch and every tag, including branches nobody has merged.


---

© LearnSome.tech · support@iwantto.learnsome.tech

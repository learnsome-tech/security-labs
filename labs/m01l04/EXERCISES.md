# Exercises — Secure Defaults

Lesson `m01l04` · [Watch](https://learnsome.tech/courses/security-course/watch?lesson=m01l04)

## Exercise 1: Find your unsafe nothing

1. Start your service with no configuration at all and write down every effective setting.
2. Mark each as safe or unsafe if it reached production untouched.
3. Invert one unsafe default, and make the old behaviour an explicit named option.
4. Add a startup check that refuses to run with that option set in production.

> **Hint**: Cookie flags, transport verification, debug pages, allowed origins and default credentials are the usual five.


---

© LearnSome.tech · support@iwantto.learnsome.tech

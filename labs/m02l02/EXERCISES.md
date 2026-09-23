# Exercises — The Environment Variable Trap

Lesson `m02l02` · [Watch](https://learnsome.tech/courses/security-course/watch?lesson=m02l02)

## Exercise 1: Inventory one service

1. List every environment variable your service reads and mark which of them are credentials.
2. For each credential, write down who can read it today and what rotating it would involve.
3. Find one place the service starts a child process and give that child an explicit environment.
4. Move one credential to an owner only file and note everything that breaks.

> **Hint**: If the honest answer to how would I rotate this is a coordinated redeploy, that is the finding.


---

© LearnSome.tech · support@iwantto.learnsome.tech

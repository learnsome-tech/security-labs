# Exercises — Moving To A Secret Manager

Lesson `m02l03` · [Watch](https://learnsome.tech/courses/security-course/watch?lesson=m02l03)

## Exercise 1: Move one credential

1. Pick one credential and write down, by name, which callers should be able to read it.
2. Ask your manager who read it last month; if it cannot answer, that is the finding.
3. Turn one long lived value into a versioned one and rotate it without a redeploy.
4. Make one client cache a lease and refetch on expiry, rather than reading once at start up.

> **Hint**: A client that reads its secret once at start up can never benefit from rotation.


---

© LearnSome.tech · support@iwantto.learnsome.tech

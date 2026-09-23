# Exercises — Rate Limiting And Resource Consumption

Lesson `m04l04` · [Watch](https://learnsome.tech/courses/security-course/watch?lesson=m04l04)

## Exercise 1: Bound one expensive endpoint

1. Find an endpoint whose work grows with caller input.
2. Measure its normal cost and choose a small default budget.
3. Return a retry response before the expensive operation.
4. Test shared counters and an honest client retry.

> **Hint**: A status code alone is not a budget; name what it counts and where it is stored.


---

© LearnSome.tech · support@iwantto.learnsome.tech

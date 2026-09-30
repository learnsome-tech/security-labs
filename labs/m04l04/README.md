# m04l04 · Rate Limiting And Resource Consumption

Module 4: API Security · lesson 4.4 · Pro · [Open the lesson](https://learnsome.tech/learn/security-course/m04l04)

**Goal:** You can demonstrate an unlimited guessing path and an unbounded page size, then add limits with clear responses and account aware backoff.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m04l04-02](m04l04-02/) | Exploit: unlimited guesses reveal the password | Graded |
| [m04l04-03](m04l04-03/) | Fix: stop the expensive check after the budget | Graded |
| [m04l04-04](m04l04-04/) | Exploit and fix: an unbounded page size | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Bound one expensive endpoint

1. Find an endpoint whose work grows with caller input.
2. Measure its normal cost and choose a small default budget.
3. Return a retry response before the expensive operation.
4. Test shared counters and an honest client retry.

> **Hint:** A status code alone is not a budget; name what it counts and where it is stored.

## Check yourself

- Why is unlimited work a security problem even without data access?
- What should happen before an expensive password check?
- Which resource should a page size limit protect?
- Why must counters be shared across instances?
- What makes a retry response useful?

---

[Course README](../../README.md) · [Application Security & Threat Modeling for Engineers on LearnSome.tech](https://learnsome.tech/courses/security-course)

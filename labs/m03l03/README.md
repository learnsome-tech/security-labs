# m03l03 · SQL Injection: The Fix

Module 3: Web Vulnerabilities · lesson 3.3 · Pro · [Open the lesson](https://learnsome.tech/learn/security-course/m03l03)

**Goal:** You can repair SQL injection with parameter binding and prove the hostile value stays data.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m03l03-02](m03l03-02/) | Exploit: input changes the operation | Graded |
| [m03l03-03](m03l03-03/) | Fix: keep the value as data | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Practice the boundary

1. Choose one vulnerable path in a disposable test.
2. Run the exploit and record its observed effect.
3. Apply the fix and rerun the same input.
4. Keep the regression test in the repository.

> **Hint:** Use fake data and an isolated test target.

## Check yourself

- Where does input cross into an interpreter?
- What output proves the exploit worked?
- What boundary does the fix restore?

---

[Course README](../../README.md) · [Application Security & Threat Modeling for Engineers on LearnSome.tech](https://learnsome.tech/courses/security-course)

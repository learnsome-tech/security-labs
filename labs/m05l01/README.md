# m05l01 · Dependency Risk And Typosquatting

Module 5: The Supply Chain · lesson 5.1 · Pro · [Open the lesson](https://learnsome.tech/learn/security-course/m05l01)

**Goal:** You can describe the trust surface a single install command opens, detect a name that is one edit away from a package you meant, and name the four defences that shrink the surface without stopping delivery.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m05l01-02](m05l01-02/) | How wide is one dependency, really | Graded |
| [m05l01-03](m05l01-03/) | Install time: code runs before you run anything | Graded |
| [m05l01-04](m05l01-04/) | Name confusion, measured rather than guessed | Graded |
| [m05l01-05](m05l01-05/) | Treat a new dependency the way you treat code | Graded |
| [m05l01-06](m05l01-06/) | What an auditing tool adds on top | Read along |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Measure your own surface

1. Print the full transitive closure of your project and count the packages.
2. For each direct dependency, find how many accounts can publish it.
3. Run a one edit check of your requirements against the popular names.
4. Pick the smallest dependency you have and try deleting it.

> **Hint:** The closure is usually five to ten times the list you wrote by hand; the account count is the number that changes minds.

## Check yourself

- Why is the count of maintainer accounts a better risk measure than the count of packages?
- At what moment does a package first get to run code on your machine?
- What does an edit distance check catch that a human reviewer reading a diff usually misses?
- What does an auditing tool tell you that a review gate cannot?
- Why does an internal mirror help during an incident?

---

[Course README](../../README.md) · [Application Security & Threat Modeling for Engineers on LearnSome.tech](https://learnsome.tech/courses/security-course)

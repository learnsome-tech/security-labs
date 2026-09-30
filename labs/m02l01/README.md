# m02l01 · Why Secrets Leak

Module 2: Secrets And Identity · lesson 2.1 · Pro · [Open the lesson](https://learnsome.tech/learn/security-course/m02l01)

**Goal:** You can name the ordinary routes a secret takes out of a system, prove that deleting a committed file does not remove it, and stop a configuration object or a request logger from printing a live credential.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m02l01-02](m02l01-02/) | Deleting a committed secret does not remove it | Graded |
| [m02l01-03](m02l01-03/) | Exploit: the helpful exception handler | Graded |
| [m02l01-04](m02l01-04/) | Fix: a type that refuses to print itself | Graded |
| [m02l01-05](m02l01-05/) | Exploit: the request logger that records everything | Graded |
| [m02l01-06](m02l01-06/) | Fix: mask at the logger, not at every call site | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Hunt one repository properly

1. Search a repository you own across its whole history, not the checkout, for key shaped strings.
2. For each hit, record when it was committed and how many clones of that repository exist.
3. Rotate anything you find before you attempt any cleanup, and time how long rotation takes.
4. Add an ignore rule and a check that runs before a commit, so the file cannot come back.

> **Hint:** Whole history means every branch and every tag, including branches nobody has merged.

## Check yourself

- Why does committing a deletion fail to remove a secret from a repository?
- What does a redacting type protect that a careful print statement does not?
- Why is the redaction filter attached to the logger rather than to each call site?
- Why is rotation the first response rather than rewriting history?
- Name two routes out of a system that involve no code at all.

---

[Course README](../../README.md) · [Application Security & Threat Modeling for Engineers on LearnSome.tech](https://learnsome.tech/courses/security-course)

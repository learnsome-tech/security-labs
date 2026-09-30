# m01l02 · Authentication Versus Authorisation

Module 1: The Security Mindset · lesson 1.2 · Free · [Open the lesson](https://learnsome.tech/learn/security-course/m01l02)

**Goal:** You can say which of the two questions a piece of code is answering, verify a password safely with a memory-hard hash and a constant-time compare, and spot the two classic authorisation mistakes: no ownership check, and trusting a role the client sent.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m01l02-02](m01l02-02/) | Authentication, done the boring correct way | Graded |
| [m01l02-03](m01l02-03/) | Exploit: authenticated, and reading somebody else's note | Graded |
| [m01l02-04](m01l02-04/) | Fix: the owner is part of the lookup | Graded |
| [m01l02-05](m01l02-05/) | Exploit: believing the role the client sent | Graded |
| [m01l02-06](m01l02-06/) | Fix: the server decides what the caller is | Graded |

## Check yourself

- In one sentence each, what question does authentication answer and what question does authorisation answer?
- Why is compare_digest used instead of the equality operator when checking a derived key?
- Why should the ownership check live inside the database query rather than after it?
- Why does the fixed lookup answer no such note rather than forbidden?
- Name three things a client can send that are not evidence of that client's rights.

---

[Course README](../../README.md) · [Application Security & Threat Modeling for Engineers on LearnSome.tech](https://learnsome.tech/courses/security-course)

# m04l03 · Mass Assignment

Module 4: API Security · lesson 4.3 · Pro · [Open the lesson](https://learnsome.tech/learn/security-course/m04l03)

**Goal:** You can recognise a handler that copies a request body into a model, replace it with a per-operation allowlist that rejects unknown fields loudly, and serialise responses from a named field list so private columns never reach a client.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m04l03-02](m04l03-02/) | Exploit: signing up as an administrator | Read along |
| [m04l03-03](m04l03-03/) | Exploit: an update that changes the owner | Read along |
| [m04l03-04](m04l03-04/) | Fix: an allowlist for each operation | Read along |
| [m04l03-05](m04l03-05/) | Fix: reject unknown fields loudly | Read along |
| [m04l03-06](m04l03-06/) | The read direction: what the response names | Read along |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Find the copy, and name your fields

1. Search for update, assign, merge and spread patterns applied to a request body.
2. For one endpoint, list the model fields the body can currently reach.
3. Replace it with a writable allowlist and reject unknown fields with a bad request.
4. Replace the response with a serialiser naming only the public fields.

> **Hint:** Admin flags, balances, owner references, verification booleans and state machine columns are the fields worth checking first.

## Check yourself

- Why does a handler that copies the request body grant more than the documentation promises?
- Why is an allowlist that iterates over permitted fields safer than filtering the body?
- Give one reason to reject unknown fields rather than ignore them.
- Why can the writable field list differ between a create and an update?
- What goes wrong when a response returns the whole database model?

---

[Course README](../../README.md) · [Application Security & Threat Modeling for Engineers on LearnSome.tech](https://learnsome.tech/courses/security-course)

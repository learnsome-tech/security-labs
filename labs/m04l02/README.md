# m04l02 · Broken Object Level Authorization

Module 4: API Security · lesson 4.2 · Pro · [Open the lesson](https://learnsome.tech/learn/security-course/m04l02)

**Goal:** You can spot an endpoint that trusts an identifier from the caller, move the ownership test inside the data lookup so no route can skip it, answer not found rather than forbidden, and recognise the nested route where the parent is checked and the child is not.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m04l02-02](m04l02-02/) | Exploit: counting to somebody else's order | Read along |
| [m04l02-03](m04l02-03/) | Fix: the owner belongs inside the lookup | Read along |
| [m04l02-04](m04l02-04/) | The nested route trap | Read along |
| [m04l02-05](m04l02-05/) | Fix: every segment of the path is authorised | Read along |
| [m04l02-06](m04l02-06/) | Unguessable identifiers are depth, not defence | Read along |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Two accounts and a list of identifiers

1. List every endpoint whose path or body carries an object identifier.
2. For each one, find where the caller identity meets the data access.
3. Write a test where a second account tries to read, update and delete.
4. Fix by moving ownership into the query, and answer not found.

> **Hint:** Start with export, download, invoice and report endpoints: they carry identifiers and return the most per request.

## Check yourself

- Why is an identifier in a path treated as untrusted input?
- What does moving the ownership test into the query prevent that a later check does not?
- Why answer not found instead of forbidden for an object owned by somebody else?
- In a nested route, which identifier is usually left unchecked, and why?
- What do unguessable identifiers buy you, and what do they not buy you?

---

[Course README](../../README.md) · [Application Security & Threat Modeling for Engineers on LearnSome.tech](https://learnsome.tech/courses/security-course)

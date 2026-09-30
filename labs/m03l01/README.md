# m03l01 · Injection In All Its Forms

Module 3: Web Vulnerabilities · lesson 3.1 · Pro · [Open the lesson](https://learnsome.tech/learn/security-course/m03l01)

**Goal:** You can recognise injection as one bug in many interpreters, name the interpreter a piece of code is talking to, and choose the strongest defence available: parameters first, an allowlist where the grammar has no parameters, and escaping only as a last resort.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m03l01-02](m03l01-02/) | Injection one: the database | Graded |
| [m03l01-03](m03l01-03/) | Injection two: the command shell | Graded |
| [m03l01-04](m03l01-04/) | Injection three: the template string | Graded |
| [m03l01-07](m03l01-07/) | The same three inputs, defended | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Find the interpreter in your own service

1. List every place your code builds a string that another program will parse
2. For each one, name the interpreter and say which of the three defences applies
3. Rewrite one concatenation as a bound parameter and run its tests
4. Find a template whose text could come from a user, and move it into the repository

> **Hint:** Search for string concatenation and format calls near the words execute, run, render and query.

## Check yourself

- State in one sentence what all injection bugs have in common, whatever the interpreter.
- Why does printing the assembled query make the database bug obvious?
- Why is a deny list of dangerous words a losing defence?
- Give one example of a place in SQL where a bound parameter cannot be used, and say what to do instead.
- Why is a template supplied by a user equivalent to letting that user run code?

---

[Course README](../../README.md) · [Application Security & Threat Modeling for Engineers on LearnSome.tech](https://learnsome.tech/courses/security-course)

# Exercises — Broken Object Level Authorization

Lesson `m04l02` · [Watch](https://learnsome.tech/courses/security-course/watch?lesson=m04l02)

## Exercise 1: Two accounts and a list of identifiers

1. List every endpoint whose path or body carries an object identifier.
2. For each one, find where the caller identity meets the data access.
3. Write a test where a second account tries to read, update and delete.
4. Fix by moving ownership into the query, and answer not found.

> **Hint**: Start with export, download, invoice and report endpoints: they carry identifiers and return the most per request.


---

© LearnSome.tech · support@iwantto.learnsome.tech

# m01l04 · Secure Defaults

Module 1: The Security Mindset · lesson 1.4 · Free · [Open the lesson](https://learnsome.tech/learn/security-course/m01l04)

**Goal:** You can tell a permissive default from a safe one, make the unsafe setting the one that has to be asked for and refused in production, and design interfaces that fail closed so a new route or a new caller is denied rather than served.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m01l04-02](m01l04-02/) | Exploit: nobody typed anything wrong | Graded |
| [m01l04-03](m01l04-03/) | Fix: safe by default, and refused where it matters | Graded |
| [m01l04-04](m01l04-04/) | Fail closed: the new route nobody thought about | Graded |
| [m01l04-05](m01l04-05/) | A default that fits in one function | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Find your unsafe nothing

1. Start your service with no configuration at all and write down every effective setting.
2. Mark each as safe or unsafe if it reached production untouched.
3. Invert one unsafe default, and make the old behaviour an explicit named option.
4. Add a startup check that refuses to run with that option set in production.

> **Hint:** Cookie flags, transport verification, debug pages, allowed origins and default credentials are the usual five.

## Check yourself

- Why do defaults beat training and checklists when a deadline is close?
- What does the startup check add that a safe default alone does not?
- What does fail closed mean for a route that has no declared policy?
- Which three cookie flags does the helper set, and what does each prevent?
- Name the four places an organisation actually sets its defaults.

---

[Course README](../../README.md) · [Application Security & Threat Modeling for Engineers on LearnSome.tech](https://learnsome.tech/courses/security-course)

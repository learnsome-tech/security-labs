# m02l02 · The Environment Variable Trap

Module 2: Secrets And Identity · lesson 2.2 · Pro · [Open the lesson](https://learnsome.tech/learn/security-course/m02l02)

**Goal:** You can explain why an environment variable beats a hardcoded credential and still is not a secret store, narrow what a child process inherits, and read a secret from a permission restricted file instead.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m02l02-02](m02l02-02/) | The step up: settings read at start up | Graded |
| [m02l02-03](m02l02-03/) | Exploit: every child process inherits it | Graded |
| [m02l02-04](m02l02-04/) | Exploit: the diagnostics dump prints it too | Graded |
| [m02l02-05](m02l02-05/) | Fix: give the child an environment, do not hand over yours | Graded |
| [m02l02-06](m02l02-06/) | Fix: a file only the service account can read | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Inventory one service

1. List every environment variable your service reads and mark which of them are credentials.
2. For each credential, write down who can read it today and what rotating it would involve.
3. Find one place the service starts a child process and give that child an explicit environment.
4. Move one credential to an owner only file and note everything that breaks.

> **Hint:** If the honest answer to how would I rotate this is a coordinated redeploy, that is the finding.

## Check yourself

- What does moving a credential into the environment fix, and what does it leave unfixed?
- Why do crash reporters and support bundles so often contain a live credential?
- What changes when you pass an explicit environment to a child process?
- Which three properties of a secret store does an environment variable lack?
- Why is a mounted secret file usually safer than an injected variable?

---

[Course README](../../README.md) · [Application Security & Threat Modeling for Engineers on LearnSome.tech](https://learnsome.tech/courses/security-course)

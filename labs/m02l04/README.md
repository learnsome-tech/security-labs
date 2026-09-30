# m02l04 · Workload Identity

Module 2: Secrets And Identity · lesson 2.4 · Pro · [Open the lesson](https://learnsome.tech/learn/security-course/m02l04)

**Goal:** You can explain how workload identity replaces a stored cloud key, verify a short lived exchange for an allowed service, and reject a caller whose identity or audience is wrong.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m02l04-02](m02l04-02/) | Static credentials stay valid until somebody rotates them | Graded |
| [m02l04-03](m02l04-03/) | Exchange an attested workload for a short token | Graded |
| [m02l04-04](m02l04-04/) | Wrong audience and wrong workload are refused | Graded |
| [m02l04-05](m02l04-05/) | Expiry turns a stolen token into a short incident | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Remove one stored cloud key

1. Choose a service that currently stores a cloud credential.
2. Define its workload identity and one allowed audience.
3. Exchange that identity for a short lived token in a test environment.
4. Delete the static key and test expiry and refusal paths.

> **Hint:** Start with one read action and one audience so the policy is easy to inspect.

## Check yourself

- What does workload identity remove from the application?
- Why check audience as well as token signature?
- How does a short lifetime reduce the impact of a leak?
- Which policy fields should be separate?
- When is a secret manager still required?

---

[Course README](../../README.md) · [Application Security & Threat Modeling for Engineers on LearnSome.tech](https://learnsome.tech/courses/security-course)

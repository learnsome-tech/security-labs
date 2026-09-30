# m06l03 · Image Scanning And Trivy

Module 6: Scanning And The Pipeline · lesson 6.3 · Pro · [Open the lesson](https://learnsome.tech/learn/security-course/m06l03)

**Goal:** You can explain why image scanning sees risks a lockfile misses, compare findings across base and application layers, and assign each finding to the team that can fix it.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m06l03-02](m06l03-02/) | A base swap changes the findings | Read along |
| [m06l03-03](m06l03-03/) | Rank findings with a fix or without one | Read along |
| [m06l03-05](m06l03-05/) | The scanner command belongs in the build | Read along |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Scan and own your image findings

1. Scan the exact digest your deployment uses.
2. Separate base findings from application findings.
3. Assign each row to a team that can change it.
4. Rebuild or upgrade one row and rerun the scan.

> **Hint:** A finding without an owner is a report, not a control.

## Check yourself

- Why does a lockfile miss findings in a container base?
- What changes when the same app moves to a different base image?
- Why include a fix version and severity in a pipeline summary?
- How should base and application findings be assigned?
- What makes an exception an owned decision rather than ignored debt?

---

[Course README](../../README.md) · [Application Security & Threat Modeling for Engineers on LearnSome.tech](https://learnsome.tech/courses/security-course)

# m06l01 · Static Application Security Testing

Module 6: Scanning And The Pipeline · lesson 6.1 · Pro · [Open the lesson](https://learnsome.tech/learn/security-course/m06l01)

**Goal:** You can explain what static analysis can and cannot see, run a small syntax aware scanner against vulnerable code, and tune a pipeline gate so useful findings stop the build without turning every warning into an emergency.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m06l01-02](m06l01-02/) | A text search confuses comments with code | Graded |
| [m06l01-03](m06l01-03/) | Find several dangerous patterns in one file | Graded |
| [m06l01-04](m06l01-04/) | Taint analysis follows data to a sink | Graded |
| [m06l01-05](m06l01-05/) | The fix changes the construction, not the warning | Graded |
| [m06l01-06](m06l01-06/) | A mature scanner adds context and severity | Read along |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Add one useful static gate

1. Run a syntax aware scanner on a service you own.
2. Baseline existing findings with an owner and review date.
3. Make new high confidence findings fail the change.
4. Fix one finding and keep the scanner output in the review.

> **Hint:** Choose a rule with a clear fix, such as a shell sink or a credential in source.

## Check yourself

- Why does a syntax tree reduce noise compared with a text search?
- What does a taint finding prove, and what does it leave for review?
- Why is a safe construction easier to gate than a comment?
- How should a team introduce a gate when old findings already exist?
- What evidence should a finding include so an engineer can act on it?

---

[Course README](../../README.md) · [Application Security & Threat Modeling for Engineers on LearnSome.tech](https://learnsome.tech/courses/security-course)

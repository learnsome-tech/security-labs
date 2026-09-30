# m06l05 · How To Stop Drowning In Findings

Module 6: Scanning And The Pipeline · lesson 6.5 · Pro · [Open the lesson](https://learnsome.tech/learn/security-course/m06l05)

**Goal:** You can turn scanner output into a small risk ranked queue, baseline existing debt, choose useful release gates, and keep exceptions from becoming permanent blind spots.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m06l05-02](m06l05-02/) | Rank by risk and action | Graded |
| [m06l05-03](m06l05-03/) | Baseline old debt and fail on new debt | Graded |
| [m06l05-04](m06l05-04/) | Deduplicate findings before assigning work | Graded |
| [m06l05-06](m06l05-06/) | Make exceptions expire | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Design one queue your team can use

1. Collect the findings from static, dependency and image scans.
2. Deduplicate them and add reachability and fix context.
3. Baseline old debt with owners and review dates.
4. Fail only on new findings that the release policy names.

> **Hint:** If the queue cannot say who changes the bytes, it is not ready for a gate.

## Check yourself

- Why is severity alone a weak way to order findings?
- What does a baseline permit, and what must it never hide?
- Why deduplicate scanner rows before assigning work?
- How should gates differ across the pipeline?
- What fields make an exception temporary and owned?

---

[Course README](../../README.md) · [Application Security & Threat Modeling for Engineers on LearnSome.tech](https://learnsome.tech/courses/security-course)

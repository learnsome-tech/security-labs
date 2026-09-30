# m01l01-05 · The open questions are the output

**Lesson:** [The Threat Model Habit](https://learnsome.tech/learn/security-course/m01l01) (lesson 1.1, module 1: The Security Mindset) · Free  
**Check:** Graded

## Goal

You can threat model a change in a few minutes by naming its data flows, its trust boundaries and its entry points, walking STRIDE over each one, and writing down only the answers that change what you build.

In the lesson: Now take one entry point, a password reset, and walk the prompt list over it. The mitigated field records which prompts this design already has an answer for. Run the prompts and the screen shows the shape of a real threat model: a column of answered, and one line marked open. That single open line is the deliverable. Elevation of privilege on a password reset is exactly where the interesting bugs live, because a reset link is a credential, and a credential that is guessable or reusable hands somebody another person's account. A model that ends with every letter answered has usually not been done honestly.

## Files

- [`starter/stride.py`](starter/stride.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l01/m01l01-05/starter`
2. Read `stride.py`.
3. Run it: `python3 stride.py`.
4. Check it from the repository root: `./check m01l01-05`.

## Expected output

```text
entry point: password reset
  S answered can someone pretend to be this?
  T answered can someone change it in flight?
  R answered can someone deny doing it?
  I answered can someone read what they should not?
  D answered can someone exhaust it?
  E OPEN can someone gain rights they were not given?
open questions: 1
```

## How to check

`./check m01l01-05` copies `starter/` into a scratch directory and runs `python3 stride.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m01l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

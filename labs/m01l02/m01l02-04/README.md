# m01l02-04 · Fix: the owner is part of the lookup

**Lesson:** [Authentication Versus Authorisation](https://learnsome.tech/learn/security-course/m01l02) (lesson 1.2, module 1: The Security Mindset) · Free  
**Check:** Graded

## Goal

You can say which of the two questions a piece of code is answering, verify a password safely with a memory-hard hash and a constant-time compare, and spot the two classic authorisation mistakes: no ownership check, and trusting a role the client sent.

In the lesson: The fix is one clause, and the shape of it matters more than the length. The ownership test sits in the same place as the lookup, so there is no route to the data that skips the check. In a real service that means the owner goes into the database query rather than into an if statement after it, which is the difference between a rule and a hope. Run the fixed version and bob gets the same answer as a note that does not exist. That wording is deliberate. Telling him he is forbidden confirms that note one exists and belongs to somebody, and that is free reconnaissance you do not need to give away.

## Files

- [`starter/bola_fixed.py`](starter/bola_fixed.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l02/m01l02-04/starter`
2. Read `bola_fixed.py`.
3. Notes from the lesson:
   - Line 8: no such note, not forbidden: do not confirm that the object exists
4. Run it: `python3 bola_fixed.py`.
5. Check it from the repository root: `./check m01l02-04`.

## Expected output

```text
bob is authenticated: True
bob asks for his own note: bob lunch order
bob asks for note one: no such note
authorisation answers what you may touch
```

## How to check

`./check m01l02-04` copies `starter/` into a scratch directory and runs `python3 bola_fixed.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m01l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

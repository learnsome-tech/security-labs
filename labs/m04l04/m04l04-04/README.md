# m04l04-04 · Exploit and fix: an unbounded page size

**Lesson:** [Rate Limiting And Resource Consumption](https://learnsome.tech/learn/security-course/m04l04) (lesson 4.4, module 4: API Security) · Pro  
**Check:** Graded

## Goal

You can demonstrate an unlimited guessing path and an unbounded page size, then add limits with clear responses and account aware backoff.

In the lesson: Rate limits also protect work that is not authentication. This page model has two paths: one accepts the requested size, and one applies a cap before the query. Run the page check. A request for a million rows becomes two hundred thousand rows without a cap, while the capped path returns at most one hundred. Apply bounds to page size, upload bytes, recursion depth, search cost, and fan out. The safe default should be small, and a caller that needs more should use deliberate pagination rather than one unbounded response.

## Files

- [`starter/paging.py`](starter/paging.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l04/m04l04-04/starter`
2. Read `paging.py`.
3. Run it: `python3 paging.py`.
4. Check it from the repository root: `./check m04l04-04`.

## Expected output

```text
one row: 1
million rows, no cap: 200000
million rows, capped: 100
page size is an input with a bound: True
```

## How to check

`./check m04l04-04` copies `starter/` into a scratch directory and runs `python3 paging.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m04l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

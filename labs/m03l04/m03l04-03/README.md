# m03l04-03 · Fix: keep the value as data

**Lesson:** [Cross-Site Scripting](https://learnsome.tech/learn/security-course/m03l04) (lesson 3.4, module 3: Web Vulnerabilities) · Pro  
**Check:** Graded

## Goal

You can show reflected markup and fix it with context aware output encoding.

In the lesson: Cross-Site Scripting lesson. Now run the fixed version with exactly the same input. The operation treats the value as data and the exploit effect disappears. Keep this example as a regression test, and use the safe interface at the boundary so a later caller cannot accidentally rebuild the vulnerable string.

## Files

- [`starter/fixed.py`](starter/fixed.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l04/m03l04-03/starter`
2. Read `fixed.py`.
3. Run it: `python3 fixed.py`.
4. Check it from the repository root: `./check m03l04-03`.

## Expected output

```text
tag returned as markup: False
<p>&lt;script&gt;steal()&lt;/script&gt;</p>
```

## How to check

`./check m03l04-03` copies `starter/` into a scratch directory and runs `python3 fixed.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m03l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

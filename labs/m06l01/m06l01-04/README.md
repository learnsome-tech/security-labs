# m06l01-04 · Taint analysis follows data to a sink

**Lesson:** [Static Application Security Testing](https://learnsome.tech/learn/security-course/m06l01) (lesson 6.1, module 6: Scanning And The Pipeline) · Pro  
**Check:** Graded

## Goal

You can explain what static analysis can and cannot see, run a small syntax aware scanner against vulnerable code, and tune a pipeline gate so useful findings stop the build without turning every warning into an emergency.

In the lesson: A pattern rule can spot a dangerous function, but it cannot tell whether attacker controlled data reaches it. This small taint pass starts at a request read, follows the variable named raw, and reports when that value reaches the shell sink. Run the data flow. Both functions are reported, including the one that removes a single character, because the scanner cannot prove that the attempted cleaning covers every shell metacharacter. That is a useful finding rather than a failure of the tool. The fix needs a safer API or a strict allowlist, and the human review decides which one fits the feature.

## Files

- [`starter/taint.py`](starter/taint.py): the listing from the lesson
- [`starter/taint_app.py`](starter/taint_app.py)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l01/m06l01-04/starter`
2. Read `taint.py`.
3. Run it: `python3 taint.py`.
4. Check it from the repository root: `./check m06l01-04`.

## Expected output

```text
report TAINTED via raw
report_fixed TAINTED via safe
```

## How to check

`./check m06l01-04` copies `starter/` into a scratch directory and runs `python3 taint.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m06l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

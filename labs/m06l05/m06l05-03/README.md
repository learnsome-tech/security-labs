# m06l05-03 · Baseline old debt and fail on new debt

**Lesson:** [How To Stop Drowning In Findings](https://learnsome.tech/learn/security-course/m06l05) (lesson 6.5, module 6: Scanning And The Pipeline) · Pro  
**Check:** Graded

## Goal

You can turn scanner output into a small risk ranked queue, baseline existing debt, choose useful release gates, and keep exceptions from becoming permanent blind spots.

In the lesson: A baseline lets a team make progress without pretending old debt does not exist. This program treats two known findings as existing debt and compares them with the current scan. Run the baseline check. The old rows remain visible, but only the two new findings fail the change. The baseline file needs ownership and a review date, otherwise it becomes a hiding place for permanent risk. Update it only when a reviewed decision says the old issue is accepted, fixed, or no longer present.

## Files

- [`starter/baseline.py`](starter/baseline.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l05/m06l05-03/starter`
2. Read `baseline.py`.
3. Run it: `python3 baseline.py`.
4. Check it from the repository root: `./check m06l05-03`.

## Expected output

```text
baseline findings: 2
new findings: 2
FAIL new: SEC104 new weak hash
FAIL new: SECRET new token
change accepted: False
```

## How to check

`./check m06l05-03` copies `starter/` into a scratch directory and runs `python3 baseline.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m06l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

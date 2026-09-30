# m06l05-02 · Rank by risk and action

**Lesson:** [How To Stop Drowning In Findings](https://learnsome.tech/learn/security-course/m06l05) (lesson 6.5, module 6: Scanning And The Pipeline) · Pro  
**Check:** Graded

## Goal

You can turn scanner output into a small risk ranked queue, baseline existing debt, choose useful release gates, and keep exceptions from becoming permanent blind spots.

In the lesson: This small queue adds context to a severity label: whether the path is reachable and whether a fix exists. Run the ranking. A reachable critical issue with a fix is first, followed by a reachable high issue, then an unreachable high issue, and finally a medium issue with no published fix. The exact formula is a policy choice, not a universal truth. The important habit is to make the context explicit so a team can explain why two findings with the same vendor severity have different next actions.

## Files

- [`starter/prioritise.py`](starter/prioritise.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l05/m06l05-02/starter`
2. Read `prioritise.py`.
3. Run it: `python3 prioritise.py`.
4. Check it from the repository root: `./check m06l05-02`.

## Expected output

```text
CRITICAL reachable fix - public api injection
HIGH reachable fix - secret in build log
HIGH unreachable fix - unused image package
MEDIUM reachable no fix - known library issue
```

## How to check

`./check m06l05-02` copies `starter/` into a scratch directory and runs `python3 prioritise.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m06l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

# m06l05-04 · Deduplicate findings before assigning work

**Lesson:** [How To Stop Drowning In Findings](https://learnsome.tech/learn/security-course/m06l05) (lesson 6.5, module 6: Scanning And The Pipeline) · Pro  
**Check:** Graded

## Goal

You can turn scanner output into a small risk ranked queue, baseline existing debt, choose useful release gates, and keep exceptions from becoming permanent blind spots.

In the lesson: Different scanners often describe the same underlying issue in different words. Deduplicate before assigning work, or one fix will produce three tickets and three arguments about ownership. Run the deduplicator. Four scanner rows become two issues, each assigned once. Keep the original references attached so a reviewer can trace the decision back to every tool that reported it. This is a small piece of pipeline code, but it protects attention, which is the resource a noisy security program spends first.

## Files

- [`starter/dedupe.py`](starter/dedupe.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l05/m06l05-04/starter`
2. Read `dedupe.py`.
3. Run it: `python3 dedupe.py`.
4. Check it from the repository root: `./check m06l05-04`.

## Expected output

```text
scanner rows: 4
underlying issues: 2
assign once: ('app.py', 4, 'SEC101')
assign once: ('image', 'curl', 'CVE-2023-38545')
```

## How to check

`./check m06l05-04` copies `starter/` into a scratch directory and runs `python3 dedupe.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m06l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

# m05l02-02 · A range is a promise you let somebody else keep

**Lesson:** [Lockfiles And Reproducible Builds](https://learnsome.tech/learn/security-course/m05l02) (lesson 5.2, module 5: The Supply Chain) · Pro  
**Check:** Graded

## Goal

You can explain what a lockfile pins and what it leaves open, verify delivered artefacts against recorded digests, and describe the three separate things that have to be fixed before a build is reproducible.

In the lesson: Start with the thing people call a pin but is not one. A requirement that accepts anything in a range is resolved at install time by taking the highest version that fits. Here are two snapshots of a package index, one from June and one from July, shipped as data so this is a real resolution and not a story. Run the same requirement against both. In June the answer is one version. In July the answer is a different version, because the publisher released twice in the meantime. Nothing in your repository changed. Your continuous integration was green last month and your laptop is running different code today, and neither of you did anything wrong.

## Files

- [`starter/index-in-july.json`](starter/index-in-july.json)
- [`starter/index-in-june.json`](starter/index-in-june.json)
- [`starter/resolve.py`](starter/resolve.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l02/m05l02-02/starter`
2. Read `resolve.py`.
3. Notes from the lesson:
   - Line 7: highest version inside the range, which is whatever exists today
4. Run it: `python3 resolve.py`.
5. Check it from the repository root: `./check m05l02-02`.

## Expected output

```text
index-in-june.json gives httpx 2.2.0
index-in-july.json gives httpx 2.4.1
one requirements line, two builds, two different programs
```

## How to check

`./check m05l02-02` copies `starter/` into a scratch directory and runs `python3 resolve.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m05l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

# m05l02-04 · A lock verifier, in fifteen lines

**Lesson:** [Lockfiles And Reproducible Builds](https://learnsome.tech/learn/security-course/m05l02) (lesson 5.2, module 5: The Supply Chain) · Pro  
**Check:** Graded

## Goal

You can explain what a lockfile pins and what it leaves open, verify delivered artefacts against recorded digests, and describe the three separate things that have to be fixed before a build is reproducible.

In the lesson: This is what a package manager does when you ask it to honour hashes, and it is short enough to read in full. For every entry in the lock, find the artefact, hash it, compare. Run the check over the delivered directory. Two artefacts match and are accepted. One has the right name and the right version but different bytes, because the mirror served a build from somewhere else, and the digests are printed side by side so the failure is obvious rather than mysterious. One was locked and never arrived at all, which is equally a failure: the lock is a complete list, so a missing entry means the environment is not the one you described.

## Files

- [`starter/dist/httpx-2.1.0.whl`](starter/dist/httpx-2.1.0.whl)
- [`starter/dist/idna-3.7.whl`](starter/dist/idna-3.7.whl)
- [`starter/dist/rich-13.7.1.whl`](starter/dist/rich-13.7.1.whl)
- [`starter/lock.json`](starter/lock.json)
- [`starter/lockcheck.py`](starter/lockcheck.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l02/m05l02-04/starter`
2. Read `lockcheck.py`.
3. Run it: `python3 lockcheck.py`.
4. Check it from the repository root: `./check m05l02-04`.

## Expected output

```text
PASS  httpx 2.1.0
PASS  rich 13.7.1
FAIL  idna 3.7 - wrong bytes
   locked 46b6a4585bdb1f86662e9a304bd9
   served e42c68ca83ed08d265e0346e6f30
FAIL  certifi-2024.7.4.whl - locked, but nothing arrived
```

## How to check

`./check m05l02-04` copies `starter/` into a scratch directory and runs `python3 lockcheck.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m05l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

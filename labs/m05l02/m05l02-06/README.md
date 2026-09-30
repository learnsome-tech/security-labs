# m05l02-06 · Reproducible builds pin the process

**Lesson:** [Lockfiles And Reproducible Builds](https://learnsome.tech/learn/security-course/m05l02) (lesson 5.2, module 5: The Supply Chain) · Pro  
**Check:** Graded

## Goal

You can explain what a lockfile pins and what it leaves open, verify delivered artefacts against recorded digests, and describe the three separate things that have to be fixed before a build is reproducible.

In the lesson: Now the third promise, which locking does not give you. Here is a build: take source, put it in an archive, hash the archive. Build it twice, on two different days, from source that never changed. The digests differ, because the clock is an input to the archive format even though nobody chose to make it one. Pin the timestamp and the two builds agree exactly. Embedded timestamps are the classic cause, along with file ordering, absolute paths, locale and anything derived from the machine name. A reproducible build lets a second party rebuild your release from your source and get your artefact, byte for byte, which turns a signature on that artefact into something anyone can check.

## Files

- [`starter/reproduce.py`](starter/reproduce.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l02/m05l02-06/starter`
2. Read `reproduce.py`.
3. Notes from the lesson:
   - Line 9: the timestamp goes into the archive, so the clock is an input
4. Run it: `python3 reproduce.py`.
5. Check it from the repository root: `./check m05l02-06`.

## Expected output

```text
built on monday:  66bcf4b1d0c0ab25a6ae710d
built on tuesday: 065a2dbaa5eb7c683698850b
byte identical: False
with the clock pinned: 40f2bc58a33596fab2c9c8f0
and pinned again:      40f2bc58a33596fab2c9c8f0
byte identical: True
```

## How to check

`./check m05l02-06` copies `starter/` into a scratch directory and runs `python3 reproduce.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m05l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

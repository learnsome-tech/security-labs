# m05l02-03 · A version names a release; a digest names the bytes

**Lesson:** [Lockfiles And Reproducible Builds](https://learnsome.tech/learn/security-course/m05l02) (lesson 5.2, module 5: The Supply Chain) · Pro  
**Check:** Graded

## Goal

You can explain what a lockfile pins and what it leaves open, verify delivered artefacts against recorded digests, and describe the three separate things that have to be fixed before a build is reproducible.

In the lesson: Say you have pinned the version exactly. You have named a release. You have not said anything about what arrives when your build asks a mirror for it. Here we take an artefact, record its digest the way a lock would, then flip a single bit in one byte and hash it again. The length is unchanged, the file name is unchanged, the version is unchanged, and the digest is completely different, which is the property a cryptographic hash exists to have. That is why a lock that records only names and versions is weaker than one that records digests: the first trusts your mirror and your network, and the second checks them.

## Files

- [`starter/tamper.py`](starter/tamper.py): the listing from the lesson
- [`starter/wheel.bin`](starter/wheel.bin)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l02/m05l02-03/starter`
2. Read `tamper.py`.
3. Run it: `python3 tamper.py`.
4. Check it from the repository root: `./check m05l02-03`.

## Expected output

```text
bytes we asked for: 51
digest in the lock: d0de8b6b1c4b2b0b9774cf9c73a7dc2f
one bit flipped in one byte, nothing else changed
digest of what arrived: cc72db7d2cc964c4e82a90036bd683e0
same length: True
verdict: REJECT the artefact
```

## How to check

`./check m05l02-03` copies `starter/` into a scratch directory and runs `python3 tamper.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m05l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

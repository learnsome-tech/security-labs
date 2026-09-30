# m05l05-03 · A Dockerfile can make root explicit

**Lesson:** [Container Security: Minimal Bases And Non Root](https://learnsome.tech/learn/security-course/m05l05) (lesson 5.5, module 5: The Supply Chain) · Pro  
**Check:** Graded

## Goal

You can reduce an image attack surface with a minimal base and a non root user, inspect those properties in a Dockerfile, and place an image scan where it can block an unsafe release.

In the lesson: The user identity should be visible in the Dockerfile rather than inherited from a base image that may change. This checker reads two small Dockerfiles and looks for an explicit user declaration. Run the check. The first image has a familiar base but no user line, so its process starts as root by default. The second uses a smaller base, creates a service account, and declares that account before the command runs. The check can be a simple policy, but it should be automatic. A reviewer should not have to remember to ask who owns the process in every image change.

## Files

- [`starter/dockerfile_check.py`](starter/dockerfile_check.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l05/m05l05-03/starter`
2. Read `dockerfile_check.py`.
3. Notes from the lesson:
   - Line 4: an explicit user line changes the runtime identity
4. Run it: `python3 dockerfile_check.py`.
5. Check it from the repository root: `./check m05l05-03`.

## Expected output

```text
unsafe base: python:3.14 explicit user: False
  verdict: REJECT root default
safer base: python:3.14-slim explicit user: True
  verdict: OK non root declared
```

## How to check

`./check m05l05-03` copies `starter/` into a scratch directory and runs `python3 dockerfile_check.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m05l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)

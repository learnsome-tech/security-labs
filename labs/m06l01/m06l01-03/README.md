# m06l01-03 · Find several dangerous patterns in one file

**Lesson:** [Static Application Security Testing](https://learnsome.tech/learn/security-course/m06l01) (lesson 6.1, module 6: Scanning And The Pipeline) · Pro  
**Check:** Graded

## Goal

You can explain what static analysis can and cannot see, run a small syntax aware scanner against vulnerable code, and tune a pipeline gate so useful findings stop the build without turning every warning into an emergency.

In the lesson: Now the scanner reports three different classes of problem from one file: a credential in source, evaluation of request data, and a weak hash used as a token fingerprint. Run the scanner. Each result has a line and a stable rule identifier, which means the finding can be discussed in a review and tracked over time rather than copied from a terminal into a ticket by hand. The scanner does not claim that the endpoint is exploitable. It tells you where the risky construction is, and the engineer still reads the surrounding code to decide the fix.

## Files

- [`starter/app.py`](starter/app.py)
- [`starter/sast.py`](starter/sast.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l01/m06l01-03/starter`
2. Read `sast.py`.
3. Notes from the lesson:
   - Line 10: the rule records a line and a stable rule identifier
4. Run it: `python3 sast.py`.
5. Check it from the repository root: `./check m06l01-03`.

## Expected output

```text
app.py 2 SEC103 credential in source
app.py 4 SEC101 eval on request data
app.py 6 SEC104 weak hash for a token
```

## How to check

`./check m06l01-03` copies `starter/` into a scratch directory and runs `python3 sast.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m06l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
